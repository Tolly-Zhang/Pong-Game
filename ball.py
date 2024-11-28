import pygame
import math
import pygame.gfxdraw  # Import gfxdraw for anti-aliased drawing

defaultName = "Ball"
defaultNameNum = 0
defaultX = 0
defaultY = 0
defaultRadius = 50
defaultColor = (255, 255, 255)
defaultMaxSpeed = 100
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
        # Initialize movement
        self.trueSpeed = maxSpeed
        self.angle = math.radians(45)  # Start at 45 degrees
        self.updateSpeedComponents()
        #VARIABLES
        self.x = x
        self.y = y
        self.trueSpeed = trueSpeed
        self.angle = angle
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.deccel = deccel
        self.hasResetPos = False
        self.screenW = self.screen.get_width()
        self.screenH = self.screen.get_height()

    def setAngle(self, angle):
        self.angle = angle
        self.updateSpeedComponents()
    
    def setTrueSpeed(self, trueSpeed):
        self.trueSpeed = trueSpeed
        self.updateSpeedComponents()

    def printSelf(self):
        print(f"Ball Name: {self.name}")
        print(f"    Diameter(d):            {self.radius}")
        print(f"    Position(x, y):         ({self.x}, {self.y})")
        print(f"    Color(r, g, b):         {self.color}")
        print(f"    maxSpeed(px/s)          {self.maxSpeed}")
        print(f"    Decceleration(px/s^2):  {self.deccel}")
    
    def update(self, deltaTime, paddles):
        self.DeccelTrueSpeed(deltaTime)
        self.move(deltaTime)
        self.checkCollisions(paddles)
        self.draw()

    def DeccelTrueSpeed(self, deltaTime):
        self.trueSpeed += self.deccel * deltaTime

    def updateSpeedComponents(self):
        self.xSpeed = math.cos(self.angle) * self.trueSpeed
        self.ySpeed = math.sin(self.angle) * self.trueSpeed

    def move(self, deltaTime):
        self.x += self.xSpeed * deltaTime
        self.y += self.ySpeed * deltaTime

    def draw(self):
        int_radius = int(self.radius)
        pygame.gfxdraw.aacircle(self.screen, int(self.x), int(self.y), int_radius, self.color)
        pygame.gfxdraw.filled_circle(self.screen, int(self.x), int(self.y), int_radius, self.color)

    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def setResetCurrentPos(self):
        self.setResetPos(self.x, self.y)

    def setResetPos(self, x, y):
        self.resetX = x
        self.resetY = y
        self.hasResetPos = True

    def resetPosition(self):
        if not self.hasResetPos:
            print(f"Ball: {self.name} has no reset position.")
        else:
            self.setPos(self.resetX, self.resetY)

    def resetToPos(self, x, y):
        self.setResetPos(x, y)
        self.resetPosition()

    def centerH(self):
        self.x = self.screenInfo.current_w / 2

    def centerV(self):
        self.y = self.screenInfo.current_h / 2

    def centerCenter(self):
        self.centerH()
        self.centerV()

    def checkCollisions(self, paddles):
        # Collide with top and bottom edges
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screenH:
            self.ySpeed *= -1

        # Collide with paddles
        for paddle in paddles:
            if self.collides_with_paddle(paddle):
                self.xSpeed *= -1
                self.trueSpeed += 50  # Increase speed on paddle collision
                self.updateSpeedComponents()
                break

    def collides_with_paddle(self, paddle):
        return (
            self.x - self.radius < paddle.x + paddle.w and
            self.x + self.radius > paddle.x and
            self.y - self.radius < paddle.y + paddle.h and
            self.y + self.radius > paddle.y
        )