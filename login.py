import pygame
import os
from texts.text import Text
from texts.inputbox import InputBox
from database.database import Database
from database.db_config import Config
config = Config()
db = Database(config.get_host(), config.get_db_name(), config.get_collection())

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()

def open_login():
    clock = pygame.time.Clock()
    login_win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Log In")
    game_background = pygame.image.load("assets/backgrounds/game_background.jpg")
    username_text = Text(200, 600, "arial", 32).set_text("Username: ", underline=True, bold=True)
    password_text = Text(200, 700, "arial", 32).set_text("Password: ", underline=True, bold=True)
    texts_to_draw = [username_text, password_text]

    running = True
    while running:
        clock.tick(60)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                #exit()
    
    # for text in texts_to_draw:
    #     text.draw(login_win)
    
    login_win.blit(game_background, (0, 0))
    pygame.display.update()

open_login()