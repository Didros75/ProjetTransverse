import math
import pygame
from pygame.examples.cursors import image
import Map

class ThePlayer(pygame.sprite.Sprite) :
    def __init__(self, position_x, position_y, gravity = 0.6, LEFT = False, RIGHT = False, SPACE = False) :
        pygame.sprite.Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = gravity
        self.position_x = position_x
        self.position_y = position_y
        self.acceleration_x=0
        self.acceleration_y=self.gravity
        self.friction=-0.2
        self.isgrounded, self.isjumping = False, False
        self.state = 0
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        self.SPACE = SPACE
        self.facingLeft = False
        self.aiming=False

        self.sprites_right = [pygame.image.load(f"assets\l0_Running{i}.png") for i in range(1, 5)]
        self.sprites_left = [pygame.transform.flip(img, True, False) for img in self.sprites_right]
        self.sprites_right_aiming = [pygame.image.load(f"assets\l0_aiming_anime{i}.png") for i in range(1, 5)]
        self.sprites_left_aiming = [pygame.transform.flip(img, True, False) for img in self.sprites_right_aiming]
        self.sprites_idle = [pygame.image.load(f"assets\l0_sprite_{i}.png") for i in range(1, 5)]
        self.sprite_index = 0
        self.image = self.sprites_right[0]
        self.animation_speed = 0.2
        self.frame_count = 0
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = pygame.Rect(position_x, position_y, self.image.get_height(), self.image.get_width())

    def animate(self, angle=0):

        if self.LEFT or self.RIGHT:
            self.frame_count += self.animation_speed
            if self.frame_count >= len(self.sprites_right):
                self.frame_count = 0
            self.sprite_index = int(self.frame_count)

            if self.RIGHT:
                self.image = self.sprites_right[self.sprite_index]
                self.facingLeft = False
            elif self.LEFT:
                self.image = self.sprites_left[self.sprite_index]
                self.facingLeft = True

        elif self.speed_x<=0.5:

            self.sprite_index += 0.2
            if self.sprite_index >= len(self.sprites_idle):
                self.sprite_index = 0
            self.image = self.sprites_idle[int(self.sprite_index)]

        else:
            self.frame_count = 0
            self.image = self.sprites_left[0] if self.facingLeft else self.sprites_right[0]

        if self.aiming:
            self.frame_count += self.animation_speed
            if -math.pi/2 <= angle <= math.pi/2:
                self.image = self.sprites_right_aiming[int(self.sprite_index)]
            else:
                self.image = self.sprites_left_aiming[int(self.sprite_index)]

    def get_position(self) :
        return (self.position_x, self.position_y)

    def jump(self) :
        if self.isgrounded :
            self.isjumping = True
            self.speed_y=14
            self.isgrounded = False

    def pos(self) :
        return self.position_x, self.position_y

    def death(self) :
        pass

    def draw(self, ref):
        self.image = pygame.transform.scale(self.image, (40, 50))
        ref.blit(self.image, (self.position_x, self.position_y))

    def move_x(self, dt) :
        self.acceleration_x = 0
        if self.LEFT:
            self.acceleration_x -=5
        if self.RIGHT:
            self.acceleration_x +=5
        self.acceleration_x += self.speed_x * self.friction
        self.speed_x+=self.acceleration_x * dt
        self.max_speed(8)
        self.position_x += (0.5 * self.acceleration_x) * (dt*dt) + self.speed_x * dt
        self.rect.x = self.position_x




    def max_speed(self, maxi) :
        min(-maxi, max(self.speed_x, maxi))
        if abs(self.speed_x) > maxi :
            self.speed_x = 0



    def move_y(self, dt) :

        self.speed_y -= self.gravity * dt
        if self.speed_y<=-30:
            self.speed_y = -30
        self.position_y -= (0.5*self.acceleration_y) * (dt*dt) + self.speed_y * dt
        self.rect.y = self.position_y

    """def collisions(self, wall):
        self.isgrounded = True
        self.speed_y=0
        self.acceleration_y=0
        for wall_rect in wall:
            self.rect.bottom=wall_rect.top
            self.position_y=self.rect.y"""

    def hit_something(self, tiles) :
        tiles_hits = []
        for tile in tiles :
            if self.rect.colliderect(tile.rectangle) and tile.image != Map.ciel :
                tiles_hits.append(tile)
        return tiles_hits

    def hit_y(self, tiles) :
        collisions = self.hit_something(tiles)
        for tile in collisions :
            if self.speed_y < 0 :
                self.isgrounded = True
                self.speed_y = 0
                #self.position_y = tile.pos_y
                self.acceleration_y = 0
                self.position_y = tile.rectangle.top - 37
                #self.rect.bottom = self.position_y
            elif self.speed_y > 0 :
                self.speed_y = 0
                self.acceleration_y = 0
                self.position_y = tile.rectangle.bottom
                #self.rect.bottom = self.position_y