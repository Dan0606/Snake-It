"""
Object Oriented InputBox Object - 
Written to implement input boxes in pygame
This code is open source in some github repo
"""

import pygame as pg
pg.init()
FONT = pg.font.SysFont("freesansbold", 90)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')

class InputBox:
    def __init__(self, x, y, w, h, text='', password=False):
        """__init__ constructor function for InputBox class

        Args:
            x (int): x position of inputbox
            y (int): y position of inputbox
            w (int): with of inputbox
            h (int): height of inputbox
            text (str, optional): text inside inputbox. Defaults to ''.
            password (bool, optional): set true to show it with stars. Defaults to False.
            COLOR_ACTIVE (tuple, optional): change color when pressing inputbox. Defaults to (46, 42, 42).
            COLOR_INACTIVE (tuple, optional): change color when quiting inputbox. Defaults to (0, 0, 0).
        """
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.password = password
        self.COLOR_ACTIVE = COLOR_ACTIVE
        self.COLOR_INACTIVE = COLOR_INACTIVE
        self.actual_text = ''
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """handle_event check for collision event

        Args:
            event (pygame.event): the event occured
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text if not self.password else self.actual_text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.password:
                        self.text += "*" * len(event.unicode)
                        self.actual_text += event.unicode
                    else:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, (0, 0, 0))

    def update(self):
        """update resizes the box if the text is too long
        """
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        """draw blits everything on screen

        Args:
            screen (pygame.display): screen to draw the inputbox
        """
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)
