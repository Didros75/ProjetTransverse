import pygame
import Map

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

    def gestion(self, player_speedx, player_speedy, player_y, portal2_pos, portal1_state, portal2_state):
        if portal2_state == -2:
            if portal1_state == -2:
                return (portal2_pos[0], portal2_pos[1]), player_speedx, -(player_speedy - 1), portal2_pos[1] - 20
            else:
                return (portal2_pos[0], portal2_pos[1]), player_speedx, player_speedy , portal2_pos[1]+ 10
        elif portal2_state == 2:
            return (portal2_pos[0], portal2_pos[1]), player_speedx, player_speedy, player_y + 10
        elif portal2_state == 1:
            return (portal2_pos[0]+10, portal2_pos[1]-10), player_speedx+4, player_speedy, player_y
        elif portal2_state == -1:
            return (portal2_pos[0]-80, portal2_pos[1]-10), -player_speedx, player_speedy, player_y

    def change_position(self, tile_touched, tiles, position, state) :
        for i in range(len(tiles)) :
            if state == -1 and tiles[i].rectangle.right == tile_touched.rectangle.left :
                if tiles[i].rectangle.bottom == tile_touched.rectangle.top :
                    if tiles[i].image == Map.img17 :
                        return position[0], tile_touched.rectangle.top
                elif tiles[i].rectangle.top == tile_touched.rectangle.bottom :
                    if tiles[i].image == Map.img1 :
                        return position[0], tile_touched.rectangle.top
            if state == 1 and tiles[i].rectangle.left == tile_touched.rectangle.right :
                if tiles[i].rectangle.bottom == tile_touched.rectangle.top:
                    if tiles[i].image == Map.img17:
                        return position[0], tile_touched.rectangle.top
                elif tiles[i].rectangle.top == tile_touched.rectangle.bottom:
                    if tiles[i].image == Map.img1:
                        return position[0], tile_touched.rectangle.top
        return position