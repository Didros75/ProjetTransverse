import pygame
import math
import equation_trajectory
import Map

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

        #self.arrow_image=pygame.transform.scale(pygame.image.load("assets/Arrow.png"), (pygame.image.load("assets/Arrow.png").get_width()*3,pygame.image.load("assets/Arrow.png").get_height()*3))
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        #self.rect = self.image.get_rect()

        #self.portal_blue = True
        #self.portal_green = True
        #self.arrow = True
        self.aiming = False
        self.gravity = 9.8
        self.animation_timer = 0
        self.animation_speed = 10
        self.rect_x, self.rect_y, self.rect_size = 0, 0, 0
        self.state=1

    def animation(self, dt, angle):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]
            self.image = pygame.transform.rotate(self.image, angle * (180 / math.pi))

    def shot(self, dt, v0, theta, x, y):
        return equation_trajectory.trajectory(v0, theta, dt, self.gravity, x, y)

    def draw_rectangle(self, screen, t, rect_x, rect_y):
        self.rect_size = min(t*9, 143)
        color = (0, 0, 0)
        pygame.draw.rect(screen, color, (rect_x, rect_y, self.rect_size, 20))


class Arrow() :
    def __init__(self, position) :
        self.gravity = 9.8
        self.position_x = position[0]
        self.position_y = position[1]
        self.image = pygame.transform.scale(pygame.image.load("assets/Arrow.png"), (pygame.image.load("assets/Arrow.png").get_width() * 3, pygame.image.load("assets/Arrow.png").get_height() * 3))
        self.rect = pygame.Rect(position[0], position[1], 20, 20)

    def shot(self, dt, v0, theta, x, y):
        coordinate = equation_trajectory.trajectory(v0, theta, dt, self.gravity, x, y)
        self.image=pygame.transform.rotate(self.image, equation_trajectory.angle_arrow(v0, theta, dt, self.gravity*10)*180/math.pi)
        self.position_x = coordinate[0]
        self.position_y = -coordinate[1]
        self.rect.left = coordinate[0]
        self.rect.top = -coordinate[1]

    def collision(self, tiles) :
        hit_something = []
        for tile in tiles :
            if self.rect.colliderect(tile.rectangle) and tile.image != Map.sky :
                hit_something.append(tile)
        if hit_something == [] :
            return True
        return False


    # COLLISIONS EN DEHORS DU CADRE

    def show(self, screen) :
        screen.blit(self.image, (self.position_x, self.position_y))

class Portals():
    def __init__(self, portal_rect, color, screen):
        self.portal_rect = portal_rect
        self.color = color
        self.screen = screen
        self.state = False

    def apparition(self, x, y):
        self.state = True
        pygame.draw.rect(self.screen, self.color, (x, y, self.portal_rect[2], self.portal_rect[3]))