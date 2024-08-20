import pygame 
from paddle import Paddle
from ball import Ball

def main():

    def quitGame():
        if running:
            running = False
            print("Window Status: Aborted")

    def resetAll():
        leftPaddle.resetPos()
        rightPaddle.resetPos()

    def updateAll(*args):
        for i in args:
            i.update()
        pygame.display.flip()  

    pygame.init()

    displayNativeResolution = (2560, 1600)
    displayBGColor = (20, 20, 20)

    screen = pygame.display.set_mode(displayNativeResolution, flags=pygame.FULLSCREEN)
    displayInfo = pygame.display.Info()
    clock = pygame.time.Clock()
    running = True
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


    while running:

        #Check Window Status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running  = False
                print("Game Status: Aborted")

        #Check Window Initation
        isInitiated = pygame.display.get_init()
        if isInitiated != displayIsInitiated:
            displayIsInitiated = isInitiated
            print(f"Window Status: {'Successful' if pygame.display.get_init() else 'Failed'}")
        #Loop
        screen.fill(displayBGColor)

        updateAll(leftPaddle, rightPaddle, ball)  
        
        clock.tick(240)
    
            
if __name__ == "__main__":
    main()