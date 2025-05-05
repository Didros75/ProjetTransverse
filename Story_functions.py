    # Gère less dialogues des personnages

import pygame
import csv

width=900
height=600

def dialog_box(line, screen, skin, index, talker=2):
    """
    Affiche les dialogues des personnages au tutoriel et en début dde niveau

    :param line: le numéro de la ligne de script qui va être affichée (int)
    :param screen:l'écran sur lequel afficher le dialogue
    :param skin: le vêtement actuel du personnage (chaine de caractère)
    :param index: le numéro de l'asset du personnage à afficher (int)
    :param talker: celui qui dit le dialogue : le joueur ou l'ennemi (int)
    :return: 1 si le dialogue existe, 0 sinon
    """

    # Définie les lignes dans le fichier où le joueur et son ennemi parle
    # puis définit celui qui dit le dialogue à afficher

    dialogs_hero=[13, 17, 21, 25, 29, 32, 37, 41, 45, 49, 52]
    dialogs_reaper=[8, 9, 12, 16, 20, 24, 28, 35, 36, 40, 44, 48, 43, 53]
    if line in dialogs_hero:
        talker=0
    elif line in dialogs_reaper:
        talker=1

    # Crée la boite de dialogue et charge les assets des personnages

    font=pygame.font.SysFont(None, 30)
    box=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (500, 150))
    hero_idle = [pygame.image.load(f"assets/{skin}/l0_sprite_{i}.png") for i in range(1, 5)]
    reaper_idle = [pygame.transform.scale(pygame.image.load(f"assets/Reaper/l0_reaper_idle{i}.png"), (200, 200)) for i in range(1, 5)]

    # ouvre le fichier où se situent les dialogues et récupère la ligne à afficher

    with open('Csv files/dialog.csv', newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier, delimiter=';')
        lecteur = list(lecteur)
        ligne=lecteur[line]

        if ligne!=[]:

            # Affiche l'utilisateur qui parle

            if talker==0:
                screen.blit(hero_idle[int(index%4)], (width / 2 - box.get_width() / 2, height - box.get_height() - 100))
            elif talker==1:
                screen.blit(reaper_idle[int(index%4)], (width / 2 + box.get_width() / 2 - 150, height - box.get_height() - 160))

            # Affiche la boite de dialogue et le texte

            screen.blit(box, (width / 2 - box.get_width() / 2, height - box.get_height() - 20))
            liste_text=ligne[0].split("/")
            for elem in range(len(liste_text)):
                text_blit = font.render(liste_text[elem], True, (255, 255, 255))
                screen.blit(text_blit, (width / 2 - box.get_width() / 2 + 20, height - box.get_height()+ elem*25))
            return 1
        else:
            return 0