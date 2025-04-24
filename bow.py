    # Gère les actions liées à l'arc et aux flèches tirées

import pygame
import math
import equation_trajectory
import Map
from sound_manager import SoundManager

class Bow():
    def __init__(self):
        """
        Initialise les variables qui caractérisent l'arc
        """

        # # Définie les images et paramètres utiles à l'affichage du joueur

        self.images = [
            pygame.transform.scale(
                pygame.image.load(f"assets/l0_arc{i}.png"),
                (pygame.image.load(f"assets/l0_arc{i}.png").get_width() // 3,
                 pygame.image.load(f"assets/l0_arc{i}.png").get_height() // 3)
            )
            for i in range(1, 5)
        ]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.animation_timer = 0
        self.animation_speed = 10

        # Définie les paramètres de l'arc (la gravité, la hitbox etc...)

        self.aiming = False
        self.gravity = 9.8
        self.rect_x, self.rect_y, self.rect_size = 0, 0, 0
        self.state=1

    def animation(self, dt, angle):
        """
        Gère l'animation de l'arc

        :param dt: le temps entre deux frames
        :param angle: l'angle selon lequel l'arc est incliné
        """
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]
            self.image = pygame.transform.rotate(self.image, angle * (180 / math.pi))

    def shot(self, dt, v0, theta, x, y):
        """
        Gère le tir d'un joueur

        :param dt: le temps entre deux frames
        :param v0: vitesse initiale
        :param theta: angle selon laquelle la flèche est tirée
        :param x: position en x
        :param y: position en y

        :return: la trajectoire que la flèche va suivre
        """
        return equation_trajectory.trajectory(v0, theta, dt, self.gravity, x, y)

    def draw_rectangle(self, screen, t, rect_x, rect_y, nb):
        """
        Affiche la barre de chargement

        :param screen: l'endroit où afficher le chargement
        :param t: le temps
        :param rect_x: la position sur l'axe x
        :param rect_y: la position sur l'axe y
        :param nb: le numéro du portail que le joueur va lancer
        """
        self.rect_size = min(t*6, 95)
        if nb==-1:
            color = (126, 34, 80)
        else:
            color = (68, 107, 166)
        pygame.draw.rect(screen, color, (rect_x, rect_y, self.rect_size, 28))

class Arrow() :
    def __init__(self, position) :
        """
        Initialise les variables qui caractérisent la flèche

        :param position: la position d'où la flèche est lancée
        """
        self.gravity = 9.8
        self.position_x = position[0]
        self.position_y = position[1]
        self.image = pygame.transform.scale(pygame.image.load("assets/Arrow.png"), (pygame.image.load("assets/Arrow.png").get_width() * 3, pygame.image.load("assets/Arrow.png").get_height() * 3))
        self.rect = pygame.Rect(position[0], position[1], 10, 10)
        self.portal_state = 0
        self.sono = SoundManager(False)

    def shot(self, dt, v0, theta, x, y):
        """
        Définie la trajectoire que va suivre la flèche

        :param dt: le temps entre les frames
        :param v0: la vitesse de la flèche (vitesse initiale)
        :param theta: l'angle actuel de la flèche
        :param x: la position sur l'axe x
        :param y: la position sur l'axe y
        """
        coordinate = equation_trajectory.trajectory(v0, theta, dt, self.gravity, x, y)
        self.image=pygame.transform.rotate(self.image, equation_trajectory.angle_arrow(v0, theta, dt, self.gravity*10)*180/math.pi)
        self.position_x = coordinate[0]
        self.position_y = -coordinate[1]
        self.rect.left = coordinate[0]
        self.rect.top = -coordinate[1]

    def collision(self, tiles, height, width) :
        """
        Gère les collisions de la flèche avec les tuiles de la map

        :param tiles: toutes les tuiles du jeu présentes sur la map
        :param height: la largeur de l'écran
        :param width: la longueur de l'écran

        :return: True si le flèche continue d'avancer, False si elle touche un objet
        :return: la tuile touchée s'il y en a une, 1 si elle touche un objet et 0 sinon
        """
        for tile in tiles :
            if self.rect.colliderect(tile.rectangle) and tile.image != Map.sky :

                # Collision avec les lasers

                if tile.image==Map.img48 or tile.image == Map.img54 :
                    return False, 0

                # Collision avec un boutton

                elif tile.image==Map.img49 or tile.image==Map.img50 or tile.image==Map.img51 or tile.image==Map.img52 :
                    self.sono.play_button_sound()
                    return False, 1

                # Collision avec un tuile
                if tile.image!=Map.img_empty and tile.image!=Map.img_empty_horizontal:
                    return False, tile

        # Flèche qui déborde du cadre, sinon, elle retourne True car pas de collision

        if self.position_y > height or self.position_x > width or self.position_x < 0 or self.position_y < 0 :
            return False, 0
        return True, 0

    def show(self, screen) :
        """
        Affiche la flèche

        :param screen: Endroit où afficher
        """
        screen.blit(self.image, (self.position_x, self.position_y))

    def position_portal(self, tile) :
        """
        Définie la position où va se situer le portail suite à une collision

        :param tile: l'znsemble des tuiles présentes sur la map
        :return: la position du portail
        """
        if tile.image == Map.img1 : # Vers le haut
            self.portal_state = -2
            return tile.rectangle.left - 30, tile.rectangle.top - 50
        elif tile.image == Map.img10 : # Vers la droite
            self.portal_state = 1
            return tile.rectangle.left - 15, tile.rectangle.top - 30
        elif tile.image == Map.img17 :  # Vers le bas
            self.portal_state = 2
            return tile.rectangle.left - 30, tile.rectangle.top - 5
        elif tile.image == Map.img8 :   # Vers la gauche
            self.portal_state = -1
            return tile.rectangle.left - 48, tile.rectangle.top - 30

        elif tile.image == Map.img0 :   # Coin en haut à gauche
            if self.rect.bottom - 15 <= tile.rectangle.top :
                self.portal_state = -2
                return tile.rectangle.left - 30, tile.rectangle.top - 50
            else :
                self.portal_state = -1
                return tile.rectangle.left - 48, tile.rectangle.top - 30
        elif tile.image == Map.img2 :   # Coin en haut à droite
            if self.rect.bottom - 13 <= tile.rectangle.top :
                self.portal_state = -2
                return tile.rectangle.left - 30, tile.rectangle.top - 50
            else :
                self.portal_state = 1
                return tile.rectangle.left - 15, tile.rectangle.top - 30
        elif tile.image == Map.img16 :  # Coin en bas à gauche
            if self.rect.top <= tile.rectangle.bottom :
                self.portal_state = 2
                return tile.rectangle.left - 30, tile.rectangle.top - 5
            else :
                self.portal_state = -1
                return tile.rectangle.left - 48, tile.rectangle.top - 30
        else :  # Coin en bas à droite
            if self.rect.top - 5 <= tile.rectangle.bottom :
                self.portal_state = 2
                return tile.rectangle.left - 30, tile.rectangle.top - 5
            else :
                self.portal_state = 1
                return tile.rectangle.left - 48, tile.rectangle.top - 30