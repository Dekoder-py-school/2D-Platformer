import pygame
import sys

pygame.init()  # setup pygame

pygame.display.set_caption("2D Platformer")  # set window name
screen = pygame.display.set_mode((640, 480))  # create window
clock = pygame.time.Clock()  # clock for frame rate

while True:  # runs until quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # exit pygame
            sys.exit()  # end program

    screen.fill("#89b4fa")

    pygame.display.update()
    clock.tick(60)