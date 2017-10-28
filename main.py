import pygame, sys, gameMap, car, camera
from pygame.locals import *
import settings



clock = pygame.time.Clock()

WIN_WIDTH = 900
WIN_HEIGHT = 640


display = pygame.display
display.init()
screen = display.set_mode((WIN_WIDTH,WIN_HEIGHT))
car = car.Car(5200, 4800)
bg = gameMap.GameMap()
camera = camera.Camera(WIN_WIDTH, WIN_HEIGHT)
entities = pygame.sprite.Group()
entities.add(bg)
entities.add(car)

running = True
while (running):
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not hasattr(event,'key'): continue
        down = event.type == KEYDOWN
        #CHANGE THESE SCALARS TO CHANGE ACCELERATIONS AND ROTATION SPEED
        if event.key==K_RIGHT: car.updateRight(down * -3)
        elif event.key==K_LEFT: car.updateLeft(down * 3)
        elif event.key==K_UP: car.updateUp(down * 0.5)
        elif event.key==K_DOWN: car.updateDown(down * -0.3)

    car.drive(bg)
    print(car.getPos())

    camera.update(car)
    #Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
    screen.fill((90,90,90))
    for e in entities:
        e.draw(screen, camera)


    display.update()
pygame.quit()
