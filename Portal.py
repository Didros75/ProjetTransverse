import pygame
import math
import equation_trajectory

class portal():
    def __init__(self, x=0, y=0):
        a=0
        self.images = [pygame.transform.scale(pygame.image.load(f"assets/portal_{i}.png"), (90, 120)) for i in range(1, 6)]
        self.image = self.images[0]
        self.frame=0
        self.animation_speed=0.1
        self.pos_x=x
        self.pos_y=y
        self.state=1
        self.rect = pygame.Rect(self.pos_x + 38, self.pos_y + 20, 15, 80)


    def animate(self):

        self.image = self.images[int(self.frame)]
        self.frame+=self.animation_speed
        if self.frame >= len(self.images)-1:
            self.frame=0

        if self.state == 1 or self.state == -1:
            if self.state == 1:
                self.image = pygame.transform.rotate(self.image, 0)
            else:
                self.image = pygame.transform.rotate(self.image, 180)
            self.rect = pygame.Rect(self.pos_x + 38, self.pos_y + 20, 15, 90)
        else:
            if self.state == 2:
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.state == -2:
                self.image = pygame.transform.rotate(self.image, 90)
            self.rect = pygame.Rect(self.pos_x + 20, self.pos_y + 38, 90, 15)
