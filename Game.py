    # Gère les intéractions d'une partie (un niveau)

from Map import Create_map
from pygame import mouse
import equation_trajectory
from Player import ThePlayer
from bow import Bow, Arrow
from Portal import Portal
from sound_manager import SoundManager
from Story_functions import *
from chrono import Chrono
from chrono import ClassementCSV
import movie_manager

def game(level, game, screen, height, width, world, help, skin, ranked=False, name='', time=0) :
    """
    Lance un niveau ou le tutoriel et l'éxecute tant que le joueur est en partie

    :param level: le numéro du level (int)
    :param game: un booléen à True tant que le joueur est en partie, False sinon
    :param screen: l'endroit où afficher le niveau
    :param height: la largeur de l'écran (int)
    :param width: la longueur de l'écran (int)
    :param world: la numéro du monde où se situe la partie (int)
    :param help: un booléen à True si le joueur a activé l'aide, False sinon
    :param skin: le numéro du skin du joueur sous forme de chaine de caractère
    :return: une chaine de caractère qui correspond au prochain menu à afficher
    :return: un entier un correspond au prochain niveau
    """
    sono=SoundManager(False)    # Le son
    classement = ClassementCSV("Csv files/best_time.csv") #le classement de la ranked

    # Définit où commence les dialogues à chaque niveau et choisit le dialogue du level actuel

    liste_dialog=[0, 8, 12, 16, 20, 24, 28, 32, 35, 40, 44, 48, 52]
    line_txt = liste_dialog[level]

    # Définition les différentes positions de départ et crée le joueur à cet endroit

    start_position = [(40, 340), (10, 430), (10, 430), (10, 240),(10, 240), (10, 430), (10, 430), (10, 50), (10, 430), (10, 430), (10, 430), (10, 430), (10, 80)]
    player = ThePlayer(start_position[level][0], start_position[level][1], skin)

    # Crée les boutons pour recommencer le jeu ou retourner au menu

    menu_button = pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (75, 75))
    reset_button = pygame.transform.scale(pygame.image.load("assets/meni_menu/Reset.png"), (75, 75))
    menu_rect = pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    reset_rect = pygame.Rect(130, 35, reset_button.get_width(), menu_button.get_height())

    # Création des deux portails et des booléens qui disent s'il est possible de se téléporter ou non

    portal_1=Portal(-75, -75, 1)
    portal_2=Portal(-75, -75, 2)
    possible1 = False
    possible2 = False

    # Création de la map et de l'arrière plan

    if level == 0 :
            map = Create_map("Maps/map_tutorial.csv", screen)
    else:
            map = Create_map(f"Maps/map{level}.csv", screen)

    if level == 1:
        chrono = Chrono()  # le chronomètre
        chrono.start()
        time=chrono.start_time
    else:
        chrono = Chrono(time)
    if 1<=level<=4:
        world=0
    elif 5<=level<=8:
        world=1
    elif 9<=level<=12:
        world=2
    level_number=12

    background = pygame.image.load(f"assets/Backgrounds/fond{str(world)}.png")
    background = pygame.transform.scale(background, (width, height))

    clock = pygame.time.Clock()
    target_fps=60
    bow = Bow()  # Création de l'arc
    angle=0
    t=0 # le temps où le joueur appuie sur la souris
    t_cooldown=0    # le temps entre deux téléportations
    number_arrow = 1    # le numéro du portail qui va être tiré
    power = 0  # La puissance de la flèche
    line_len = 50   #longueur de la ligne d'aide
    collision = 0  # la tuile que la flèche touche (ou les lasers)

    aiming = False  # booléen si le joueur vise ou non
    shoted = False  # booléen si le joueur a tiré ou non
    shotable = False  # booléen s'il est possible de tirer ou non
    movable = False  # booléen si le joueur peut bouger ou non
    laser = True    # booléen si les lasers sont activés ou non

    # Boucle qui s'exécute tant que le joueur est tpujours en train de jouer la partie

    while game:
        clicked = False # booléen si le joueur appuie sur une touche du clavier ou non
        dt=clock.tick(60) * 0.001 * target_fps

        # Si le joueur a touché les lasers ils sont désactivés puis la map est affichée

        if collision == 1 :
            if laser :
                laser=False
            else:
                laser=True
        tiles = map.load_map(background, laser)

        # Si le joueur est mort on le recrée à la position de départ

        if player.death() :
            player = ThePlayer(start_position[level][0], start_position[level][1], skin)

        # Parcours tous les évenements que le joueur peut déclencher et vérifie s'il le fait ou non

        for event in pygame.event.get():

            # Fais quitter le jeu au joueur

            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                clicked=True    # devient True si le joueur appuie sur une touche du clavier

                # Active les touches de mouvement si le joueur ne tire pas et peut bouger

                if not player.aiming and movable:
                    if event.key == pygame.K_d: # Avec la touche D le joueur s'oriente et avance vers la droite
                        player.facingLeft=False
                        player.RIGHT=True
                    if event.key == pygame.K_q: # Avec la touche Q le joueur s'oriente et avance vers la droite
                        player.facingLeft=True
                        player.LEFT=True
                    if event.key == pygame.K_SPACE: # Avec la touche espace le joueur saute
                        if player.isgrounded:
                            player.jump()

                # Si le joueur appuie sur E et que la flèche n'est pas en train d'être tirée on change de portail à lancer

                if event.key == pygame.K_e:
                    if not shoted :
                        number_arrow = -number_arrow
                        bow.state=-bow.state

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si le joueur appuie sur le bouton du menu il est redirigé vers la fenêtre principale

                if menu_rect.collidepoint(event.pos):
                    return "menu", level, time

                # Si le joueur appuie sur le bouton recommencer le niveau est remis à 0

                if reset_rect.collidepoint(event.pos):
                    portal_1.delete_portal(portal_2)
                    possible1, possible2 = False, False
                    player = ThePlayer(start_position[level][0], start_position[level][1], skin)
                    laser=True

                # Si le joueur effectue un clique gauche il se met à viser

                if event.button==1:
                    if not shoted and shotable:
                        t = 0
                        player.RIGHT=False
                        player.LEFT=False
                        player.aiming = True
                        aiming=True

            if event.type == pygame.MOUSEBUTTONUP:

                # Si le joueur est en train de viser et qu'il relâche la souris il tire

                if event.button==1 and shoted==False and aiming==True and shotable:
                    angle = equation_trajectory.angle(player.position_x+player.rect_final.width/2, player.position_y+player.rect_final.height/2, mouse.get_pos()[0], mouse.get_pos()[1])
                    power=t
                    t = 0
                    px = player.position_x+player.rect_final.width/2
                    py = player.position_y+10
                    shoted=True
                    player.aiming=False
                    aiming=False
                    sono.stop_charging_sound()

            # Quand le joueur relâche les touches de mouvement il arrête de faire le mouvement qu'il effectuait

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.RIGHT=False
                if event.key == pygame.K_q:
                    player.LEFT=False
                if event.key == pygame.K_SPACE:
                    player.isjumping=False

        angle2 = equation_trajectory.angle(player.position_x+player.rect_final.width/2, player.position_y+player.rect_final.height/2, mouse.get_pos()[0], mouse.get_pos()[1])
        collision = 0   # la tuile que la flèche touche (ou les lasers)

        # Si le joueur a tiré on crée une flèche et on calcule sa position et sa puissance

        if shoted :
            position = player.get_position()
            arrow = Arrow(position)
            if power>=15:
                power=15
            arrow.shot(t, power*25, angle, px, -py)

            # On affiche la flèche et on vérifie si elle a touché une tuile

            arrow.show(screen)
            shoted, collision = arrow.collision(tiles, height, width)[0], arrow.collision(tiles, height, width)[1]

        # Si la flèche a touché une tuile on récupère la position où va se situer le portail

        if collision != 0 and collision != 1:
            position_portal = arrow.position_portal(collision)

            # On change la position du portail si besoin et on vérifie qu'il est possible de se téléporter

            if number_arrow == -1 : # Cas où le joueur tire le portail 2
                portal_2.state = arrow.portal_state
                position_portal = portal_2.change_position(collision, tiles, position_portal, arrow.portal_state)
                portal_2.pos_x, portal_2.pos_y = position_portal[0], position_portal[1]
                possible2 = portal_2.not_teleportable(tiles, collision, screen)

            else :  # Cas où le joueur tire le portail 1
                portal_1.state = arrow.portal_state
                position_portal = portal_1.change_position(collision, tiles, position_portal, arrow.portal_state)
                portal_1.pos_x, portal_1.pos_y = position_portal[0], position_portal[1]
                possible1 = portal_1.not_teleportable(tiles, collision, screen)

        # on anime le joueur, on appelle les fonctions de mouvement et on l'affiche

        player.animate(angle2)
        player.move_y(dt)
        player.move_x(dt)
        player.draw(screen)
        t+=0.1  # Incrémentation des variables qui représentent le temps
        t_cooldown+=0.1

        # Affichage des barres de chargement selon le portail qui va être lancé

        if number_arrow == 1:
            power_bar = pygame.transform.scale(pygame.image.load("assets/blue_chargin_bar.png"), (130, 50))
        else:
            power_bar = pygame.transform.scale(pygame.image.load("assets/pink_chargin_bar.png"), (130, 50))
        screen.blit(power_bar, (20, height - power_bar.get_height() - 20))

        list_point=[]
        if aiming:
            sono.play_charging_sound()

            # Si le joueur a activé l'aide et vise on calcule la trajectoire potentielle que la flèche va suivre

            if help:
                for i in range(line_len):
                    power=t
                    if power>15:
                        power=15
                    list_point.append(equation_trajectory.trajectory_line(power*25, -angle2,i/10,9.8 , player.position_x+30, player.position_y+20))

                # On affiche cette ligne avec la couleur du portail utilisé

                for point in list_point:
                    if number_arrow == 1:
                        pygame.draw.circle(screen, (68, 107, 166), point, 2)
                    else:
                        pygame.draw.circle(screen, (126, 34, 80), point, 2)

            # On anime et montre l'arc

            bow.animation(dt, angle2)
            screen.blit(bow.image, (player.position_x, player.position_y))
            bow.draw_rectangle(screen, t, 50, height-power_bar.get_height()-9, number_arrow)

        # On anime et montre les deux portails et les boutons d'arrêt et de réinitialisation

        portal_1.animate()
        portal_2.animate()
        screen.blit(portal_1.image, (portal_1.pos_x, portal_1.pos_y))
        screen.blit(portal_2.image, (portal_2.pos_x, portal_2.pos_y))
        screen.blit(menu_button, menu_rect)
        screen.blit(reset_button, reset_rect)

        if possible1 and possible2 :
            if t_cooldown>=3:

                # Si le joueur peut se téléporter et qu'il va dans un portail on définit le portail d'arrivée

                if player.rect_final.colliderect(portal_1.rect):
                    port=portal_2
                elif player.rect_final.colliderect(portal_2.rect):
                    port=portal_1
                if player.rect_final.colliderect(portal_1.rect) or player.rect_final.colliderect(portal_2.rect):
                    sono.play_tp_sound()

                    # On change l'emplacement du joueur pour le téléporter

                    if port.state==-2:  # Cas où le portail est orienté vers le haut
                        player.speed_y = -player.speed_y
                        player.position_y = port.rect.y-70
                        player.position_x=port.rect.x+15

                    elif port.state==2: # Cas où le portail est orienté vers le bas
                        player.position_y = port.rect.y+10
                        player.position_x = port.rect.x +10

                    elif port.state==-1:    # Cas où le portail est orienté vers la gauche
                        player.speed_x = -player.speed_x
                        player.position_y = port.rect.y
                        player.position_x = port.rect.x -20

                    elif port.state == 1:   # Cas où le portail est orienté vers la droite
                        player.speed_x = -player.speed_x
                        player.position_y = port.rect.y
                        player.position_x = port.rect.x - player.rect_final.width+30
                    t_cooldown = 0
                player.rect_final.x=player.position_x
                player.rect_final.y=player.position_y

        # Sinon s'il ne peut pas se téléporter on affiche un message sur l'écran

        else :
            if player.rect_final.colliderect(portal_1.rect) or player.rect_final.colliderect(portal_2.rect) :
                font = pygame.font.Font(None, 20)
                text_cant_play = font.render("Vous ne pouvez pas vous téléporter", True, (255, 255, 255))
                cant_play_rect = pygame.Rect(320, 490, 260, 35)
                pygame.draw.rect(screen, (0, 0, 0), cant_play_rect)
                screen.blit(text_cant_play, (335, 500))

        # On regarde si le joueur est en collision avec des tuiles et on l'arrête si c'est le cas

        player.hit_something(tiles)

        # Si le joueur arrive à droite de l'écran on passe au niveau suivant

        if player.rect_final.x >= 880:
            if level < level_number:
                return "game", level+1, time
            else:
                if ranked:
                    classement.add_score(name, classement._time_to_str(chrono.stop()))
                else :
                    video_player = movie_manager.PngPlayer("end_story", screen, position=(0, 0), fps=24)
                    video_player.play()
                return "menu", level, time

        # On affiche les boites de dialogue si besoin

        if not ranked:
            if dialog_box(line_txt, screen, skin, t) == 1:
                movable = False
                shotable = False
                if clicked:
                    line_txt+=1
            else:
                movable=True
                shotable=True
        else:
            movable = True
            shotable = True

        pygame.display.flip()