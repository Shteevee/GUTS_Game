import pygame, sys, gameMap, car
from pygame.locals import *
import settings

<<<<<<< HEAD
def main():
    global pygame, car, gameMap

    display = pygame.display
    display.init()
    screen = display.set_mode(settings.screen_size)

    # car = car.Car(10,10)
    # bg = gameMap.GameMap()
    running = True
    clock = pygame.time.Clock()

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

        car.drive()
        print(car.getPos())

        Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
        screen.fill((90,90,90))
        bg.draw(screen)
        car.draw(screen)
        display.flip()

    pygame.quit()

main()
=======
clock = pygame.time.Clock()

display = pygame.display
display.init()
screen = display.set_mode((900,640))
car = car.Car(650, 600)
bg = gameMap.GameMap()
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

    car.drive(bg)
    print(car.getPos())

    #Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
    screen.fill((90,90,90))
    bg.draw(screen)
    car.draw(screen)
    display.flip()
pygame.quit()
>>>>>>> master
