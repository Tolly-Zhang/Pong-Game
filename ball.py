import pygame
import math

defaultName = "Ball"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultRadius = 50
defaultColor = (255, 255, 255)
defaultMaxSpeed = 10
defaultTrueSpeed = 0
defaultAngle = 0
defaultXSpeed = 0
defaultYSpeed = 0
defaultDeccel = 0

class Ball():
    def __init__(self, screen, name = defaultName, x = defaultX, y = defaultY, radius = defaultRadius, color=defaultColor, maxSpeed = defaultMaxSpeed, trueSpeed = defaultTrueSpeed, angle = defaultAngle, xSpeed = defaultXSpeed, ySpeed = defaultYSpeed, deccel = defaultDeccel):
        global defaultNameNum
        #CONSTANTS
        self.screen = screen
        if name == defaultName:
            name += str(defaultNameNum)
            defaultNameNum += 1
        self.name = name
        self.screenInfo = pygame.display.Info()
        self.radius = radius
        self.color = color
        self.radius = radius
        self.maxSpeed = maxSpeed
        #VARIABLES
        self.x = x
        self.y = y
        self.trueSpeed = trueSpeed
        self.angle = angle
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.deccel = deccel
        self.hasResetPos = False

    def setAngle(self, angle):
        self.angle = angle
    
    def setTrueSpeed(self, trueSpeed):
        self.trueSpeed = trueSpeed

    def printSelf(self):
        print(f"Ball Name: {self.name}")
        print(f"    Diameter(d):            {self.radius}")
        print(f"    Position(x, y):         ({self.x}, {self.y})")
        print(f"    Color(r, g, b):         {self.color}")
        print(f"    maxSpeed(px/s)          {self.maxspeed}")
        print(f"    Decceleration(px/s^2):  {self.deccel}")
    
    def update(self, deltaTime):
        self.draw()
        self.DeccelTrueSpeed(deltaTime)
        self.updateSpeedComponents()
        self.move(deltaTime)

    
    def DeccelTrueSpeed(self, deltaTime):
        self.trueSpeed += self.deccel * deltaTime

    def updateSpeedComponents(self):
        self.xSpeed = math.cos(self.angle) * self.trueSpeed
        self.ySpeed = math.sin(self.angle) * self.trueSpeed

    def move(self, deltaTime):
        self.x += self.xSpeed * deltaTime
        self.y += self.ySpeed * deltaTime

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def setResetCurrentPos(self):
        self.setResetPos(self.x, self.y)

    def setResetPos(self, x, y):
        self.resetX = x
        self.resetY = y
        self.hasResetPos = True

    def resetPos(self):
        if not self.hasResetPos:
            print(f"Ball: {self.name} has no reset position.")
        else:
            self.setPos(self.resetX, self.resetY)

    def resetToPos(self, x, y):
        self.setResetPos(x, y)
        self.resetPos()

    def centerH(self):
        self.x = self.screenInfo.current_w / 2

    def centerV(self):
        self.y = self.screenInfo.current_h / 2

    def centerCenter(self):
        self.centerH()
        self.centerV()