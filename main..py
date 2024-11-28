import pygame
from paddle import Paddle
from ball import Ball
import pygame.gfxdraw  # Import gfxdraw for anti-aliased drawing
import random
import time
import math  # Import the math module

def main():

    def resetAll(*args):
        for i in args:
            i.resetPosition()
        screen.fill(displayBGColor)  # Clear the screen before launching the ball
        pygame.display.flip()
        time.sleep(2)  # Wait for 2 seconds before launching the ball
        launchBall(ball)

    def updateAll(deltaTime, paddles, *args):
        for i in args:
            if isinstance(i, Ball):
                i.update(deltaTime, paddles)
            else:
                i.update(deltaTime)
        pygame.display.flip()

    def launchBall(ball):
        angle = random.uniform(0, 2 * math.pi)
        ball.setAngle(angle)
        ball.setTrueSpeed(300)  # Set a higher initial speed for the ball

    pygame.init()

    displayNativeResolution = (2560, 1600)
    displayBGColor = (20, 20, 20)

    screen = pygame.display.set_mode(displayNativeResolution, flags=pygame.FULLSCREEN | pygame.SRCALPHA)
    displayInfo = pygame.display.Info()
    clock = pygame.time.Clock()
    displayIsInitiated = False

    # Universal Variables

    paddleHeight = displayInfo.current_h / 7
    paddleWidth = paddleHeight / 5
    ballRadius = paddleHeight / 4

    leftPaddle = Paddle(screen, name="Left Paddle", w=paddleWidth, h=paddleHeight)
    rightPaddle = Paddle(screen, name="Right Paddle", w=paddleWidth, h=paddleHeight)
    ball = Ball(screen, name="Ball", radius=ballRadius)

    # Paddle Positioning and Reset Position

    leftPaddle.alignLC()
    rightPaddle.alignRC()
    ball.centerCenter()

    leftPaddle.setResetCurrentPosition()
    rightPaddle.setResetCurrentPosition()
    ball.setResetCurrentPos()

    leftPaddle.printSelf()
    rightPaddle.printSelf()

    leftPaddle.setStartStopTime(0.2)
    rightPaddle.setStartStopTime(0.2)

    leftPaddle.yBeginAimingSpeed()
    rightPaddle.yBeginAimingSpeed()

    # Initialize scores
    leftScore = 0
    rightScore = 0

    running = True
    print("Game Status: Initiated")
    resetAll(leftPaddle, rightPaddle, ball)  # Initial reset and launch
    while running:

        # Check Window Status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Game Status: Aborted")

        # Check Window Initation
        isInitiated = pygame.display.get_init()
        if isInitiated != displayIsInitiated:
            displayIsInitiated = isInitiated
            print(f"Window Status: {'Successful' if pygame.display.get_init() else 'Failed'}")

        deltaTime = clock.tick(240) / 1000
        screen.fill(displayBGColor)

        # Loop

        # Key Pressing
        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_w] and not pressedKeys[pygame.K_s]:
            leftPaddle.ySetTargetSpeed(-leftPaddle.maxSpeed)
        elif pressedKeys[pygame.K_s] and not pressedKeys[pygame.K_w]:
            leftPaddle.ySetTargetSpeed(leftPaddle.maxSpeed)
        else:
            leftPaddle.ySetTargetSpeed(0)

        if pressedKeys[pygame.K_UP] and not pressedKeys[pygame.K_DOWN]:
            rightPaddle.ySetTargetSpeed(-rightPaddle.maxSpeed)
        elif pressedKeys[pygame.K_DOWN] and not pressedKeys[pygame.K_UP]:
            rightPaddle.ySetTargetSpeed(rightPaddle.maxSpeed)
        else:
            rightPaddle.ySetTargetSpeed(0)

        # Handle scoring and reset
        if ball.x - ball.radius <= 0:
            # Right player scores
            rightScore += 1
            print(f"Score: Left {leftScore} - Right {rightScore}")
            resetAll(leftPaddle, rightPaddle, ball)
        elif ball.x + ball.radius >= displayInfo.current_w:
            # Left player scores
            leftScore += 1
            print(f"Score: Left {leftScore} - Right {rightScore}")
            resetAll(leftPaddle, rightPaddle, ball)

        # Update all game objects
        updateAll(deltaTime, [leftPaddle, rightPaddle], leftPaddle, rightPaddle, ball)

if __name__ == "__main__":
    main()