import pygame, sys, screen, car
from pygame.locals import *

clock = pygame.time.Clock()

display = pygame.display
display.init()
screen = display.set_mode((900,640))
car = car.Car(10,10)

running = True
while (running):
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not hasattr(event,'key'):continue
        down = event.type == KEYDOWN
        #CHANGE THESE SCALARS TO CHANGE ACCELERATIONS AND ROTATION SPEED
        if event.key==K_RIGHT: car.updateRight(down * -3)
        elif event.key==K_LEFT: car.updateLeft(down * 3)
        elif event.key==K_UP: car.updateUp(down * 0.5)
        elif event.key==K_DOWN: car.updateDown(down * -0.3)

    car.setSpeed()
    car.setRotate()
    car.move()
    print(car.getPos())

    #Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
    screen.fill((0,0,0))
    car.draw(screen)
    display.flip()
pygame.quit()
