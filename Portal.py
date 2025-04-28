    # Gère le placement des portails et la téléportation

import pygame
import Map

class Portal() :
    def __init__(self, x=0, y=0, num=1):
        """
        Initialise les paramètres nécessaires au chargement du portail

        :param x: la position sur l'axe x
        :param y: la position sur l'axe y
        :param num: le numéro du portail (le bleu ou le rose)
        """

        # Charge l'animation du portail selon si celui ci est un portail bleu ou rose

        self.num=num
        if self.num==1:
            self.images = [pygame.transform.scale(pygame.image.load(f"assets/portal_{i}.png"), (90, 120)) for i in range(1, 6)]
        else:
            self.images = [pygame.transform.scale(pygame.image.load(f"assets/portal{i}b.png"), (90, 120)) for i in range(1, 6)]
        self.image = self.images[0]
        self.frame=0
        self.animation_speed=0.1

        # Définie les variables de position et de taille

        self.pos_x=x
        self.pos_y=y
        self.state=1
        self.width=5
        self.length=70
        self.rect = pygame.Rect(self.pos_x + 48, self.pos_y + 20, self.width, self.length)

    def animate(self):
        """
        Anime le portail
        """
        self.image = self.images[int(self.frame)]
        self.frame+=self.animation_speed
        if self.frame >= len(self.images)-1:
            self.frame=0

        # Affiche le portail selon son état (s'il pointe vers le sol, le ciel etc...)

        if self.state == 1 : # S'il est dirigé vers la droite
            self.image = pygame.transform.rotate(self.image, 0)
            self.rect = pygame.Rect(self.pos_x +47, self.pos_y+28, self.width, self.length)
        elif self.state == -1 : # Vers la gauche
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = pygame.Rect(self.pos_x +37, self.pos_y+15, self.width, self.length)
        elif self.state == 2: # Vers le bas
            self.image = pygame.transform.rotate(self.image, -90)
            self.rect = pygame.Rect(self.pos_x+20, self.pos_y +42, self.length, self.width)
        else: # Vers le haut
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = pygame.Rect(self.pos_x+35, self.pos_y +37, self.length, self.width)


    def change_position(self, tile_touched, tiles, position, state) :
        """
        Cahnge la position du portail s'il est situé dans un mur

        :param tile_touched: la tuile que le portail a touchée
        :param tiles: l'ensemble des tuiles présentes sur la map
        :param position: la position actuelle du portail
        :param state: l'état actuel du portail (vers où il est dirigé)
        :return: la nouvelle position du portail
        """
        for i in range(30, len(tiles) - 60) :
            if tiles[i] == tile_touched :

                # Collisions sur l'axe vertical (change la position en y)

                if (state == 1 and tiles[i+31].image != Map.sky) or (state == -1 and tiles[i+29].image != Map.sky) :
                    return position[0], position[1] - 35
                elif (state == 1 and tiles[i-29].image != Map.sky) or (state == -1 and tiles[i-31].image != Map.sky) :
                    return position[0], position[1] + 15
                elif (state == 1 and tiles[i+61].image != Map.sky) or (state == -1 and tiles[i+59].image != Map.sky) :
                    return position[0], position[1] - 10

                # Collisions sur l'axe en horizontal (change la position en x)

                if (state == -2 and tiles[i-29].image != Map.sky) or (state == 2 and tiles[i+31].image != Map.sky) :
                    return position[0] - 45, position[1]
                elif (state == -2 and tiles[i-28].image != Map.sky) or (state == 2 and tiles[i+32].image != Map.sky) :
                    return position[0] - 10, position[1]
                elif (state == -2 and tiles[i-31].image != Map.sky) or (state == 2 and tiles[i+29].image != Map.sky) :
                    return position[0] + 10, position[1]
        return position

    def not_teleportable(self, tiles, tile_touched, screen) :
        """
        Vérifie qu'il est possible que le joueur puisse se téléporter

        :param tiles: l'ensemble des tuiles présentes sur la map
        :param tile_touched: la tuile avec laquelle le portail est en collision
        :return: True si le joueur peut se téléporter, False sinon
        """
        for i in range(60, len(tiles)-60) :
            if tiles[i] == tile_touched :

                # Vérifie si un bloc existe au dessus du portail et qu'il est dirigé vers le haut

                if (tiles[i-60].image != Map.sky) and self.state == -2:
                    return False

                # Vérifie si un bloc existe en dessous du portail et qu'il est dirigé vers le bas

                if (tiles[i+60].image != Map.sky) and self.state == 2:
                    return False
        return True

    def delete_portal(self, second_portal) :
        """
        Supprime les portails existants en les replaçant en dehors du cadre de jeu

        :param second_portal: le deuxième portail
        """
        self.pos_x = -75
        self.pos_y = -75
        second_portal.pos_x = -75
        second_portal.pos_y = -75