import pygame
import math
import equation_trajectory

class portal():
    def __init__(self):
        a=0
        self.images = [pygame.transform.scale(pygame.image.load(f"assets/portal_{i}.png"), (80, 100)) for i in range(1, 6)]
        self.image = self.images[0]
        self.frame=0
        self.animation_speed=0.1
        self.pos_x=0
        self.pos_y=0
        self.state=1
        self.rect = pygame.Rect(self.pos_x + 32, self.pos_y + 10, 15, 80)


    def animate(self):

        self.image = self.images[int(self.frame)]
        self.frame+=self.animation_speed
        if self.frame >= len(self.images)-1:
            self.frame=0

        if self.state == 1 or self.state == 3:
            self.image = pygame.transform.rotate(self.image, 0)
            self.rect = pygame.Rect(self.pos_x + 32, self.pos_y + 10, 15, 80)
        else:
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = pygame.Rect(self.pos_x + 10, self.pos_y + 32, 80, 15)
