    # Gère le placement des portails et la téléportation

import pygame
import Map

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
        for i in range(1, len(tiles) - 1) :

            if state == -1 and tiles[i].rectangle.right == tile_touched.rectangle.left :
                if tiles[i].rectangle.bottom == tile_touched.rectangle.top :
                    if tiles[i].image == Map.img17 or tiles[i].image == Map.img9 or (tiles[i].image == Map.sky and tiles[i+1].image == Map.sky) :
                        return (position[0], tile_touched.rectangle.top - 10), 0
                elif tiles[i].rectangle.top == tile_touched.rectangle.bottom :
                    if tiles[i].image == Map.img1 or tiles[i].image == Map.img9 or (tiles[i].image == Map.sky and tiles[i + 1].image == Map.sky) :
                        return (position[0], tile_touched.rectangle.bottom), 0

            elif state == 1 and tiles[i].rectangle.left == tile_touched.rectangle.right :
                if tiles[i].rectangle.bottom == tile_touched.rectangle.top :
                    if tiles[i].image == Map.img17 or tiles[i].image == Map.img9 or tiles[i-1].image == Map.sky :
                        return (position[0], tile_touched.rectangle.top - 15), 0
                elif tiles[i].rectangle.top == tile_touched.rectangle.bottom :
                    if tiles[i].image == Map.img1 or tiles[i].image == Map.img9 or tiles[i-1].image == Map.sky :
                        return (position[0], tile_touched.rectangle.bottom), 0

            elif state == -2 or state == 2:
                if self.rect.colliderect(tiles[i].rectangle)  and (tiles[i].image == Map.img8 or tiles[i].image == Map.img9) :
                    return (position[0] - 5, position[1]), 1
                else :
                    return position, 0

        return position, 0

    def not_teleportable(self, tiles, tile_touched) :
        for i in range(60, len(tiles)-60) :
            if tiles[i] == tile_touched :
                if tiles[i-60].image != Map.sky and self.state == -2:
                    return False
                if tiles[i+60].image != Map.sky and self.state == 2:
                    return False
        return True