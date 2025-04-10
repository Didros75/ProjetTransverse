    # Module contenant la classe qui gère les intéractions du joueur

import math
import pygame
import Map

class ThePlayer(pygame.sprite.Sprite) :
    def __init__(self, position_x, position_y,skin, gravity = 0.6, LEFT = False, RIGHT = False, SPACE = False) :
        pygame.sprite.Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = gravity
        self.position_x = position_x
        self.position_y = position_y
        self.acceleration_x=0
        self.acceleration_y=self.gravity
        self.friction=-0.2
        self.isgrounded = False
        self.state = 0
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        self.SPACE = SPACE
        self.facingLeft = False
        self.aiming=False

        self.sprites_right = [pygame.image.load(f"assets/{skin}/l0_Running{i}.png") for i in range(1, 5)]
        self.sprites_left = [pygame.transform.flip(img, True, False) for img in self.sprites_right]
        self.sprites_right_aiming = [pygame.image.load(f"assets/{skin}/l0_aiming_anime{i}.png") for i in range(1, 5)]
        self.sprites_left_aiming = [pygame.transform.flip(img, True, False) for img in self.sprites_right_aiming]
        self.sprites_idle = [pygame.image.load(f"assets/{skin}/l0_sprite_{i}.png") for i in range(1, 5)]
        self.sprite_index = 0
        self.image = self.sprites_right[0]
        self.animation_speed = 0.15
        self.frame_count = 0
        self.image = self.sprites_right[0]
        self.rect = pygame.Rect(position_x, position_y, 30, 50)
        self.rectx = pygame.Rect(self.position_x-5, self.position_y + 5, 40, 30)
        self.rect_final = pygame.Rect(position_x, position_y, 40, 50)

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
            self.sprite_index += self.animation_speed
            if self.sprite_index >= len(self.sprites_idle):
                self.sprite_index = 0
            self.image = self.sprites_idle[int(self.sprite_index)]

        else:
            self.frame_count = 0  # Reset animation quand il ne bouge pas
            self.image = self.sprites_left[0] if self.facingLeft else self.sprites_right[0]
        if self.aiming:
            self.frame_count += self.animation_speed
            if -math.pi/2 <= angle <= math.pi/2:
                self.image = self.sprites_right_aiming[int(self.sprite_index)]
            else:
                self.image = self.sprites_left_aiming[int(self.sprite_index)]

    def get_position(self) :
        """
        retourne la position du joueurr
        """
        return self.position_x, self.position_y

    def jump(self) :
        if self.isgrounded :
            self.isgrounded = False
            self.speed_y = 10

    def death(self) :
        """
        gère la mort du joueur
        retourne 1 si le joueur est mort, 0 sinon
        """
        if self.position_y > 700 :
            self.state = 1
        return self.state

    def draw(self, ref) :
        self.image = pygame.transform.scale(self.image, (40, 50))
        ref.blit(self.image, (self.position_x, self.position_y))
        #pygame.draw.rect(ref, "white", self.rect_final)

    def move_x(self, dt) :
        self.acceleration_x = 0
        if self.LEFT :
            self.acceleration_x -=5
        if self.RIGHT :
            self.acceleration_x +=5
        self.acceleration_x += self.speed_x * self.friction
        self.speed_x+=self.acceleration_x * dt
        self.max_speed(8)
        self.position_x += (0.5 * self.acceleration_x) * (dt*dt) + self.speed_x * dt
        self.rect_final.x = self.position_x

    def max_speed(self, maxi) :
        min(-maxi, max(self.speed_x, maxi))
        if abs(self.speed_x) > maxi :
            self.speed_x = 0

    def move_y(self, dt) :
        if self.isgrounded == False :
            self.speed_y -= self.gravity * dt
        if self.speed_y <= -20:
            self.speed_y = -20
        self.position_y -= (0.5*self.acceleration_y) * (dt*dt) + self.speed_y * dt
        self.rect_final.y = self.position_y

    """def hit_something(self, tiles, screen) :
        tilesx_hits = []
        tilesy_hits = []
        if 0>self.speed_y>-0.6:
            self.speed_y = 0

        for tile in tiles:
            if self.rect.colliderect(tile.rectangle) and tile.image != Map.sky :
                if self.rect.bottom > tile.rectangle.top > self.rect.top:  # Collision sol
                    tilesy_hits.append(tile)

                elif self.rect.top < tile.rectangle.bottom < self.rect.bottom:  # Collision plafond
                    tilesy_hits.append(tile)

            if self.rectx.colliderect(tile.rectangle) and tile.image != Map.sky :
                if self.rectx.right > tile.rectangle.left >= self.rectx.left:
                    tilesx_hits.append(tile)

                elif self.rectx.left < tile.rectangle.right <= self.rectx.right :
                    tilesx_hits.append(tile)

        self.isgrounded = any(tile.rectangle.top <= self.rect.bottom <= tile.rectangle.bottom for tile in tilesy_hits)
        print("X : ", tilesx_hits)
        print("Y : ", tilesy_hits)
        print()
        pygame.draw.rect(screen, 'black', self.rect)
        pygame.draw.rect(screen, 'white', self.rectx)
        return tilesx_hits, tilesy_hits

    def hit_y(self, collisions) :
        #collisions = self.hit_something(tiles)[1]
        #for tile in collisions :
        if collisions != [] :
            tile = collisions[-1]
            if self.speed_y <= 0 :
                    self.isjumping = False
                    self.acceleration_y = 0
                    self.position_y = tile.rectangle.top - 45
                    self.rect.bottom = self.position_y + 50
                    self.rectx.bottom = self.position_y + 40
                    self.speed_y = 0
            else :
                    self.speed_y = 0
                    self.acceleration_y = 0
                    self.position_y = tile.rectangle.bottom
                    self.rect.top = self.position_y
                    self.rectx.top = self.position_y + 5

    def hit_x(self, collisions) :
        #collisions = self.hit_something(tiles)[0]
        #for tile in collisions :
        if collisions != [] :
                tile = collisions[-1]
                if self.speed_x > 0 :
                    self.speed_x = 0
                    self.position_x = tile.rectangle.left - 35
                    self.rect.right = tile.rectangle.left - 5
                    self.rectx.right = tile.rectangle.left
                else :
                    self.speed_x = 0
                    print("aaa")
                    self.position_x = tile.rectangle.right + 5
                    self.rect.left = self.position_x + 5
                    self.rectx.left = self.position_x"""

    def hit_something(self, tiles, screen) :
        if 0 > self.speed_y > -0.6:
            self.speed_y = 0

        collisions = []
        for tile in tiles :
            if self.rect_final.colliderect(tile.rectangle) and tile.image != Map.sky :
                top = False
                right = False
                bottom = False
                left = False

                collisions.append((tile))

                if tile.image == Map.img0 :
                    if self.isgrounded :
                        if self.rect_final.bottom - 5 <= tile.rectangle.top :
                            top = True
                        else :
                            right = True
                    else :
                        if self.rect_final.bottom - 10 <= tile.rectangle.top :
                            top = True
                        else :
                            right = True
                elif tile.image == Map.img2 :
                    if self.isgrounded:
                        if self.rect_final.bottom - 5 <= tile.rectangle.top:
                            top = True
                        else:
                            left = True
                    else:
                        if self.rect_final.bottom - 10 <= tile.rectangle.top:
                            top = True
                        else:
                            left = True

                if tile.image == Map.img16 :
                    bottom = True
                elif tile.image == Map.img18 :
                    bottom = True

                if tile.image == Map.img1 or top :
                    self.isgrounded = True
                    self.speed_y = 0
                    self.acceleration_y = 0
                    self.position_y = tile.rectangle.top - self.rect_final.height+1
                    self.rect_final.top = self.position_y
                elif tile.image == Map.img17 or bottom :
                    self.speed_y = 0
                    self.acceleration_y = 0
                    self.position_y = tile.rectangle.bottom + 1
                    self.rect_final.top = self.position_y
                if tile.image == Map.img8 or right :
                    self.speed_x = 0
                    self.position_x = tile.rectangle.left - self.rect_final.width
                    self.rect_final.left = self.position_x
                elif tile.image == Map.img10 or left :
                    self.speed_x = 0
                    self.position_x = tile.rectangle.right - 1
                    self.rect_final.left = self.position_x
                if tile.image == Map.img48 :
                    self.state = 1
        air=True
        for collide in collisions :
            if collide.image == Map.img1 or collide.image == Map.img0 or collide.image == Map.img2 :
                air=False
        if air:
            self.isgrounded = False