import pygame

defaultName = "Paddle"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultW = 20
defaultH = 100
defaultColor = (255, 255, 255)
defaultMaxSpeed = 1000
defaultMaxAccel = 1000
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
            name += " " + str(defaultNameNum)
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
        self.isTargetingSpeedY = False
        self.targetSpeedY = 0
        self.isTargetingSpeedX = False
        self.targetSpeedX = 0
        self.collideLeft = False
        self.collideRight = False
        self.collideTop = False
        self.collideBot = False
        
    #Self Printing

    def printSelf(self):
        print(f"Paddle Name: {self.name}")
        print(f"    Dimensions(w, h):       ({self.w}, {self.h})")
        print(f"    Position(x, y):         ({self.x}, {self.y})")
        print(f"    Color(r, g, b):         {self.color}")
        print(f"    maxSpeed(px/s)          {self.maxSpeed}")
        print(f"    X Acceleration(px/s^2): {self.xAccel}")
        print(f"    Y Acceleration(px/s^2): {self.yAccel}")

    #Updating and Motion

    def update(self, deltaTime):
        self.updateXSpeed(deltaTime)
        self.updateYSpeed(deltaTime)
        self.move(deltaTime)
        self.draw()

    def draw(self): 
        pygame.draw.rect(self.screen, self.color, pygame.Rect((self.x, self.y), (self.w, self.h)))

    def move(self, deltaTime):
        self.x += self.xSpeed * deltaTime
        self.y += self.ySpeed * deltaTime

    def updateXSpeed(self, deltaTime):
        xCollision = self.checkEdgeCollisionX()
        if self.isTargetingSpeedX:
            self.targetToSpeedX(deltaTime)
        else:
            self.changeXSpeedByAccel(deltaTime)
        if xCollision["Left"]:
            self.alignL()
            self.xSpeed = max(self.xSpeed, 0)
        elif xCollision["Right"]:
            self.alignR()
            self.xSpeed = min(self.xSpeed, 0)

    def updateYSpeed(self, deltaTime):
        yCollision = self.checkEdgeCollisionY()
        if self.isTargetingSpeedY:
            self.targetToSpeedY(deltaTime)
        else:
            self.changeYSpeedByAccel(deltaTime)
        if yCollision["Top"]:
            self.alignT() 
            self.ySpeed = max(self.ySpeed, 0)
        elif yCollision["Bottom"]:
            self.alignB()
            self.ySpeed = min(self.ySpeed, 0)

    def changeXSpeedByAccel(self, deltaTime):
        self.xSpeed += self.xAccel * deltaTime
        self.trimXSpeed()

    def changeYSpeedByAccel(self, deltaTime):
        self.xSpeed += self.xAccel * deltaTime
        self.trimYSpeed()

    def trimXSpeed(self):
        if self.xSpeed > self.maxSpeed:
            self.xSpeed = self.maxSpeed
        elif self.xSpeed < -1 * self.maxSpeed:
            self.xSpeed = -1 * self.maxSpeed
            
    def trimYSpeed(self):
        if self.ySpeed > self.maxSpeed:
            self.ySpeed = self.maxSpeed
        elif self.ySpeed < -1 * self.maxSpeed:
            self.ySpeed = -1 * self.maxSpeed

    def setYTargetSpeed(self, speed):
        self.targetSpeedY = speed

    def beginTargetingY(self):
        self.isTargetingSpeedY = True

    def stopTargetingY(self):
        self.isTargetingSpeedY = False

    def targetToSpeedY(self, deltaTime):
        if self.ySpeed == self.targetSpeedY:
            return
        speedChange = self.maxAccel * deltaTime
        if (self.ySpeed > 0 and self.targetSpeedY < 0) or (self.ySpeed < 0 and self.targetSpeedY > 0):
            speedChange *= 2
        if abs(self.targetSpeedY - self.ySpeed) < speedChange:
            self.ySpeed = self.targetSpeedY
        elif self.ySpeed < self.targetSpeedY:
            self.ySpeed += speedChange
        elif self.ySpeed > self.targetSpeedY:
            self.ySpeed -= speedChange

    def setXTargetSpeed(self, speed):
        self.targetSpeedX = speed

    def beginTargetingX(self):
        self.isTargetingSpeedX = True

    def stopTargetingX(self):
        self.isTargetingSpeedX = False

    def targetToSpeedX(self, deltaTime):
        if self.xSpeed == self.targetSpeedX:
            return
        speedChange = self.maxAccel * deltaTime
        if self.xSpeed > 0 and self.targetSpeedX < 0 and self.xSpeed > 0 and self.targetSpeedX < 0:
            speedChange *=2
        if abs(self.targetSpeedX - self.xSpeed) < speedChange:
            self.xSpeed = self.targetSpeedX
        elif self.xSpeed < self.targetSpeedX:
            self.xSpeed += speedChange
        elif self.xSpeed > self.targetSpeedX:
            self.xSpeed -= speedChange
        
    def setStartStopTimee(self, sec):
        if sec == 0:
            print("Stop time cannot be 0")
            return
        self.maxAccel = self.maxSpeed / sec

    #Set Accleration to Max Possible

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
        
    #Setting Position

    def setPos(self, x, y):
        self.x = x
        self.y = y

    #Setting Reset Position

    def resetPos(self):
        if not self.hasResetPos:
            print(f"Paddle: {self.name} has no reset position.")
        else:
            self.setPos(self.resetX, self.resetY)

    def resetToPos(self, x, y):
        self.setResetPos(x, y)
        self.resetPos()

    def setResetPos(self, x, y):
        self.resetX = x
        self.resetY = y
        self.hasResetPos = True

    def setResetCurrentPos(self):
        self.setResetPos(self.x, self.y)

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

    #Edge Collision Check

    def checkEdgeCollisionX(self):
        output = {"Left": False, "Right": False}
        if self.x <= 0:
            output["Left"] = True
        if self.x >= self.screenInfo.current_w - self.w:
            output["Right"] = True
        return output
    
    def checkEdgeCollisionY(self):
        output = {"Top": False, "Bottom": False}
        if self.y <= 0:
            output["Top"] = True
        if self.y >= self.screenInfo.current_h - self.h:
            output["Bottom"] = True
        return output