import sys

import pygame


class Game:
    def __init__(self):
        pygame.init()  # setup pygame

        pygame.display.set_caption("2D Platformer")  # set window name
        self.screen = pygame.display.set_mode((640, 480))  # create window
        self.clock = pygame.time.Clock()  # clock for frame rate
        self.sprite = pygame.image.load("./assets/sprite.png")

        self.sprite_pos = [160, 260]
        self.y_movement = [False, False]
        self.x_movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:  # runs until quit
            self.screen.fill("#89b4fa")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # exit pygame
                    sys.exit()  # end program
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.y_movement[0] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.y_movement[1] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.x_movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.x_movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.y_movement[0] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.y_movement[1] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.x_movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.x_movement[1] = False

            self.sprite_pos[1] += (self.y_movement[1] - self.y_movement[0]) * 5
            self.sprite_pos[0] += (self.x_movement[1] - self.x_movement[0]) * 5
            self.screen.blit(self.sprite, self.sprite_pos)

            sprite_r = pygame.Rect(*self.sprite_pos, *self.sprite.get_size())
            if sprite_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, "#f38ba8", self.collision_area)
            else:
                pygame.draw.rect(self.screen, "#a6e3a1", self.collision_area)

            pygame.display.update()
            self.clock.tick(60)


Game().run()
