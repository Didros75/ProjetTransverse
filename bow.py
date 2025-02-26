import pygame
import math
import equation_trajectoire

class Bow():
    def __init__(self):
        self.images = [
            pygame.transform.scale(
                pygame.image.load(f"assets/l0_arc{i}.png"),
                (pygame.image.load(f"assets/l0_arc{i}.png").get_width() // 3,
                 pygame.image.load(f"assets/l0_arc{i}.png").get_height() // 3)
            )
            for i in range(1, 5)
        ]

        self.arrow_image=pygame.transform.scale(pygame.image.load("assets/Arrow.png"), (pygame.image.load("assets/Arrow.png").get_width()*3,pygame.image.load("assets/Arrow.png").get_height()*3))
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect()

        self.portal_blue = True
        self.portal_green = True
        self.arrow = True
        self.aiming = False
        self.gravity = 9.8
        self.animation_timer = 0
        self.animation_speed = 10

    def animation(self, dt, angle):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]

            self.image = pygame.transform.rotate(self.image, angle * (180 / math.pi))



    def shot(self, dt, v0, tetha, x, y):
        return equation_trajectoire.trajectory(v0, tetha, dt, self.gravity, x, y)

class Portals():
    def __init__(self, portal_rect, color, screen):
        self.portal_rect = portal_rect
        self.color = color
        self.screen = screen
        self.state = False

    def apparition(self, x, y):
        self.state = True
        pygame.draw.rect(self.screen, self.color, (x, y, self.portal_rect[2], self.portal_rect[3]))
