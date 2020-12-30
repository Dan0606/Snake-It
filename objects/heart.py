import pygame
pygame.init()
class Heart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/game/heart.png")

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    