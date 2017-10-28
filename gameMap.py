import pygame, sys
from pygame.locals import *

class GameMap(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load("images/map.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = (self.image.get_rect())

    #draw map from top left of screen
    def draw(self, screen):
        self.rect = self.image.get_rect()
        screen.blit(self.image, (0,0))
