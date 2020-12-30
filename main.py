import pygame
import os
from objects.player import Player
from objects.language import Language
from database.database import Database
from database.db_config import Config
from texts.inputbox import InputBox
from texts.text import Text 
from game import start_play
from menu import run_menu

config = Config()
pygame.init()
db = Database(config.get_host(), config.get_db_name(), config.get_collection())
collection = db.collection


x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


run_menu()

