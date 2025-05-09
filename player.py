    # Module contenant la classe qui gère les intéractions du joueur

import math
import pygame
import map

class ThePlayer(pygame.sprite.Sprite) :
    def __init__(self, position_x, position_y,skin, gravity = 0.6) :
        """
        Initialise les variables qui caractérisent le joueur

        :param position_x: position de départ du joueur su l'axe x (int)
        :param position_y: position de départ du joueur su l'axe y (int)
        :param skin: définit le skin actuel du joueur (chaine de caractère)
        :param gravity: définit la gravité (plus elle est haute plus elle agit sur le joueur), int
        """
        pygame.sprite.Sprite.__init__(self)

        # Définie la vitesse, la position et l'accélération initiale

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

        # Définie les touches sur lesquelles le joueur appuie (False si le joueur ne fait rien)

        self.LEFT = False
        self.RIGHT = False
        self.SPACE = False
        self.facingLeft = False
        self.aiming=False

        # Définie les images et paramètres utiles à l'affichage du joueur

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
        """
        Gère l'animation du joueur

        :param angle: Angle en radians représentant la direction de visée
        """
        if self.LEFT or self.RIGHT:
            self.frame_count += self.animation_speed #ajoute à chaque frame la variable animation_speed
            if self.frame_count >= len(self.sprites_right): #si frame_count arrive à la fin de la liste des sprites, on retourne au premier
                self.frame_count = 0
            self.sprite_index = int(self.frame_count) #le sprite actif est défini par frame count arrondi

            if self.RIGHT: #si le joueur regarde a droite, on pioche dans la liste sprites_right
                self.image = self.sprites_right[self.sprite_index]
                self.facingLeft = False
            elif self.LEFT: #idem pour la gauche
                self.image = self.sprites_left[self.sprite_index]
                self.facingLeft = True

        elif self.speed_x<=0.5: #idem quand il ne bouge pas
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
        retourne la position du joueur
        """
        return self.position_x, self.position_y

    def jump(self) :
        """
        Permet de faire sauter le joueur
        """
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
        """
        Affiche le joueur

        :param ref: l'endroit sur lequel le joueur doit être affiché
        """
        self.image = pygame.transform.scale(self.image, (40, 50))
        ref.blit(self.image, (self.position_x, self.position_y))

    def move_x(self, dt) :
        """
        Permet au joueur d'avancer sur l'axe x (vers la gauche ou la droite)

        :param dt: temps écoulé depuis la dernière frame
        """

        # Modifie l'accélération du joueur en fonction de son déplacement

        self.acceleration_x = 0
        if self.LEFT :
            self.acceleration_x -=5
        if self.RIGHT :
            self.acceleration_x +=5
        self.acceleration_x += self.speed_x * self.friction

        # Modifie la vitesse et définie la nouvelle position du joueur

        self.speed_x+=self.acceleration_x * dt
        self.max_speed(8)
        self.position_x += (0.5 * self.acceleration_x) * (dt*dt) + self.speed_x * dt
        self.rect_final.x = self.position_x

    def max_speed(self, maxi) :
        """
        Empêche le joueur de dépasse une vitesse maximale

        :param maxi: définie la vitesse maximale que le joueur peut atteindre
        """
        min(-maxi, max(self.speed_x, maxi))
        if abs(self.speed_x) > maxi :
            self.speed_x = 0

    def move_y(self, dt) :
        """
        Permet au joueur d'avancer sur l'axe y (vers le haut ou le bas)

        :param dt: temps écoulé depuis la dernière frame
        """

        # Change la vitesse et la définie la nouvelle position du joueur

        if self.isgrounded == False :
            self.speed_y -= self.gravity * dt
        if self.speed_y <= -20:
            self.speed_y = -20
        self.position_y -= (0.5*self.acceleration_y) * (dt*dt) + self.speed_y * dt
        self.rect_final.y = self.position_y

    def hit_something(self, tiles) :
        """
        Gère les collisions entre les tuiles et le joueur

        :param tiles: une liste de toutes les tuiles sur la map
        """
        if 0 > self.speed_y > -0.6:
            self.speed_y = 0

        # Parcours toutes les tuiles et vérifie si le joueur les touche ou pas

        collisions = []
        for tile in tiles :
            if self.rect_final.colliderect(tile.rectangle) and tile.image != map.sky :

                # Gère les collisions avec les coins

                top = False
                right = False
                bottom = False
                left = False

                collisions.append((tile))

                if tile.image == map.img0 : # Coin en haut à gauche
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
                elif tile.image == map.img2 : # Coin en haut à droite
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

                if tile.image == map.img16 : # Coins en bas
                    bottom = True
                elif tile.image == map.img18 :
                    bottom = True

                if tile.image == map.img1 or top : # Collision par le haut
                    self.isgrounded = True
                    self.speed_y = 0
                    self.acceleration_y = 0
                    self.position_y = tile.rectangle.top - self.rect_final.height+1
                    self.rect_final.top = self.position_y
                elif tile.image == map.img17 or bottom : # Collision par le bas
                    self.speed_y = 0
                    self.acceleration_y = 0
                    self.position_y = tile.rectangle.bottom + 1
                    self.rect_final.top = self.position_y
                if tile.image == map.img8 or right : # Collision par la droite
                    self.speed_x = 0
                    self.position_x = tile.rectangle.left - self.rect_final.width
                    self.rect_final.left = self.position_x
                elif tile.image == map.img10 or left : # Collision par la gauche
                    self.speed_x = 0
                    self.position_x = tile.rectangle.right - 1
                    self.rect_final.left = self.position_x

                # Collision avec un laser (on active la mort du joueur)

                if tile.image == map.img48 or tile.image==map.img54:
                    self.state = 1

        # Change le statut du joueur (si il touche le sol ou non)

        air=True
        for collide in collisions :
            if collide.image == map.img1 or collide.image == map.img0 or collide.image == map.img2 :
                air=False
        if air:
            self.isgrounded = False