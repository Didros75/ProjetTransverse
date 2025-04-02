    # Gère les intéractions d'une partie (un niveau)

import pygame
from Map import Create_map
from pygame import mouse
import equation_trajectory
from Player import ThePlayer
from bow import Bow, Arrow
from Portal import Portal
from sound_manager import SoundManager
import time

def game(level, game, screen, height, width, world, help, skin) :
    sono=SoundManager(False)
    power = 0

    bow = Bow()

        # Définition des différentes positions de départ et d'arrivé

    start_position = [(40, 340), (10, 430), (10, 430), (10, 240), (10, 430), (10, 430)]
    menu_button = pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (75, 75))
    menu_rect = pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())

    player = ThePlayer(start_position[level][0], start_position[level][1])

    power_bar = pygame.transform.scale(pygame.image.load("assets/blue_chargin_bar.png"), (130, 50))
    portal_1=Portal(-75, -75, 1)
    portal_2=Portal(-75, -75, 2)

    if level == 0 :
            map = Create_map("Maps/map_tutorial.csv", screen)
    else:
            map = Create_map(f"Maps/map{level}.csv", screen)

    clock = pygame.time.Clock()
    target_fps=60


    possible1 = False
    possible2 = False
    aiming=False
    shoted=False
    angle=0
    t=0
    t_cooldown=0
    number_arrow = 1

    line=True
    line_len=50
    collision=0
    laser=True

    if world == 0 :
        background=pygame.image.load("assets/fond2.jpg")
    elif world == 1 :
        background = pygame.image.load("assets/fond.jpg")
    elif world == 2 :
        background = pygame.image.load("assets/fond1.png")

    background = pygame.transform.scale(background, (width, height))

    while game:
        dt=clock.tick(60) * 0.001 * target_fps
        if collision == 1 :
            laser=False
        tiles = map.load_map(background, laser)


        if player.death() :
            player = ThePlayer(start_position[level][0], start_position[level][1])



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if not player.aiming:
                    if event.key == pygame.K_d:
                        player.facingLeft=False
                        player.RIGHT=True
                    if event.key == pygame.K_q:
                        player.facingLeft=True
                        player.LEFT=True
                    if event.key == pygame.K_SPACE:
                        if player.isgrounded:
                            player.jump()
                if event.key == pygame.K_e:
                    if not shoted :
                        number_arrow = -number_arrow
                        bow.state=-bow.state

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    return "menu", level

                if event.button==1:
                    if not shoted:
                        t = 0
                        player.RIGHT=False
                        player.LEFT=False
                        player.aiming = True
                        aiming=True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button==1 and shoted==False and aiming==True:

                    angle = equation_trajectory.angle(player.position_x+player.rect_final.width/2, player.position_y+player.rect_final.height/2, mouse.get_pos()[0], mouse.get_pos()[1])
                    power=t
                    t = 0
                    px = player.position_x+player.rect_final.width/2
                    py = player.position_y+10
                    shoted=True
                    player.aiming=False
                    aiming=False
                    sono.stop_charging_sound()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.RIGHT=False
                if event.key == pygame.K_q:
                    player.LEFT=False
                if event.key == pygame.K_SPACE:
                    player.isjumping=False

        angle2 = equation_trajectory.angle(player.position_x+player.rect_final.width/2, player.position_y+player.rect_final.height/2, mouse.get_pos()[0], mouse.get_pos()[1])

        collision = 0

        if shoted :
            position = player.get_position()
            arrow = Arrow(position)
            if power>=15:
                power=15
            arrow.shot(t, power*25, angle, px, -py)

            arrow.show(screen)
            shoted, collision = arrow.collision(tiles, height, width)[0], arrow.collision(tiles, height, width)[1]

        if collision != 0 and collision != 1:

            position_portal = arrow.position_portal(collision)

            if number_arrow == -1 :
                portal_2.state = arrow.portal_state
                function = portal_2.change_position(collision, tiles, position_portal, arrow.portal_state)
                position_portal = function[0]
                portal_2.pos_x, portal_2.pos_y = position_portal[0], position_portal[1]
                possible2 = portal_2.not_teleportable(tiles, collision)

            else :
                portal_1.state = arrow.portal_state
                function = portal_1.change_position(collision, tiles, position_portal, arrow.portal_state)
                position_portal = function[0]
                """while function[1] == 1 : ###
                    function = portal_1.change_position(collision, tiles, position_portal, arrow.portal_state)
                    print(position_portal)
                    position_portal = function[0]"""
                portal_1.pos_x, portal_1.pos_y = position_portal[0], position_portal[1]
                possible1 = portal_1.not_teleportable(tiles, collision)

        player.animate(angle2)
        player.move_y(dt)
        player.move_x(dt)
        player.draw(screen)
        t+=0.1
        t_cooldown+=0.1
        if number_arrow == 1:
            power_bar = pygame.transform.scale(pygame.image.load("assets/blue_chargin_bar.png"), (130, 50))
        else:
            power_bar = pygame.transform.scale(pygame.image.load("assets/pink_chargin_bar.png"), (130, 50))
        screen.blit(power_bar, (20, height - power_bar.get_height() - 20))
        list_point=[]
        if aiming:
            sono.play_charging_sound()
            if help:
                if line==True:
                    for i in range(line_len):
                        power=t
                        if power>15:
                            power=15

                        list_point.append(equation_trajectory.trajectory_line(power*25, -angle2,i/10,9.8 , player.position_x+30, player.position_y+20))


                    for point in list_point:
                        if number_arrow == 1:
                            pygame.draw.circle(screen, (68, 107, 166), point, 2)
                        else:
                            pygame.draw.circle(screen, (126, 34, 80), point, 2)
            bow.animation(dt, angle2)
            screen.blit(bow.image, (player.position_x, player.position_y))

            bow.draw_rectangle(screen, t, 50, height-power_bar.get_height()-9, number_arrow)

        portal_1.animate()
        portal_2.animate()
        screen.blit(portal_1.image, (portal_1.pos_x, portal_1.pos_y))
        screen.blit(portal_2.image, (portal_2.pos_x, portal_2.pos_y))
        #player.hit_x(tiles), player.hit_y(tiles)

        if possible1 and possible2 :
            if t_cooldown>=3:
                if player.rect_final.colliderect(portal_1.rect):
                    port=portal_2
                elif player.rect_final.colliderect(portal_2.rect):
                    port=portal_1
                if player.rect_final.colliderect(portal_1.rect) or player.rect_final.colliderect(portal_2.rect):
                    sono.play_tp_sound()
                    if port.state==-2:
                        player.speed_y = -player.speed_y
                        player.position_y = port.rect.y-70
                        player.position_x=port.rect.x+30


                    elif port.state==2:
                        player.position_y = port.rect.y+10
                        player.position_x = port.rect.x +30


                    elif port.state==-1:
                        player.speed_x = -player.speed_x
                        player.position_y = port.rect.y
                        player.position_x = port.rect.x +10


                    elif port.state == 1:
                        player.speed_x = -player.speed_x
                        player.position_y = port.rect.y
                        player.position_x = port.rect.x - player.rect_final.width-10


                    t_cooldown = 0
                    player.move_y(dt)
                    player.move_x(dt)

        else :
            if player.rect_final.colliderect(portal_1.rect) or player.rect_final.colliderect(portal_2.rect) :
                font = pygame.font.Font(None, 20)
                text_cant_play = font.render("Vous ne pouvez pas vous téléporter", True, (255, 255, 255))
                cant_play_rect = pygame.Rect(320, 490, 260, 35)
                pygame.draw.rect(screen, (0, 0, 0), cant_play_rect)
                screen.blit(text_cant_play, (335, 500))

        player.hit_something(tiles, screen)

        if player.rect_final.x >= 880: #au lieu d'un rect_end j'ai juste fais quand on arrive a droite de l'ecran ca sera plus fluide
            if level<5:
                return "game", level+1
            else:
                return "menu", level



        #pygame.draw.rect(screen, 'black', portal_1.rect)
        #pygame.draw.rect(screen, 'black', portal_2.rect)

        #pygame.draw.rect(screen, 'black', player.rect_final)
        #print(player.isgrounded)
        #print(player.speed_y)
        screen.blit(menu_button, menu_rect)
        pygame.display.flip()

