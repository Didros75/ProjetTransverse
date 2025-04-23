    # Gère le menu du choix des niveaux

import pygame
from sound_manager import SoundManager

def Level_selection(screen, height, width):
    """
    Affiche le menu du choix des niveaux et gère les évènements qui y sont liés

    :param screen: l'écran sur lequel afficher le menu
    :param height: la largeur de l'écran (int)
    :param width: la longueur de l'écran (int)
    :return: une chaine de caractère représentant le prochain menu à afficher
    :return: un entier égal 0 si le joueur retourne au menu principal, égal au level choisi sinon
    """

    # Initialise tous les éléments nécessaires à la création du menu des niveaux

    button_dim=75
    sono = SoundManager(False)
    font = pygame.font.Font(None, 40)
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_dim, button_dim))
    menu_rect=pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (500, 300))
    button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Vide.png"), (button_dim-10, button_dim-10))
    chapter1_text=font.render("Chapter 1", True, (255, 255, 255))

    # Affiche tous ces éléments

    screen.blit(background, (0, 0))
    screen.blit(board, (width/2-250, 150))
    screen.blit(chapter1_text,(width/2-220, 180))
    screen.blit(menu_button, menu_rect)

    # Création des boutons qui représentent les différents niveaux

    buttons = []
    for i in range(5):
        rect = pygame.Rect(240 + i * 85, 220, button_dim-10, button_dim-10)
        buttons.append((rect, str(i + 1)))

    # Affichage de chacun des boutons

    for rect, number in buttons:
        screen.blit(button, rect)
        text = font.render(number, True, (255, 255, 255))
        screen.blit(text, (rect.x + 25, rect.y + 20))

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

                # Si le joueur appuie sur un bouton level, il est redirigé vers ce level

                for rect, number in buttons:
                    if rect.collidepoint(event.pos):
                        sono.play_button_sound()
                        return "game", int(number)

            # Permet à l'utilisateur de quitter la page principale

            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()