"""
Object Oriented Player Object -
Written to implement the player in Snake It game
This code is open source and free to use
"""

import pygame
from math import sqrt
from objects.heart import Heart


class Player:
    def __init__(self, image, x, y):    
        """__init__ constructor function for Player class

        Args:
            image (str.png): the player image to display on screen
            x (int): starting x position of player
            y (int): starting y position of player
        """
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.vel = 20
        self.score = 0
        self.isRight = False
        self.heart1 = Heart(1720, 26)
        self.heart2 = Heart(1780, 26)
        self.heart3 = Heart(1840, 26)
        self.hearts = [self.heart1, self.heart2, self.heart3]
        self.can_boost = True


    def move(self, win):
        """move handles movement for player object

        Args:
            win (pygame.display): the window to move the player
        """
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (self.x < 1920 - 200):
            if not self.isRight:
                self.image = pygame.transform.flip(self.image, True, False)
            if keys[pygame.K_SPACE] and self.can_boost:
                self.dash("right")
            else:
                self.x += self.vel
            self.isRight = True

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (self.x > 0):
            if self.isRight:
                self.image = pygame.transform.flip(self.image, True, False)
            if keys[pygame.K_SPACE] and self.can_boost:
                self.dash("left")
            else:
                self.x -= self.vel
            self.isRight = False  

        win.blit(self.image,(self.x, self.y))
    
    def dash(self, direction):
        if direction == "right":
            self.x += self.vel + 20
        else:
            self.x -= self.vel + 20

    def update_score(self):
        self.score += 1

            
def is_collided(x1, y1, x2, y2):
    if sqrt((x1 - x2)**2 + (y1 - y2)**2) < 100:
        return True
    return False
        
        
