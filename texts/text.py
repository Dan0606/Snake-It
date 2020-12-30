""" 
Object Oriented Text Object - 
This code is open source and free to use
"""

import pygame
import typing
pygame.init()
pygame.font.init()

class Text:
    def __init__(self, x, y, font, size, color=(0, 0, 0)):
        """__init__ constructor function for Text class

        Args:
            x (int): x position on screen
            y (int): y position on screen
            font (str): font of text
            size (int): size of text
            color (rgb tuple, optional): color of text. Defaults to (0, 0, 0).
        """
        self.x = x
        self.color = color
        self.y = y
        self.size = size
        self.font_name = font
        self.font = pygame.font.SysFont(self.font_name, self.size)
        self.text = self.font.render('', True, self.color)

    def set_text(self, text, underline = False, bold = False):
        """set_text set text caption

        Args:
            text (str): string of text
            underline (bool, optional): sets the text underline if true. Defaults to False.
            bold (bool, optional): set the text bold if true. Defaults to True.
        """
        self.underline = underline
        self.bold = bold
        if self.underline:
            self.font.set_underline(True)
        if self.bold:
            self.font.set_bold(True)
        self.text = self.font.render(text, True, self.color)
    
    def draw(self, win):
        """draw blit the text on screen

        Args:
            win (pygame.display): pygame window to display the text on
        """
        win.blit(self.text, (self.x, self.y))

    def replace(self, x : typing.Optional[int], y : typing.Optional[int], size : typing.Optional[int]):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if size != None:
            self.size = size
            self.font = pygame.font.SysFont(self.font_name, self.size)
