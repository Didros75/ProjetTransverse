import pygame

import equation_trajectoire
from equation_trajectoire import *
class Bow():
    def __init__(self):
        self.images = [
            pygame.image.load("assets/l0_arc1.png"),
            pygame.image.load("assets/l0_arc2.png"),
            pygame.image.load("assets/l0_arc3.png"),
            pygame.image.load("assets/l0_arc4.png"),
        ]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.portal_blue=True
        self.portal_green=True
        self.arrow=True
        self.aiming=False
        self.gravity=9.8
        self.animation_timer = 0
        self.animation_speed = 20

    def animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]

    def shot(self, dt, v0, tetha, x, y):
        return equation_trajectoire.trajectory(v0, tetha, dt, self.gravity, x, y)

class Portals():
    def __init__(self, portal_rect, color, screen):
        self.portal_rect = portal_rect
        self.color = color
        self.screen = screen
        self.state=False


    def apparition(self, x, y):
        self.state=True
        pygame.draw.rect(self.screen, self.color, (x, y, self.portal_rect[2], self.portal_rect[3]))





