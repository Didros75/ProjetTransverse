    # Gère le menu paramètre

import pygame
from sound_manager import SoundManager

def settings(screen, height, width, sound, help):
    """


    :param screen: l'endroit où afficher le menu
    :param height: la largeur de l'écran (int)
    :param width: la longueur de l'écran (int)
    :param sound: Un booléen à True s'il y a du son, False sinon
    :param help: Un booléen à True s'il y a de l'aide, False sinon
    :return: une chaine de caractère représentant le menu à afficher
    :return: un booléen si on doit afficher ou non l'aide
    :retur: un booléen si la musique doit se jouer ou non
    """

    # Initialise les éléments qui composent le menu des paramètres

    sono=SoundManager(False)
    button_height, button_width = 75, 187
    litle_button=50
    title_font = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 40)

    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_height, button_height))
    exit_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_height, button_height))
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (400, 300))
    x_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (litle_button, litle_button))
    y_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/Y.png'), (litle_button, litle_button))

    text_parametres = title_font.render("Settings :", True, (255, 255, 255))
    text_son=font.render("Music : ", True, (255, 255, 255))
    text_aide=font.render("Help : ", True, (255, 255, 255))

    menu_rect=pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    exit_rect = pygame.Rect(width-button_height-35, 35, exit_button.get_width(), exit_button.get_height())

    son_x_rect=pygame.Rect(width/2+10, 210, x_button.get_width(), x_button.get_height())
    son_y_rect=pygame.Rect(width/2-y_button.get_width()-10, 210, y_button.get_width(), y_button.get_height())
    aide_x_rect=pygame.Rect(width/2+10, 260, x_button.get_width(), x_button.get_height())
    aide_y_rect=pygame.Rect(width/2-y_button.get_width()-10, 260, y_button.get_width(), y_button.get_height())

    # Affiche tous ces éléments sur l'écran

    screen.blit(background, (0, 0))
    screen.blit(board, (width/2-200, 150))
    screen.blit(text_parametres, (width/2-170, 170))
    screen.blit(text_son, (width/2-170, 220))
    screen.blit(text_aide, (width/2-170, 270))
    screen.blit(x_button, son_x_rect)
    screen.blit(y_button, son_y_rect)
    screen.blit(x_button, aide_x_rect)
    screen.blit(y_button, aide_y_rect)
    screen.blit(menu_button, menu_rect)
    screen.blit(exit_button, exit_rect)
    pygame.display.flip()

    # Boucle qui s'éxecute tant que le joueur reste sur la fenêtre des paramètres

    in_game = True
    while in_game:

        # Si le son est activé on coche la case oui, sinon on coche la case non

        if sound:
            pygame.draw.rect(screen, (27, 20, 100), (son_x_rect[0]+12, son_x_rect[1]+12, son_x_rect[2]-22, son_x_rect[3]-22))
            screen.blit(y_button, son_y_rect)
        else:
            pygame.draw.rect(screen, (27, 20, 100), (son_y_rect[0]+12, son_y_rect[1]+12, son_y_rect[2]-22, son_y_rect[3]-22))
            screen.blit(x_button, son_x_rect)

        # Si l'aide est activée on coche la case oui, sinon on coche la case non

        if help:
            pygame.draw.rect(screen, (27, 20, 100), (aide_x_rect[0]+12, aide_x_rect[1]+12, aide_x_rect[2]-22, aide_x_rect[3]-22))
            screen.blit(y_button, aide_y_rect)
        else:
            pygame.draw.rect(screen, (27, 20, 100), (aide_y_rect[0]+12, aide_y_rect[1]+12, aide_y_rect[2]-22, aide_y_rect[3]-22))
            screen.blit(x_button, aide_x_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si le joueur appuie sue le bouton du menu il est redirigé vers le menu principal

                if menu_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "menu", sound, help

                # Si le joueur appuie sur le bouton du son il est activé ou désactivé

                if son_x_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    sound=False
                if son_y_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    sound=True

                # Si le joueur appuie sur le bouton de l'aide elle est activée ou désactivée

                if aide_x_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    help=False
                if aide_y_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    help=True

                # Si le joueur appuie sur le bouton exit il va quitter le jeu

                if exit_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.quit()
                    return False

            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        pygame.display.flip()
