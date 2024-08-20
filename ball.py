import pygame
defaultDiameter = 10
defaultColor = (0, 0, 0)
defaultMaxSpeed = 10
defaultDeccel = 1

class Ball():
    def __init__(self, position, diameter, color = defaultColor, maxSpeed = defaultMaxSpeed, deccel = defaultDeccel):
        #CONSTANTS
        self.color = color
        self.diameter = diameter
        self.maxSpeed = maxSpeed
        self.deccel = deccel
        #VARIABLES
        self.position = position
    def draw(self, screen, clock):
        pass