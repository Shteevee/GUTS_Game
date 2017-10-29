import pygame
from pygame.locals import *

class GameMap(pygame.sprite.Sprite):
    def __init__(self, map_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(map_image)
        self.rect = self.image.get_rect()

    def scale(self, scale_factor):
        for i in range(0, scale_factor, 1):
            self.image = pygame.transform.scale2x(self.image)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    #draw map from top left of screen
    def draw(self, screen, camera):
        self.rect = self.image.get_rect()
        screen.blit(self.image, camera.apply(self))

    def drawNav(self, screen):
        screen.blit(self.image, self.image.get_rect())
