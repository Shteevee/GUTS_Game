import pygame, sys, math
from pygame.locals import *

"""
Car class with following methods:
    -draw
    -getPos
    -setSpeed
    -setRotate
    -move
    -updateRight
    -updateLeft
    -updateUp
    -updateDown

Initialise with starting coords
"""
class Car(pygame.sprite.Sprite):
    #initialise car instance
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = start_x
        self.y = start_y
        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0
        self.speed = 0
        self.maxSpeed = 20
        self.maxReverse = -3
        self.direction = 0
        self.rad = 0
        self.rotated = None
        self.image = pygame.transform.scale2x(
                        pygame.transform.scale2x(pygame.image.load("images/car.png")))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    #Uses direction to rotate the image and send it to be drawn next update
    #also update car mask to new rotation
    def draw(self, screen, camera):
        self.rotated = pygame.transform.rotate(self.image, self.direction)
        self.rect = self.rotated.get_rect()
        self.rect.center = self.getPos()
        self.mask = pygame.mask.from_surface(self.rotated)
        screen.blit(self.rotated, camera.apply(self))

    #Return a tuple of coords
    def getPos(self):
        return (self.x, self.y)

    #call all driving methods
    def drive(self, bg):
        self.setSpeed()
        self.setRotate()
        self.move(bg)

    #Work out the speed, accelerate to cap
    def setSpeed(self):
        self.speed += (self.up+self.down)
        if self.speed > self.maxSpeed: self.speed = self.maxSpeed
        if self.speed < self.maxReverse: self.speed = self.maxReverse

    #Work out the angle in radians
    def setRotate(self):
        self.direction += (self.right+self.left)
        self.rad = self.direction * (math.pi/180)

    #Take the angle and speed and move the car
    def move(self, gameMap):
        if not pygame.sprite.collide_mask(self, gameMap):
            self.x += -self.speed * math.sin(self.rad)
            self.y += -self.speed * math.cos(self.rad)
        else:
            self.x -= -self.speed * math.sin(self.rad)
            self.y -= -self.speed * math.cos(self.rad)
            self.speed = -0.1

    def updateRight(self, r):
        self.right = r

    def updateLeft(self, l):
        self.left = l

    def updateUp(self, u):
        self.up = u

    def updateDown(self, d):
        self.down = d
