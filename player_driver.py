import traceback
import client
import pygame
from pygame.locals import *
import settings
import car as c
import camera as cam

def game_loop(client, game_map):
    clock = pygame.time.Clock()

    WIN_WIDTH = settings.screen_width
    WIN_HEIGHT = settings.screen_height

    pygame.display.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    car = c.Car(settings.car_x, settings.car_y)
    camera = cam.Camera(WIN_WIDTH, WIN_HEIGHT)
    game_map.scale(4)
    car.scale(2)
    entities = pygame.sprite.Group()
    entities.add(game_map)
    entities.add(car)

    running = True
    update = 0
    while (running):
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not hasattr(event,'key'): continue
            down = event.type == KEYDOWN
            #CHANGE THESE SCALARS TO CHANGE ACCELERATIONS AND ROTATION SPEED
            if event.key==K_RIGHT: car.updateRight(down * -2)
            elif event.key==K_LEFT: car.updateLeft(down * 2)
            elif event.key==K_UP: car.updateUp(down * 0.5)
            elif event.key==K_DOWN: car.updateDown(down * -0.3)

        car.drive(game_map)

        update += 1
        if update >= 30:
            update = 0
            client.send_position(car.getPos())

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
