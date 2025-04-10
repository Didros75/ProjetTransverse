    # Gère les actions liées à l'arc et aux flèches tirées

import pygame
import math
import equation_trajectory
import Map
from sound_manager import SoundManager

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

    def draw_rectangle(self, screen, t, rect_x, rect_y, nb):
        self.rect_size = min(t*6, 95)
        if nb==-1:
            color = (126, 34, 80)
        else:
            color = (68, 107, 166)
        pygame.draw.rect(screen, color, (rect_x, rect_y, self.rect_size, 28))

class Arrow() :
    def __init__(self, position) :
        self.gravity = 9.8
        self.position_x = position[0]
        self.position_y = position[1]
        self.image = pygame.transform.scale(pygame.image.load("assets/Arrow.png"), (pygame.image.load("assets/Arrow.png").get_width() * 3, pygame.image.load("assets/Arrow.png").get_height() * 3))
        self.rect = pygame.Rect(position[0], position[1], 10, 10)
        self.portal_state = 0
        self.sono = SoundManager(False)

    def shot(self, dt, v0, theta, x, y):
        coordinate = equation_trajectory.trajectory(v0, theta, dt, self.gravity, x, y)
        self.image=pygame.transform.rotate(self.image, equation_trajectory.angle_arrow(v0, theta, dt, self.gravity*10)*180/math.pi)
        self.position_x = coordinate[0]
        self.position_y = -coordinate[1]
        self.rect.left = coordinate[0]
        self.rect.top = -coordinate[1]

    def collision(self, tiles, height, width) :
        for tile in tiles :
            if self.rect.colliderect(tile.rectangle) and tile.image != Map.sky :
                if tile.image==Map.img48 or tile.image == Map.img9 :
                    return False, 0
                elif tile.image==Map.img49 or tile.image==Map.img50 or tile.image==Map.img51 or tile.image==Map.img52 :
                    self.sono.play_button_sound()
                    return False, 1
                return False, tile
        if self.position_y > height or self.position_x > width or self.position_x < 0 or self.position_y < 0 :
            return False, 0
        return True, 0

    def show(self, screen) :
        screen.blit(self.image, (self.position_x, self.position_y))

    def position_portal(self, tile) :
        if tile.image == Map.img1 :
            self.portal_state = -2
            return tile.rectangle.left - 30, tile.rectangle.top - 50
        elif tile.image == Map.img10 :
            self.portal_state = 1
            return tile.rectangle.left - 15, tile.rectangle.top - 30
        elif tile.image == Map.img17 :
            self.portal_state = 2
            return tile.rectangle.left - 30, tile.rectangle.top - 5
        elif tile.image == Map.img8 :
            self.portal_state = -1
            return tile.rectangle.left - 48, tile.rectangle.top - 30

        elif tile.image == Map.img0 :
            if self.rect.bottom - 15 <= tile.rectangle.top :
                self.portal_state = -2
                return tile.rectangle.left - 30, tile.rectangle.top - 50
            else :
                self.portal_state = -1
                return tile.rectangle.left - 48, tile.rectangle.top - 30
        elif tile.image == Map.img2 :
            if self.rect.bottom - 13 <= tile.rectangle.top :
                self.portal_state = -2
                return tile.rectangle.left - 30, tile.rectangle.top - 50
            else :
                self.portal_state = 1
                return tile.rectangle.left - 15, tile.rectangle.top - 30
        elif tile.image == Map.img16 :
            if self.rect.top <= tile.rectangle.bottom :
                self.portal_state = 2
                return tile.rectangle.left - 30, tile.rectangle.top - 5
            else :
                self.portal_state = -1
                return tile.rectangle.left - 48, tile.rectangle.top - 30
        else :
            if self.rect.top - 5 <= tile.rectangle.bottom :
                self.portal_state = 2
                return tile.rectangle.left - 30, tile.rectangle.top - 5
            else :
                self.portal_state = 1
                return tile.rectangle.left - 48, tile.rectangle.top - 30