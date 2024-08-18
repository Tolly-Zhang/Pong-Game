import pygame
defaultDimensions = (20, 100)
defaultColor = (255, 255, 255)
defaultMaxSpeed = 10
defaultAccel = 1

class Paddle():
    def __init__(self, position, dimensions = defaultDimensions, color=defaultColor, maxSpeed = defaultMaxSpeed, accel = defaultAccel):
        #CONSTANTS
        self.dimensions = dimensions
        self.color = color
        self.maxspeed
        self.accel = accel
        #VARIABLES
        self.position = position
    def draw(self, screen):
        pass       