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

    show_car = False

    running = True
    while (running):
        clock.tick(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    show_car = not show_car

        client.get_metrics()
        x, y, direction = client.wait_for_data()
        x = x / 16
        y = y / 16
        print("X: " + str(x) + "   Y: " + str(y) + "    Direction: " + str(direction))

        #Draw the images (KEEP SCREEN INFRONT OF ANYTHING DRAWN ON TOP)
        screen.fill((90,90,90))
        game_map.drawNav(screen)

        if show_car:
            car.drawNav(screen, (x, y), direction)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    try:
        client.run(game_loop)
    except:
        traceback.print_exc()
