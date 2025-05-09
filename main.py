    # Gère les intéractions du jeu complet

import game
import menu
import settings
import pygame
import level_selection
import skin_manager
import leader_menu
from sound_manager import SoundManager

def begin_game() :
    """
    Fonction principale permettant de lancer le jeu
    """

    # Actualise les paramètres principaux (level de départ, skin etc...)

    pygame.init()
    sono=SoundManager()
    skin=0
    world = 0
    level = 0
    time=0
    width = 900
    height = 600
    screen = pygame.display.set_mode((width, height))
    sound=True #le son et l'aide a la visée sont a activer dans les parametres, et c'est main qui fait le lien entre les deux
    help=True
    ranked=False #activer ou desactiver le mode chronométré
    name='' #nom pour le leaderboard
    window="menu" #ca represente la page sur laquelle on se trouve : si on est sur Menu et qu'on clique sur jouer, window va etre egal a level, puis a game quand on va choisir le lvl

    # Boucle de jeu qui s'exécute tant que le joueur n'appuie pas sur la croix

    while window != "exit" :

        # Appelle la classe skin quand le joueur clique sur l'icone associée

        if window == "skin":
            list=skin_manager.skin(screen, height, width, skin)
            window=list[0]
            skin=list[1]

        # Appelle la classe tutoriel quand le joueur clique sur l'icone associée

        if window == "tuto":
            list=game.game(0, True, screen, height, width, world, help, skin)
            window = list[0]
            level = list[1]

        # Appelle la classe menu quand le joueur clique sur l'icone associée

        if window == "menu" :
            window = menu.menu(screen, height, width)

        # Appelle la classe level quand le joueur clique sur l'icone associée

        if window == "level" :
            list=level_selection.Level_selection(screen, height, width, ranked) #ici j'ai mis une liste parce que ca renvoie a la fois la fenetre choisie (si on a cliqué sur le bouton maison ou choisi un lvl), et egalement le niveau choisi, pour le mettre en parametre de game, parce qu'on repasse par le main pour lancer le jeu avec l'appelle de la fonction Game qui a besoin du lvl en argument
            window=list[0]
            level=list[1]

        # Appelle la classe Jeu quand le joueur clique sur l'icone associée

        if window == "game" :
            list=game.game(level, True, screen, height, width, world, help, skin, ranked, name, time)
            window = list[0]
            level = list[1] #pareil ici, ca modifie le lvl où on est si on reussi a terminer le niveau (on return game et level = level + 1 pour que ca enchaine sur le level suivant)
            time=list[2]
        # Appelle la classe paramètres quand le joueur clique sur l'icone associée

        if window == "settings" :
            list=settings.settings(screen, height, width, sound, help)
            window = list[0] #tous les parametres devront etre passés par ici pour faire le lien entre game et settings
            sound=list[1]
            help=list[2]
            ranked=list[3]
            name=list[4]

            # Joue ou met sur pause la musique

            if sound==False :
                sono.pause_music()
            else:
                sono.resume_music()

        if window == "leaderboard" :
            window=leader_menu.leader_menu(screen, height, width)

    pygame.quit()

if __name__ == "__main__" :
    begin_game()