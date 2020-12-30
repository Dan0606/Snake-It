"""
Object Oriented Language Object -
Written to create languages objects to fall from the sky for Snake It game
This code is open source and free to use
"""

import pygame
from pygame import mixer
from math import sqrt
from random import randint, choice
from time import sleep
from objects.player import is_collided

miss_sound = mixer.Sound("assets\\sounds\\miss_sound.wav")

class Language:
    def __init__(self):
        """__init__ constructor function of Language class"""
        self.languages_images = ["assets/languages/c.png", "assets/languages/c#.png",
                            "assets/languages/c++.png", "assets/languages/elixir.png", 
                            "assets/languages/go.png", "assets/languages/java.png",
                            "assets/languages/js.png", "assets/languages/php.png", 
                            "assets/languages/ruby.png", "assets/languages/rust.png"]
        self.image = pygame.image.load(choice(self.languages_images))
        #self.image = pygame.image.load("assets/game/adir_elad.png")
        self.x = randint(0, 1700)
        self.y = 0
        self.isOnScreen = False
        self.vel = 10
        self.pre_score = 0
        

    def move(self, win, player, languages):
        self.change_vel(player.score, languages)
        """move move the language image down

        Args:
            win (pygame.display): the window to move the langauge on
        """
        if self.isOnScreen:
            self.y += self.vel
        if (self.y > 1080):
            if self.remove_heart(player.hearts) == False:
                return False
            miss_sound.play()
            self.reset_place()
        self.draw(win)

    def reset_place(self):
        """reset_place reset the object after catching it to y = 0 and choose another image
        """
        self.isOnScreen = False
        self.y = 0
        self.x = randint(0, 1700)
        self.image = pygame.image.load(choice(self.languages_images))

    def draw(self, win):
        """draw draw the object on screen

        Args:
            win (pygame.display): the screen to display the image
        """
        if self.isOnScreen:
            win.blit(self.image, (self.x, self.y))
    
    def set_on_screen(self):
        """set_on_screen set the isOnScreen variable for True
        """
        self.isOnScreen = True

    
    def change_vel(self, score, languages):
        """change_vel change the image speed according to the score

        Args:
            score (int): player's game score
        """
        if score % 10 == 0 and score != 0 and score != self.pre_score:
            self.pre_score = score  
            for lang in languages:
                lang.vel += 1
                print(lang.vel)
        # if score != 0 and score != self.pre_score:
        #     self.pre_score = score
        #     for lang in languages:
        #         lang.vel += 0.5               
        #         print(self.vel)

    @staticmethod
    def remove_heart(hearts):
        if len(hearts) != 1:
            hearts.pop(0)
        else:
            hearts.pop(0)
            return False
                