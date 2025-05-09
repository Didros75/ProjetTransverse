    # Affiche et gère le leaderboard

import pygame
from sound_manager import SoundManager
from chrono import ClassementCSV

def leader_menu(screen, height, width):
    """
    Fonction pour afficher le leader board, soit les 5 premiers noms et temps du fichier best_time.csv
    """

    # Crée les éléments nécessaires au menu

    button_size=75
    sono = SoundManager(False)
    font = pygame.font.Font(None, 45)
    title_font=pygame.font.Font(None, 55)
    classement = ClassementCSV("Csv files/best_time.csv")
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button = pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_size, button_size))
    exit_button = pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_size, button_size))
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (400, 300))
    text=title_font.render("Top 5 :", True, (255, 255, 255))
    menu_rect = pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    exit_rect = pygame.Rect(width - button_size - 35, 35, exit_button.get_width(), exit_button.get_height())

    # Affiche ces éléments

    screen.blit(background, (0, 0))
    screen.blit(board, (width/2 - board.get_width()/2, 150))
    screen.blit(menu_button, menu_rect)
    screen.blit(exit_button, exit_rect)
    screen.blit(text, (width/2-170, 175))

    liste_players=classement.top_5()[0]#recupère les 5 premiers noms
    liste_temps=classement.top_5()[1]#recupère les 5 premiers temps

    for i in range(len(liste_players)): #les affiche
        text=str(i+1 )+" "+str(liste_players[i]) +" "+ str(liste_temps[i])
        text_surface=font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (width/2-170, 230 + i * 40))
    pygame.display.flip()
    in_game = True

    # Permet de retourner au menu ou de quitter le jeu

    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "menu"
                elif exit_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        pygame.display.flip()