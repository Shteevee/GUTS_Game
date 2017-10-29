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
    car = c.Car(settings.car_x / 16, settings.car_y / 16)

    running = True
    while (running):
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

        client.get_position()
        x, y = client.wait_for_data()
        car_position = (x / 16, y / 16)
        print(car_position)

        #Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
        screen.fill((90,90,90))
        game_map.drawNav(screen)
        car.drawNav(screen, car_position)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    try:
        client.run(game_loop)
    except:
        traceback.print_exc()
