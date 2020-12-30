"""
Object Oriented Config Object -
Written to get data from json file, in order to get database cords
This code is open source and free to use
"""

import json

class Config:
    def __init__(self):
        """__init__ constructor function for Config class
        """
        with open("database/config.json", 'r') as f:
            self.data = json.load(f)
    
    def get_mongodb_link(self):
        """get_mongodb_link get the MongoDB connection link to connect to DB with pymongo

        Returns:
            str: connection link
        """
        return self.data["mongodb-link"]
    
    def get_username(self):
        """get_username get username from config.json file

        Returns:
            str: the username of database account
        """
        return self.data["username"]
    
    def get_password(self):
        """get_password get password from config.json file

        Returns:
            str: the password of database account
        """
        return self.data["password"]

    def get_host(self):
        """get_host creates the host link to connect MongoDB database

        Returns:
            str: the host link
        """
        link = self.get_mongodb_link()
        link = link.replace("<username>", self.get_username())
        link = link.replace("<password>", self.get_password())
        link = link.replace("<db>", self.get_db_name())
        return link

    def get_db_name(self):
        """get_db_name get the database name from MongoDB cluster

        Returns:
            str: database name
        """
        return self.data["db-name"]
    
    def get_collection(self):
        """get_collection get collection name from cluster.database

        Returns:
            str: collection name
        """
        return self.data["collection"]
        