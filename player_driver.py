import traceback
import client
import pygame
from pygame.locals import *
import settings
import car as c
import camera as cam

def game_loop(game_map):
    clock = pygame.time.Clock()

    WIN_WIDTH = settings.screen_width
    WIN_HEIGHT = settings.screen_height

    pygame.display.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    car = c.Car(800, 600)
    camera = cam.Camera(WIN_WIDTH, WIN_HEIGHT)
    entities = pygame.sprite.Group()
    entities.add(game_map)
    entities.add(car)

    running = True
    while (running):
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                #CHANGE THESE SCALARS TO CHANGE ACCELERATIONS AND ROTATION SPEED
                if event.key==K_RIGHT: car.updateRight(-2)
                elif event.key==K_LEFT: car.updateLeft(2)
                elif event.key==K_UP: car.updateUp(0.5)
                elif event.key==K_DOWN: car.updateDown(-0.3)

        car.drive(game_map)
        print(car.getPos())

        camera.update(car)
        #Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
        screen.fill((90,90,90))
        for e in entities:
            e.draw(screen, camera)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    try:
        client.run(game_loop)
    except:
        traceback.print_exc()
