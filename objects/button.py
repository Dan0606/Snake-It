"""
Object Oriented Button Object - 
Written to implement buttons easier in pygame
This code is written by @techwithtim, and free to use according to his video
"""

import pygame
pygame.init()

class Button():
    def __init__(self, color, x, y, width, height, text, size):
        """__init__ constructor function for Button object

        Args:
            color (tuple): color of the button
            x (int): x position of button
            y (int): y position of button
            width (int): width of button
            height (int): height of button
            text (str): text inside button
            size (int): text size
        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size

    def draw(self,win,outline=None):
        """draw draws the button on window

        Args:
            win (pygame.display): window to display on
            outline (bool, optional): outlines the button rectangle. Defaults to None.
        """
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('arial', self.size)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        """isOver check if mouse cursor is over the button

        Args:
            pos (tuple): x, y cords of mouse position

        Returns:
            bool: true if mouse is over, false otherwise
        """
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False