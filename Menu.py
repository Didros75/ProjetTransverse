    # Gère le menu (paramètres, bouton jouer etc...)
from sound_manager import SoundManager
import pygame

def menu(screen, height, width):
    """
    Fonction qui centralise toutes les actions liées aux skins

    :param screen: l'écran sur lequel afficher le menu
    :param height: la largeur de l'écran, un int
    :param width: la longueur de l'écran, un int
    :return: une chaine de caractère représentant une classe que le module main va afficher
    """
    sono = SoundManager(False)

    # Définie toues les éléments nécessaires pour afficher le menu principal

    button_height, button_width = 75, 187
    button=pygame.transform.scale(pygame.image.load('assets/meni_menu/bouton.png'), (button_width, button_height))
    settings_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/settings.png'), (button_height-15, button_height-15))
    exit_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_height, button_height))
    skin_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/Skin.png'), (button_height-15, button_height-15))
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    leader_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/Leader_board.png'), (button_height-15, button_height-15))
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (400, 300))
    help_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/help.png'), (button_height, button_height))
    instructions = ["Bienvenu dans Arctal !", "Le bouton tutoriel vous permet de démarrer un tuto" ,"rapide afin de vous expliquer les bases du jeu.", "Le bouton paramètre vous permet de gerer la musique, ","l'aide à la visée, ainsi que d'activer le mode chronométré", "Vous pouvez changer l'apparence de votre personnage","grace a l'onglet skin.", "Appuyez sur le bouton jouer afin d'etre redirigé vers la ","selection du chapitre de l'histoire (hors mode classé)","Le bouton trophé vous permet d'accéder au top 5 des ","meilleurs temps du mode chronométré", "Enfin, la croix vous permet de quitter le jeu", "BON JEU !"]
    screen.blit(background, (0, 0))
    font=pygame.font.Font(None, 60)
    font2=pygame.font.Font(None, 20)
    text_play = font.render("Jouer", True, (255, 255, 255))
    text_tuto = font.render("Tutoriel", True, (255, 255, 255))

    play_rect = pygame.Rect(width/2-button_width/2, 270, button.get_width(), button.get_height())
    tutorial_rect=pygame.Rect(width/2-button_width/2, 350, button.get_width(), button.get_height())
    settings_rect = pygame.Rect(width/2-3*(button_height-15)/2-5, 430, settings_button.get_width(), settings_button.get_height())
    skin_rect= pygame.Rect(width/2-(button_height-15)/2, 430, settings_button.get_width(), settings_button.get_height())
    leader_rect = pygame.Rect(width/2+(button_height-15)/2+5, 430, leader_button.get_width(), leader_button.get_height())
    exit_rect = pygame.Rect(width-button_height-35, 35, exit_button.get_width(), exit_button.get_height())
    help_rect = pygame.Rect(35, 35, help_button.get_width(), help_button.get_height())


    # Affiche tous ces éléments

    screen.blit(button, play_rect)
    screen.blit(help_button, help_rect)
    screen.blit(settings_button, settings_rect)
    screen.blit(exit_button, exit_rect)
    screen.blit(skin_button, skin_rect)
    screen.blit(leader_button, leader_rect)
    screen.blit(button, tutorial_rect)
    screen.blit(text_tuto, (tutorial_rect[0]+15,tutorial_rect[1]+18 ,0, 0))
    screen.blit(text_play, (play_rect[0]+35,play_rect[1]+18 ,0, 0))

    showing_help=False #variable pour savoir si le joueur est en train de cliquer sur le bouton help

    # Boucle qui s'éxecute tant que le joueur est sur le menu

    pygame.display.flip()
    in_game = True
    while in_game:

        if showing_help: #si le joueur reste appuyé sur le bouton, les instructions s'affichent
            screen.blit(board, (width/2 - board.get_width()/2, 150))
            for i in range(len(instructions)):
                text=font2.render(instructions[i], True, (255, 255, 255))
                screen.blit(text, (width/2 - board.get_width()/2 + 20, 170+i*20))

        # Parcours les évènements possibles que le joueur peut lancer

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si le joueur appuie sur le bouton tutoriel la fontion va retourner tuto

                if tutorial_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    return "tuto"

                # Si le joueur appuie sur le bouton skin la fontion va retourner la page skin

                if skin_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    return "skin"

                # Si le joueur appuie sur le bouton joueur la fontion va retourner la page level

                if play_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "level"

                # Si le joueur appuie sur le bouton paramètres la fontion va retourner la page settings

                if settings_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "settings"

                # Si le joueur appuie sur le bouton du leaderboard, il retourne la page leaderboard

                if leader_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "leaderboard"

                # Si le joueur appuie sur le bouton quitter la fontion va arrêter le jeu

                if exit_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.quit()
                    return False

                if help_rect.collidepoint(event.pos):
                    showing_help=True


            if event.type == pygame.MOUSEBUTTONUP: #quand le joueur arrete d'appuyer sur le bouton help, on remet tous les autres elements par dessus
                showing_help=False
                screen.blit(background, (0, 0))
                screen.blit(button, play_rect)
                screen.blit(help_button, help_rect)
                screen.blit(settings_button, settings_rect)
                screen.blit(exit_button, exit_rect)
                screen.blit(skin_button, skin_rect)
                screen.blit(leader_button, leader_rect)
                screen.blit(button, tutorial_rect)
                screen.blit(text_tuto, (tutorial_rect[0] + 15, tutorial_rect[1] + 18, 0, 0))
                screen.blit(text_play, (play_rect[0] + 35, play_rect[1] + 18, 0, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        pygame.display.flip()