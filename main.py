from sys import *
import pygame

running = True
while (running):

    window = pygame.display.init()
    pygame.display.set_mode((900,640))

    event = pygame.event.wait ()
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
