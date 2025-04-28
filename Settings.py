    # Gère le menu paramètre

import pygame
from sound_manager import SoundManager

def ask_name(screen):
    """Cette fonction permet de demander a l'utilisateur d'entrer son nom s'il choisit le mode competitif"""
    font = pygame.font.Font(None, 32)
    input_text = ""
    active = True

    while active: #cette boucle sert a gerer les entrées de texte a l'ecran sur pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        txt_instructions = font.render("Entrez votre nom :", True, (255, 255, 255))
        pygame.draw.rect(screen, (27, 20, 100), (270, 392, 300, 40))
        pygame.draw.rect(screen, (0, 0, 0), (270, 392, 300, 40), 2)
        txt_surface = font.render(input_text, True, (255, 255, 255))
        screen.blit(txt_surface, (280, 400))
        screen.blit(txt_instructions, (280, 370))
        pygame.display.flip()

    return input_text

def settings(screen, height, width, sound, help, chrono=False):
    """
    gère les paramètres du jeu.

    :param screen: l'endroit où afficher le menu
    :param height: la largeur de l'écran (int)
    :param width: la longueur de l'écran (int)
    :param sound: Un booléen à True s'il y a du son, False sinon
    :param help: Un booléen à True s'il y a de l'aide, False sinon
    :return: une chaine de caractère représentant le menu à afficher
    :return: un booléen si on doit afficher ou non l'aide
    :return: un booléen si la musique doit se jouer ou non
    """

    # Initialise les éléments qui composent le menu des paramètres

    sono=SoundManager(False)
    button_height, button_width = 75, 187
    litle_button=50
    title_font = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 35)
    name=''
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_height, button_height))
    exit_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_height, button_height))
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (400, 300))
    x_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (litle_button, litle_button))
    y_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/Y.png'), (litle_button, litle_button))

    text_parametres = title_font.render("Paramètres :", True, (255, 255, 255))
    text_son=font.render("Son : ", True, (255, 255, 255))
    text_aide=font.render("Aide : ", True, (255, 255, 255))
    text_chrono=font.render("Classé : ", True, (255, 255, 255))


    menu_rect=pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    exit_rect = pygame.Rect(width-button_height-35, 35, exit_button.get_width(), exit_button.get_height())

    son_x_rect=pygame.Rect(width/2+10, 210, x_button.get_width(), x_button.get_height())
    son_y_rect=pygame.Rect(width/2-y_button.get_width()-10, 210, y_button.get_width(), y_button.get_height())
    aide_x_rect=pygame.Rect(width/2+10, 260, x_button.get_width(), x_button.get_height())
    aide_y_rect=pygame.Rect(width/2-y_button.get_width()-10, 260, y_button.get_width(), y_button.get_height())
    chrono_x_rect = pygame.Rect(width / 2 + 10, 310, x_button.get_width(), x_button.get_height())
    chrono_y_rect = pygame.Rect(width / 2 - y_button.get_width() - 10, 310, y_button.get_width(), y_button.get_height())

    # Affiche tous ces éléments sur l'écran

    screen.blit(background, (0, 0))
    screen.blit(board, (width/2-200, 150))
    screen.blit(text_parametres, (width/2-170, 170))
    screen.blit(text_son, (width/2-170, 220))
    screen.blit(text_aide, (width/2-170, 270))
    screen.blit(text_chrono, (width/2-170, 320))
    screen.blit(x_button, son_x_rect)
    screen.blit(y_button, son_y_rect)
    screen.blit(x_button, aide_x_rect)
    screen.blit(y_button, aide_y_rect)
    screen.blit(x_button, chrono_x_rect)
    screen.blit(y_button, chrono_y_rect)
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

        if chrono:
            pygame.draw.rect(screen, (27, 20, 100), (chrono_x_rect[0]+12, chrono_x_rect[1]+12, chrono_x_rect[2]-22, chrono_x_rect[3]-22))
            screen.blit(y_button, chrono_y_rect)
        else:
            pygame.draw.rect(screen, (27, 20, 100), (chrono_y_rect[0]+12, chrono_y_rect[1]+12, chrono_y_rect[2]-22, chrono_y_rect[3]-22))
            screen.blit(x_button, chrono_x_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si le joueur appuie sur le bouton du menu il est redirigé vers le menu principal

                if menu_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "menu", sound, help, chrono, name

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

                #Active et desactive le mode chronometré, et demande un nom
                if chrono_x_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.draw.rect(screen, (27, 20, 100), (270, 360, 300, 73))
                    chrono = False
                if chrono_y_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    chrono = True
                    name=ask_name(screen)

                # Si le joueur appuie sur le bouton exit il va quitter le jeu

                if exit_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.quit()
                    return False

            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        pygame.display.flip()
