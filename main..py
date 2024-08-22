import pygame 
from paddle import Paddle
from ball import Ball

def main():

    def resetAll(*args):
        for i in args:
            i.reseetPos()

    def updateAll(*args):
        for i in args:
            i.update(deltaTime)
        pygame.display.flip()  

    pygame.init()

    displayNativeResolution = (2560, 1600)
    displayBGColor = (20, 20, 20)

    screen = pygame.display.set_mode(displayNativeResolution, flags=pygame.FULLSCREEN)
    displayInfo = pygame.display.Info()
    clock = pygame.time.Clock()
    displayIsInitiated = False

    #Universal Variables

    paddleHeight = displayInfo.current_h / 7
    paddleWidth = paddleHeight / 5

    leftPaddle = Paddle(screen, name = "Left Paddle", w = paddleWidth, h = paddleHeight)
    rightPaddle = Paddle(screen, name = "Right Paddle", w = paddleWidth, h = paddleHeight)
    ball = Ball(screen, name = "Ball", radius = paddleHeight / 4)

    leftPaddle.alignLC()
    rightPaddle.alignRC()
    ball.centerCenter()

    leftPaddle.setResetCurrentPos()
    rightPaddle.setResetCurrentPos()

    leftPaddle.printSelf()
    rightPaddle.printSelf()
    leftPaddle.setStartStopTimee(0.2)
    rightPaddle.setStartStopTimee(0.2)

    leftPaddle.beginTargetingY()
    rightPaddle.beginTargetingY()

    running = True
    print("Game Status: Initiated")
    while running:

        #Check Window Status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Game Status: Aborted")

        #Check Window Initation
        isInitiated = pygame.display.get_init()
        if isInitiated != displayIsInitiated:
            displayIsInitiated = isInitiated
            print(f"Window Status: {'Successful' if pygame.display.get_init() else 'Failed'}")

        deltaTime = clock.tick(240) / 1000.0
        screen.fill(displayBGColor)

        #Loop

        #Key Pressing
        
        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_w] and not pressedKeys[pygame.K_s]:
            leftPaddle.setYTargetSpeed(-leftPaddle.maxSpeed)
        elif pressedKeys[pygame.K_s] and not pressedKeys[pygame.K_w]:
            leftPaddle.setYTargetSpeed(leftPaddle.maxSpeed)
        elif pressedKeys[pygame.K_w] == pressedKeys[pygame.K_s]:
            leftPaddle.setYTargetSpeed(0)

        if pressedKeys[pygame.K_UP] and not pressedKeys[pygame.K_DOWN]:
            rightPaddle.setYTargetSpeed(-rightPaddle.maxSpeed)
        elif pressedKeys[pygame.K_DOWN] and not pressedKeys[pygame.K_UP]:
            rightPaddle.setYTargetSpeed(rightPaddle.maxSpeed)
        elif pressedKeys[pygame.K_UP] == pressedKeys[pygame.K_DOWN]:
            rightPaddle.setYTargetSpeed(0)

        updateAll(leftPaddle, rightPaddle, ball)
        
if __name__ == "__main__":
    main()