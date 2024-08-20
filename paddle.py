import pygame
defaultName = "Paddle"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultW = 20
defaultH = 100
defaultColor = (255, 255, 255)
defaultMaxSpeed = 10
defaultAccel = 1

class Paddle():
    def __init__(self, screen, name = defaultName, x = defaultX, y = defaultY, w = defaultW, h = defaultH, color=defaultColor, maxSpeed = defaultMaxSpeed, accel = defaultAccel):
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
        self.maxspeed = maxSpeed
        self.accel = accel
        #VARIABLES
        self.x = x
        self.y = y
        self.hasResetPos = False
        
    def printSelf(self):
        print(f"Paddle Name: {self.name}")
        print(f"    Dimensions(w, h):       ({self.w}, {self.h})")
        print(f"    Position(x, y):         ({self.x}, {self.y})")
        print(f"    Color(r, g, b):         {self.color}")
        print(f"    maxSpeed(px/s)          {self.maxspeed}")
        print(f"    Acceleration(px/s^2):   {self.accel}")

    def update(self):
        self.draw()
        
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
            print("Paddle object does not have reset position.")
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
    