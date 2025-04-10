    # Gère le placement des portails et la téléportation

import pygame
import Map
import time

class Portal() :
    def __init__(self, x=0, y=0, num=1):
        self.num=num
        if self.num==1:
            self.images = [pygame.transform.scale(pygame.image.load(f"assets/portal_{i}.png"), (90, 120)) for i in range(1, 6)]
        else:
            self.images = [pygame.transform.scale(pygame.image.load(f"assets/portal{i}b.png"), (90, 120)) for i in range(1, 6)]
        self.image = self.images[0]
        self.frame=0
        self.animation_speed=0.1
        self.pos_x=x
        self.pos_y=y
        self.state=1
        self.width=5
        self.length=70
        self.rect = pygame.Rect(self.pos_x + 48, self.pos_y + 20, self.width, self.length)

    def animate(self):

        self.image = self.images[int(self.frame)]
        self.frame+=self.animation_speed
        if self.frame >= len(self.images)-1:
            self.frame=0

        if self.state == 1 or self.state == -1:
            if self.state == 1:
                self.image = pygame.transform.rotate(self.image, 0)
                self.rect = pygame.Rect(self.pos_x +47, self.pos_y+28, self.width, self.length)

            else:
                self.image = pygame.transform.rotate(self.image, 180)
                self.rect = pygame.Rect(self.pos_x +37, self.pos_y+15, self.width, self.length)
        else:
            if self.state == 2:
                self.image = pygame.transform.rotate(self.image, -90)
                self.rect = pygame.Rect(self.pos_x+20, self.pos_y +42, self.length, self.width)

            elif self.state == -2:
                self.image = pygame.transform.rotate(self.image, 90)
                self.rect = pygame.Rect(self.pos_x+35, self.pos_y +37, self.length, self.width)


    def change_position(self, tile_touched, tiles, position, state) :
        for i in range(30, len(tiles) - 60) :
            if tiles[i] == tile_touched :
                if (state == 1 and tiles[i+31].image != Map.sky) or (state == -1 and tiles[i+29].image != Map.sky) :
                    return position[0], position[1] - 35
                elif (state == 1 and tiles[i-29].image != Map.sky) or (state == -1 and tiles[i-31].image != Map.sky) :
                    return position[0], position[1] + 15
                elif (state == 1 and tiles[i+61].image != Map.sky) or (state == -1 and tiles[i+59].image != Map.sky) :
                    return position[0], position[1] - 10

                if (state == -2 and tiles[i-29].image != Map.sky) or (state == 2 and tiles[i+31].image != Map.sky) :
                    return position[0] - 45, position[1]
                elif (state == -2 and tiles[i-28].image != Map.sky) or (state == 2 and tiles[i+32].image != Map.sky) :
                    return position[0] - 10, position[1]
                elif (state == -2 and tiles[i-31].image != Map.sky) or (state == 2 and tiles[i+29].image != Map.sky) :
                    return position[0] + 10, position[1]
        return position

    def not_teleportable(self, tiles, tile_touched) :
        for i in range(60, len(tiles)-60) :
            if tiles[i] == tile_touched :
                if tiles[i-60].image != Map.sky and self.state == -2:
                    return False
                if tiles[i+60].image != Map.sky and self.state == 2:
                    return False
        return True

    def delete_portal(self, second_portal) :
        self.pos_x = -75
        self.pos_y = -75
        second_portal.pos_x = -75
        second_portal.pos_y = -75