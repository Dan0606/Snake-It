from texts.inputbox import InputBox
import pygame
from pygame import mixer
import os
from database.database import Database
from database.db_config import Config
from objects.button import Button
from texts.text import Text
from game import start_play

x = 0
y = 30
pygame.mixer.pre_init(44100, 16, 2, 4096)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
pygame.font.init()

config = Config()
db = Database(config.get_host(), config.get_db_name(), config.get_collection())
logged_in = False
mixer.music.load("assets/sounds/menu_music.mp3")
def run_menu(user=None, logged_in=False, music=True):
    """run_menu starts the menu
    """
    if music:
        mixer.music.play(-1)
    mixer.music.set_volume(0.05) 
    CLOCK = pygame.time.Clock()
    FPS = 60
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    started_playing = False
    # assigning values to X and Y variable 
    
    menu_win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Main Menu")
    game_background = pygame.image.load("assets/game/game_background.jpg")
    # create a font object. 
    # 1st parameter is the font file 
    # which is present in pygame. 
    # 2nd parameter is size of the font 
    
    
    # create a text suface object, 
    # on which text is drawn on it.
    if user is not None:
        user_text = Text(640, 460, "arial", 62)
        user_text.set_text(f"Welcome Back - {user['username']}", bold = True)
    title_text = Text(380, 120, "arial", 270) 
    title_text.set_text("Snake It!", bold=True)
    play_button = Button((0, 0, 0), 820, 625, 300, 107, "Play!", 76)
    login_button = Button((0, 0, 0), 600, 520, 290, 105, "Login", 74)
    signup_button = Button((0, 0, 0), 1050, 520, 290, 105, "Sign Up", 64)
    # set the center of the rectangular object. 

    images_to_blit = [[game_background, (0, 0)]]
    #input_boxes = [textinput, textinput2]
    
    # create the display surface object 
    # of specific dimension..e(X, Y). 
    
    # set the pygame window name 
    
    
    
    menu_run = True    
    while menu_run:
        title_text.draw(menu_win) 
        CLOCK.tick(FPS)
        current_fps = CLOCK.get_fps()
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos) and logged_in:
                    menu_run = False
                    start_play(user)
                    mixer.music.fadeout(1)
                    exit()
                if login_button.isOver(pos):
                    menu_run = False
                    open_login(logged_in)
                    exit()
            if event.type == pygame.MOUSEMOTION:
                #if play_button.isOver(pos) and logged_in:
                if play_button.isOver(pos):
                    play_button.color = (12, 152, 245)
                else:
                    play_button.color = (255, 255, 255)
                if login_button.isOver(pos) and not logged_in:
                    login_button.color = (12, 152, 245)
                else:
                    login_button.color = (255, 255, 255)
                if signup_button.isOver(pos) and not logged_in:
                    signup_button.color = (12, 152, 245)
                else:
                    signup_button.color = (255, 255, 255)
            if event.type == pygame.QUIT:
                menu_run = False

       
        menu_win.blit(game_background, (0, 0))
        title_text.draw(menu_win)
        if user is not None:
            user_text.draw(menu_win)
        if logged_in == True:
            play_button.draw(menu_win, outline=(0, 0, 0))
        else:
            login_button.draw(menu_win, (0, 0, 0))
            signup_button.draw(menu_win, (0, 0, 0))

        pygame.display.update()


def open_login(logged_in):
    clock = pygame.time.Clock()
    login_win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Log In")
    game_background = pygame.image.load("assets/game/game_background.jpg")
    username_text = Text(330, 170, "freesansbold", 150)
    username_text.set_text("Username: ")
    password_text = Text(330, 335, "freesansbold", 150)
    password_text.set_text("Password: ", underline=False)
    username_input = InputBox(1000, 190, 500, 70)
    password_input = InputBox(1000, 355, 500, 70, password=True)
    login_button = Button((255, 255, 255), 770, 570, 300, 110, "Login", 65)
    texts_to_draw = [username_text, password_text]
    input_boxes = [username_input, password_input]
    login_run = True
    while login_run:
        clock.tick(60)
        login_win.blit(game_background, (0, 0))
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.isOver(pos):
                    print(f"username - {username_input.text}")
                    print(f"password - {password_input.actual_text}")
                    user = db.log_in(username_input.text, password_input.actual_text)
                    if not user:
                        logged_in = False
                    else:
                        logged_in = True
                        print("Logged in is {}".format(logged_in))
                        mixer.fadeout(1)
                        run_menu(user, logged_in, music=False)
                        exit() 
            if event.type == pygame.MOUSEMOTION:
                if login_button.isOver(pos):
                    login_button.color = (12, 152, 245)
                else:
                    login_button.color = (255, 255, 255)
            if event.type == pygame.QUIT:
                login_run = False
            for box in input_boxes:
                box.handle_event(event)
                #exit()
        for box in input_boxes:
            box.draw(login_win)
        for text in texts_to_draw:
            text.draw(login_win)

        login_button.draw(login_win, outline=True)
        pygame.display.update()

if __name__ == '__main__':
    run_menu()