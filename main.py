    # Gère les intéractions du jeu complet

import Game
import Menu
import Settings
import pygame
import level_selection
from sound_manager import SoundManager

def begin_game() :
    pygame.init()
    sono=SoundManager()
    world = 0
    level = 0
    width = 900
    height = 600
    screen = pygame.display.set_mode((width, height))
    sound=True #le son et l'aide a la visée sont a activer dans les parametres, et c'est main qui fait le lien entre les deux
    help=True
    window="menu" #ca represente la page sur laquelle on se trouve : si on est sur Menu et qu'on clique sur jouer, window va etre egal a level, puis a game quand on va choisir le lvl

    while window != "exit" :
        # !!!! si tu veux mettre le tuto, fais un if windows = 'tuto', et la t'appelle ton module, si tu le fais pas ca va planter quand tu cliques
        if window == "menu" :
            window = Menu.menu(screen, height, width)
        if window == "level" :
            list=level_selection.Level_selection(screen, height, width) #ici j'ai mis une liste parce que ca renvoie a la fois la fenetre choisie (si on a cliqué sur le bouton maison ou choisi un lvl), et egalement le niveau choisi, pour le mettre en parametre de game, parce qu'on repasse par le main pour lancer le jeu avec l'appelle de la fonction Game qui a besoin du lvl en argument
            window=list[0]
            level=list[1]
        if window == "game" :
            list=Game.game(level, True, screen, height, width, world, help)
            window = list[0]
            level = list[1] #pareil ici, ca modifie le lvl où on est si on reussi a terminer le niveau (on return game et level = level + 1 pour que ca enchaine sur le level suivant)
        if window == "settings" :
            list=Settings.settings(screen, height, width, sound, help)
            window = list[0] #tous les parametres devront etre passés par ici pour faire le lien entre game et settings
            sound=list[1]
            help=list[2]

            if sound==False :
                sono.pause_music() #ca c'est avec la class sound manager flemme d'expliquer y touchez pas
            else:
                sono.resume_music()

    pygame.quit()

if __name__ == "__main__" :
    begin_game()