import pygame
defaultName = "Ball"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultRadius = 50
defaultColor = (255, 255, 255)
defaultMaxSpeed = 10
defaultDeccel = 1

class Ball():
    def __init__(self, screen, name = defaultName, x = defaultX, y = defaultY, radius = defaultRadius, color=defaultColor, maxSpeed = defaultMaxSpeed, deccel = defaultDeccel):
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
        self.deccel = deccel
        #VARIABLES
        self.x = x
        self.y = y
        self.hasResetPos = False

    def printSelf(self):
        print(f"Ball Name: {self.name}")
        print(f"    Diameter(d):            {self.radius}")
        print(f"    Position(x, y):         ({self.x}, {self.y})")
        print(f"    Color(r, g, b):         {self.color}")
        print(f"    maxSpeed(px/s)          {self.maxspeed}")
        print(f"    Decceleration(px/s^2):  {self.deccel}")
    
    def update(self):
        self.draw()

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