from pymongo import MongoClient
import pymongo
from errors.password_errors import *
from errors.username_errors import *

class Database(MongoClient):
    def __init__(self, host, db_name : str, collection):
        self.cluster = MongoClient(host)
        self.db = self.cluster[db_name]
        self.collection = self.db[collection]
    
    def clear_collection(self):
        """clear_collection deletes all collection (usernames, passwords, high scores, etc...)
        """
        self.collection.delete_many({})
    
    def user_exists(self, username):
        """user_exists check if a user exists in the collection

        Args:
            username (str): username

        Returns:
            bool: true if exists, false otherwise
        """
        if self.collection.find_one({"username_lower" : username.lower()}) != None:
            return True
        return False
    
    def get_query_by_username(self, username : str):
        """get_query_by_username get post / query from collection by giving username

        Args:
            username (str): username to get query of

        Raises:
            UserNameNotFoundError: if a user isn't registered in the system / collection

        Returns:
            dict: dict of post if user exists
        """
        result = self.collection.find_one({"username_lower" : username.lower()})
        if result != None:
            return result
        return UserNameNotFoundError
    
    def add_user(self, post : dict):
        """add_user adds a user to the collection

        Args:
            post (dict): post / query to insert

        Raises:
            UserNameExistsError: if username already exists in the system / collection
        """
        if self.user_exists(post["username"]):
            raise UserNameExistsError
        post["username_lower"] = post["username"].lower()
        post["best_score"] = 0
        self.collection.insert_one(post)
    
    def check_password(self, username, password):
        """check_password check if password matches the username given

        Args:
            username (str): username to check the password to
            password (str): the password to check for the given username

        Returns:
            bool: true if password matches, false otherwise
        """
        post = self.get_query_by_username(username)
        return post["password"] == password
    
    def change_password(self, query, new_password):
        """change_password changes password to a username

        Args:
            query (dict): query from database to get the username and password
            new_password (str): new password to change to

        Raises:
            WrongPasswordError: if the old password is incorrect
            SamePasswordError: if you are trying to change the password that you already have
        """
        if self.check_password(query["username"], query["password"]) == False:
            raise WrongPasswordError
        if query["password"] == new_password:
            raise SamePasswordError
        self.collection.update_one({"_id" : query["_id"]} ,{"$set" : {"password" : new_password}})
    
    def change_username(self, query, new_username, password):
        """change_username changes username

        Args:
            query (dict): query from database to get username and password
            new_username (str): new username to change to
            password (str): password to check if you have access to change this user's username

        Raises:
            WrongPasswordError: if the password is incorrect, you have no access to change username
            SameUserNameError: if you are trying to change your username to your current username
            UserNameExistsError: if you are trying to change to an already exists username
        """
        if self.check_password(query["username"], query["password"]) == False:
            raise WrongPasswordError
        if query["username"] == new_username:
            raise SameUserNameError
        if self.user_exists(new_username.lower()):
            raise UserNameExistsError
        self.collection.update_many({"_id" : query["_id"]} ,{"$set" : {"username" : new_username, "username_lower" : new_username.lower()}})
    
    def sign_up(self, username, password):
        """sign_up signs up a new user to the system / collection
        """
        post = {"username" : username, "password" : password}
        self.add_user(post)
        print(f"Signed up as {post['username']}")
    
    def log_in(self, username, password):
        """log_in logging in to a previous created account

        Raises:
            WrongPasswordError: if password is incorrect

        Returns:
            dict: query of the account logged in
        """
        post = {"username" : username, "password" : password}
        db_post = self.get_query_by_username(username)
        if db_post["username_lower"] == post["username"].lower() and db_post["password"] == post["password"]:
            print(f"Logged in as {db_post['username']}")
            return self.get_query_by_username(post["username"])
        else:
            try:
                raise WrongPasswordError
            except WrongPasswordError:
                return False

    def update_bestscore(self, username, score):
        user = self.get_query_by_username(username)
        best_score = user["best_score"]
        self.collection.update_many({"_id" : user['_id']}, {"$max" : {"best_score" : score}})
        return score > best_score