import pygame
from sys import exit

class game (): 
    def gameLoop():
        # starts engine and game size
        pygame.init()
        width = 800
        height = 800
        pygame.display.set_caption("idk lol")
        clock = pygame.time.Clock()

        mainScreen = pygame.Surface((width, height-50))
        mainScreen.fill("Blue")
        # actual game loop
        while True:
            # checks if player closes tab
            for event in pygame.event.get():
                screen = pygame.display.set_mode((width, height))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            screen.blit(mainScreen, (0, 50))
            # renders changes
            pygame.display.update()
            # max fps
            clock.tick(60)
    

game.gameLoop() 