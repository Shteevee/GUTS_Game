import pygame
from pygame.locals import *

class GameMap(pygame.sprite.Sprite):
    def __init__(self, map_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(map_image)
        self.splits = 16
        self.scale = 5
        self.tile_width = self.image.get_width() / self.splits
        self.tile_height = self.image.get_height() / self.splits
        self.tiles = []

        for i in range(0, self.splits, 1):
            for j in range(0, self.splits, 1):
                self.tiles.append(self.image.subsurface(
                    Rect(i * self.tile_width,
                         j * self.tile_height,
                         self.tile_width,
                         self.tile_height)))

                for x in range(0, self.scale, 1):
                    self.tiles[-1] = pygame.transform.scale2x(self.tiles[-1])

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    #draw map from top left of screen
    def draw(self, screen, camera):
        self.rect = self.image.get_rect()
        #screen.blit(self.image, camera.apply(self))
        for i in range(0, self.splits, 1):
            for j in range(0, self.splits, 1):
                screen.blit(self.tiles[j + i * self.splits],
                            Rect(i * self.tile_width * (2 ^ self.scale),
                            j * self.tile_height * (2 ^ self.scale),
                            self.tile_width * (2 ^ self.scale),
                            self.tile_height * (2 ^ self.scale)))
