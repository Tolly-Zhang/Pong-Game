import pygame

defaultName = "Paddle"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultW = 20
defaultH = 100
defaultColor = (255, 255, 255)
defaultMaxSpeed = 100
defaultMaxAccel = 50
defautXSpeed = 0
defaultYSpeed = 0
defaultXAccel = 0
defaultYAccel = 0

class Paddle():
    def __init__(self, screen, name = defaultName, x = defaultX, y = defaultY, w = defaultW, h = defaultH, color=defaultColor, maxSpeed = defaultMaxSpeed, maxAccel = defaultMaxAccel, xSpeed = defautXSpeed, ySpeed = defaultYSpeed, xAccel = defaultXAccel, yAccel = defaultYAccel):
        global defaultNameNum
        #CONSTANTS
        self.screen = screen
        if name == defaultName:
            name += str(defaultNameNum)
            defaultNameNum += 1
        self.name = name
        self.screenInfo = pygame.display.Info()
        self.w = w
        self.h = h
        self.color = color
        self.maxSpeed = maxSpeed
        self.maxAccel = maxAccel
        
        #VARIABLES
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.xAccel = xAccel
        self.yAccel = yAccel
        self.hasResetPos = False

    def maxXAccel(self):
        if self.xAccel >= 0:
            self.xAccel = self.maxAccel
        else:
            self.xAccel = -1 * self.maxAccel
    
    def maxYAccel(self):
        if self.yAccel >= 0:
            self.yAccel = self.maxAccel
        else:
            self.yAccel = -1 * self.maxAccel
        
    def printSelf(self):
        print(f"Paddle Name: {self.name}")
        print(f"    Dimensions(w, h):       ({self.w}, {self.h})")
        print(f"    Position(x, y):         ({self.x}, {self.y})")
        print(f"    Color(r, g, b):         {self.color}")
        print(f"    maxSpeed(px/s)          {self.maxSpeed}")
        print(f"    X Acceleration(px/s^2): {self.xAccel}")
        print(f"    Y Acceleration(px/s^2): {self.yAccel}")

    def update(self, deltaTime):
        self.changeSpeed(deltaTime)
        self.move(deltaTime)
        self.draw()

    def changeSpeed(self, deltaTime):
        self.xSpeed = min(self.maxSpeed, self.xSpeed + self.xAccel * deltaTime)
        self.ySpeed = min(self.maxSpeed, self.ySpeed + self.yAccel * deltaTime)

    def move(self, deltaTime):
        self.x += self.xSpeed * deltaTime
        self.y += self.ySpeed * deltaTime
        
    def draw(self): 
        pygame.draw.rect(self.screen, self.color, pygame.Rect((self.x, self.y), (self.w, self.h)))

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
            print(f"Paddle: {self.name} has no reset position.")
        else:
            self.setPos(self.resetX, self.resetY)

    def resetToPos(self, x, y):
        self.setResetPos(x, y)
        self.resetPos()

    #Alignment
    
    def centerH(self):
        self.x = (self.screenInfo.current_w - self.w) / 2

    def centerV(self):
        self.y = (self.screenInfo.current_h - self.h) / 2

    def alignL(self):
        self.x = 0

    def alignR(self):
        self.x = self.screenInfo.current_w - self.w

    def alignT(self):
        self.y = 0

    def alignB(self):
        self.y = self.screenInfo.current_h - self.h
    
    def alignLC(self):
        self.alignL()
        self.centerV()
    
    def alignRC(self):
        self.alignR()
        self.centerV()
    