import pygame
from sys import exit

class game (): 
    def gameLoop():
        # starts engine and game size
        pygame.init()
        width = 800
        height = 800

        # actual game loop
        while True:
            # checks if player closes tab
            for event in pygame.event.get():
                screen = pygame.display.set_mode((width, height))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # renders changes
            pygame.display.update()


game.gameLoop()