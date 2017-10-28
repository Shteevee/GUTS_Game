import pygame, sys, math
from pygame.locals import *

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)

class Camera(pygame.Surface):
    def __init__(self, width, height):
        pygame.surface.__init__('self', Rect(0,0,width,height))
        self.camera_func = simple_camera
        self.state = Rect(0,0,width, height)
        self.HALF_WIDTH = int(width/2.75)
        self.HALF_HEIGHT = int(height/5)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    #set the top left point of the camera to draw from
    def update(self, target):
        self.state.left = (-target.rect.left + self.HALF_WIDTH)
        self.state.top = (-target.rect.top + self.HALF_HEIGHT)
        # self.state = self.camera_func(self.state, target.rect)
