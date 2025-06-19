import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()  # setup pygame

        pygame.display.set_caption("2D Platformer")  # set window name
        self.screen = pygame.display.set_mode((640, 480))  # create window
        self.clock = pygame.time.Clock()  # clock for frame rate
        self.img = pygame.image.load("./assets/sprite.png")

    def run(self):
        while True:  # runs until quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # exit pygame
                    sys.exit()  # end program

            self.screen.fill("#89b4fa")

            pygame.display.update()
            self.clock.tick(60)

Game().run()