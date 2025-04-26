    # Gère le menu du choix des niveaux

import pygame
from sound_manager import SoundManager

def Level_selection(screen, height, width, ranked):
    """
    Affiche le menu du choix des niveaux et gère les évènements qui y sont liés

    :param screen: l'écran sur lequel afficher le menu
    :param height: la largeur de l'écran (int)
    :param width: la longueur de l'écran (int)
    :return: une chaine de caractère représentant le prochain menu à afficher
    :return: un entier égal 0 si le joueur retourne au menu principal, égal au level choisi sinon
    """

    # Initialise tous les éléments nécessaires à la création du menu des niveaux
    if ranked:
        return "game", 1
    button_dim=100
    sono = SoundManager(False)
    font = pygame.font.Font(None, 50)
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_dim, button_dim))
    menu_rect=pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (500, 300))
    button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Vide.png"), (button_dim-10, button_dim-10))
    chapter1_text=font.render("Chapitre :", True, (255, 255, 255))

    # Affiche tous ces éléments

    screen.blit(background, (0, 0))
    screen.blit(board, (width/2-250, 150))
    screen.blit(chapter1_text,(width/2-200, 190))
    screen.blit(menu_button, menu_rect)

    # Création des boutons qui représentent les différents chapitres

    buttons = []
    for i in range(3):
        rect = pygame.Rect(240 + i * 160, 250, button_dim-10, button_dim-10)
        buttons.append((rect, str(i + 1)))

    # Affichage de chacun des boutons

    for rect, number in buttons:
        screen.blit(button, rect)
        font = pygame.font.Font(None, 60)
        text = font.render(number, True, (255, 255, 255))
        screen.blit(text, (rect.x + 33, rect.y + 28))

    # Boucle qui s'exécute tant  que le joueur n'a pas quitté la page level

    pygame.display.flip()
    in_game = True
    while in_game:
        for event in pygame.event.get():    # parcours des évènements pygame possibles
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si le joueur appuie sur le bouton du menu, il est renvoyé sur la page du menu principal

                if menu_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    return "menu", 0

                # Si le joueur appuie sur un bouton chapitre, il est redirigé vers ce chapitre

                for rect, number in buttons:
                    if rect.collidepoint(event.pos):
                        sono.play_button_sound()
                        if int(number) == 1:
                            return "game", 1
                        elif int(number) == 2:
                            return "game", 5
                        elif int(number) == 3:
                            return "game", 12

            # Permet à l'utilisateur de quitter la page principale

            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()