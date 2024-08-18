import pygame
from ball import Ball
from paddle import Paddle

def main():
    pygame.init()
    screen = pygame.display.set_mode((2560, 1600))
    pygame.display.toggle.fullscreen()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        
        pygame.display.flip()

        clock.tick(240)
if __name__ == "__main__":
    main()
