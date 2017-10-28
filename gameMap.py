import pygame, sys
from pygame.locals import *

class GameMap():

    def __init__(self):
        self.image = pygame.image.load("images/map.png")
        self.mask = pygame.mask.from_surface(self.image)

    #draw map from top left of screen
    def draw(self, screen):
        screen.blit(self.image, (0,0))
