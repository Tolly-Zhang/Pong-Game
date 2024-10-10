import pygame

defaultName = "Paddle"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultW = 20
defaultH = 100
defaultColor = (255, 255, 255)
defaultMaxSpeed = 1000
defaultInstantStop = False
defaultMaxAccel = 100
defautXSpeed = 0
defaultYSpeed = 0
defaultXAccel = 0
defaultYAccel = 0

class Paddle():
    def __init__(self, screen = None, name = defaultName, x = defaultX, y = defaultY, w = defaultW, h = defaultH, color=defaultColor, maxSpeed = defaultMaxSpeed, instantStop = defaultInstantStop, maxAccel = defaultMaxAccel, xSpeed = defautXSpeed, ySpeed = defaultYSpeed, xAccel = defaultXAccel, yAccel = defaultYAccel):
        global defaultNameNum

        #CONSTANTS

        self.screen = screen
        if name == defaultName:
            name += " " + str(defaultNameNum)
            defaultNameNum += 1
        self.name = name
        if screen != None:
            self.screenW = self.screen.getW()
            self.screenH = self.screen.getH()
        self.w = w
        self.h = h
        self.color = color
        self.maxSpeed = maxSpeed
        self.instantStop = instantStop
        self.maxAccel = maxAccel
        
        #VARIABLES

        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.xAccel = xAccel
        self.yAccel = yAccel
        self.hasResetPosition = False
        self.yIsTargetingSpeed = False
        self.yTargetSpeed = 0
        self.xIsTargetingSpeed = False
        self.xTargetSpeed = 0
    
    def __str__(self) -> str:
        return self.name
        
    #Self Printing

    def printSelf(self):
        print("PADDLE PRINT START")
        print(f"Paddle Name: {self.name}")
        for attribute in self.__dict__:
            print(f"    {attribute}: {self.__dict__[attribute]}")
        print("PADDLE PRINT END")

    #Screen Management

    def setScreen(self, screen):
        self.screen = screen
        print(f"{self}'s screen has been set to {self.screen}.")

    #Updating and Motion

    def update(self, deltaTime):
        self.xUpdateSpeed(deltaTime)
        self.yUpdateSpeed(deltaTime)
        self.move(deltaTime)
        self.draw()

    def draw(self): 
        pygame.draw.rect(self.screen, self.color, pygame.Rect((self.x, self.y), (self.w, self.h)))

    def move(self, deltaTime):
        self.x += self.xSpeed * deltaTime
        self.y += self.ySpeed * deltaTime

    def xUpdateSpeed(self, deltaTime):
        xCollision = self.checkEdgeCollisionX()
        if self.xIsTargetingSpeed:
            self.xAimToSpeed(deltaTime)
        else:
            self.xChangeSpeedByAccel(deltaTime)
        if xCollision["Left"]:
            self.alignL()
            self.xSpeed = max(self.xSpeed, 0)
        elif xCollision["Right"]:
            self.alignR()
            self.xSpeed = min(self.xSpeed, 0)

    def yUpdateSpeed(self, deltaTime):
        yCollision = self.checkEdgeCollisionY()
        if self.yIsTargetingSpeed:
            self.yAimToSpeed(deltaTime)
        else:
            self.yChangeSpeedByAccel(deltaTime)
        if yCollision["Top"]:
            self.alignT() 
            self.ySpeed = max(self.ySpeed, 0)
        elif yCollision["Bottom"]:
            self.alignB()
            self.ySpeed = min(self.ySpeed, 0)

    def xChangeSpeedByAccel(self, deltaTime):
        self.xSpeed += self.xAccel * deltaTime
        self.xTrimSpeed()

    def yChangeSpeedByAccel(self, deltaTime):
        self.xSpeed += self.xAccel * deltaTime
        self.yTrimSpeed()

    def xTrimSpeed(self):
        if self.xSpeed > self.maxSpeed:
            self.xSpeed = self.maxSpeed
        elif self.xSpeed < -1 * self.maxSpeed:
            self.xSpeed = -1 * self.maxSpeed
            
    def yTrimSpeed(self):
        if self.ySpeed > self.maxSpeed:
            self.ySpeed = self.maxSpeed
        elif self.ySpeed < -1 * self.maxSpeed:
            self.ySpeed = -1 * self.maxSpeed

    def xSetTargetSpeed(self, speed):
        self.xTargetSpeed = speed

    def xBeginAimingSpeed(self):
        self.xIsTargetingSpeed = True
        print(f"{self} is now aiming towards a target X Speed. Standard movement will be overridden.")

    def xStopAimingSpeed(self):
        self.xIsTargetingSpeed = False
        print(f"{self} is no longer aiming towards a target X Speed. Normal movement will no longer be overridden.")

    def xAimToSpeed(self, deltaTime):
        if self.xSpeed == self.xTargetSpeed:
            return
        if self.instantStop:
            self.xSpeed = self.xTargetSpeed
        speedChange = self.maxAccel * deltaTime
        if self.xSpeed > 0 and self.xTargetSpeed < 0 and self.xSpeed > 0 and self.xTargetSpeed < 0:
            speedChange *=2
        if abs(self.xTargetSpeed - self.xSpeed) < speedChange:
            self.xSpeed = self.xTargetSpeed
        elif self.xSpeed < self.xTargetSpeed:
            self.xSpeed += speedChange
        elif self.xSpeed > self.xTargetSpeed:
            self.xSpeed -= speedChange

    def ysetTargetSpeed(self, speed):
        self.yTargetSpeed = speed

    def yBeginAimingSpeed(self):
        self.yIsTargetingSpeed = True
        print(f"{self} is now aiming towards a target Y Speed. Standard movement will be overridden.")

    def yStopAimingSpeed(self):
        self.yIsTargetingSpeed = False
        print(f"{self} is no longer aiming towards a target Y Speed. Normal movement will no longer be overridden.")

    def yAimToSpeed(self, deltaTime):
        if self.ySpeed == self.yTargetSpeed:
            return
        if self.instantStop:
            self.ySpeed = self.yTargetSpeed
            return
        speedChange = self.maxAccel * deltaTime
        if (self.ySpeed > 0 and self.yTargetSpeed < 0) or (self.ySpeed < 0 and self.yTargetSpeed > 0):
            speedChange *= 2
        if abs(self.yTargetSpeed - self.ySpeed) < speedChange:
            self.ySpeed = self.yTargetSpeed
        elif self.ySpeed < self.yTargetSpeed:
            self.ySpeed += speedChange
        elif self.ySpeed > self.yTargetSpeed:
            self.ySpeed -= speedChange

    def setStartStopTimee(self, sec):
        if sec == 0:
            self.instantStop = True
            print(f"{self} will now Start or Stop instantly.")
        elif sec > 0:
            self.maxAccel = self.maxSpeed / sec
            print(f"{self}'s acceleration has been set to {self.maxAccel}.")
        else:
            raise ArithmeticError (f"Start or Stop Time cannot be negative.")

    #Set Acceleration

    def setMaxAccel(self, maxAccel):
        self.maxAccel = maxAccel
        print(f"{self}'s maximum acceleration has been set to {self.maxAccel}.") 
    
    #Set Accleration to Max Possible

    def xSetToMaxAccel(self):
        if self.xAccel >= 0:
            self.xAccel = self.maxAccel
        else:
            self.xAccel = -1 * self.maxAccel

        print(f"{self}'s X Acceleration has been set to the maximum of {self.xAccel}.")
    
    def ySetToMaxAccel(self):
        if self.yAccel >= 0:
            self.yAccel = self.maxAccel
        else:
            self.yAccel = -1 * self.maxAccel

        print(f"{self}'s Y Acceleration has been set to the maximum of {self.yAccel}.")
        
    #Setting Position

    def setPosition(self, x, y):
        self.x = x
        self.y = y

        print(f"{self}'s position has been set to ({self.x}, {self.y}).")

    #Setting Reset Position

    def resetPosition(self):
        if not self.hasResetPosition:
            print(f"Paddle: {self} has no reset position.")
        else:
            self.setPosition(self.xResetPosition, self.yResetPosition)
            print(f"{self} has been reset to a position of ({self.x}, {self.y}).")

    def setResetPosition(self):
        self.setResetPosition(self.x, self.y)

    def setResetPosition(self, x, y):
        self.xResetPosition = x
        self.yResetPosition = y
        self.hasResetPosition = True
        print(f"{self}'s Reset Position has been set to ({self.xResetPosition}, {self.yResetPosition})")

    def resetToPosition(self, x, y):
        self.setResetPosition(x, y)
        self.resetPosition()
        print(f"{self}'s position has been reset to ({self.x}, {self.y}).")

    #Alignment
    
    def centerH(self):
        self.x = (self.screenW - self.w) / 2

    def centerV(self):
        self.y = (self.screenH - self.h) / 2

    def alignL(self):
        self.x = 0

    def alignR(self):
        self.x = self.screenW - self.w

    def alignT(self):
        self.y = 0

    def alignB(self):
        self.y = self.screenH - self.h
    
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
        if self.x >= self.screenW - self.w:
            output["Right"] = True
        return output
    
    def checkEdgeCollisionY(self):
        output = {"Top": False, "Bottom": False}
        if self.y <= 0:
            output["Top"] = True
        if self.y >= self.screenH - self.h:
            output["Bottom"] = True
        return output