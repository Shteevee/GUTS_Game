from sys import *
from pygame import *

"""
Car class with following methods:
    -getPos


Initialise with starting coords
"""
class car:
    #initialise car instance
    def __init__(self, start_x, start_y):
        x = start_x
        y = start_y
        image = None

    def getPos(self):
        return (x,y)
