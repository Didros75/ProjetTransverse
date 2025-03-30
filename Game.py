    # Gère les intéractions d'une partie (un niveau)

import pygame
from Map import Create_map
from pygame import mouse
import Menu
import equation_trajectory
from Player import ThePlayer
from bow import Bow, Arrow
from Portal import Portal
from sound_manager import SoundManager
import time

def game(level, game, screen, height, width, world, help) :
    sono=SoundManager(False)
    power = 0
    #pygame.init()
    #width=900
    #height=600
    #screen = pygame.display.set_mode((width, height))

    #game = Menu.menu(screen, level)
    bow = Bow()

        # Définition des différentes positions de départ et d'arrivé

    start_position = [(40, 340), (0, 0), (0, 0), (0, 0)]
    end_position = [(860, 400), (860, 400), (860, 400), (860, 400)]
    menu_button = pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (50, 50))
    menu_rect = pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    rect_end = pygame.Rect(end_position[level][0], end_position[level][1], 10, 50)
    player = ThePlayer(start_position[level][0], start_position[level][1])

    portal_1=Portal(-75, -75, 1)
    portal_2=Portal(-75, -75, 2)

    if level == 0 :
            map = Create_map("Maps/map_tutorial.csv", screen)
    elif level == 1 :
            map = Create_map("Maps/map1.csv", screen)
    elif level == 2 :
            map = Create_map("Maps/map2.csv", screen)
    elif level == 3 :
            map = Create_map("Maps/map3.csv", screen)

    clock = pygame.time.Clock()
    target_fps=60
    power_bar=pygame.image.load("assets/chargin_bar.png")

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

    if world == 0 :
        background=pygame.image.load("assets/fond2.jpg")
    elif world == 1 :
        background = pygame.image.load("assets/fond.jpg")
    elif world == 2 :
        background = pygame.image.load("assets/fond1.png")

    background = pygame.transform.scale(background, (width, height))

    while game:
        dt=clock.tick(60) * 0.001 * target_fps
        tiles = map.load_map(background)

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

                    angle = equation_trajectory.angle(player.position_x+20, player.position_y+30, mouse.get_pos()[0], mouse.get_pos()[1])
                    power=t
                    t = 0
                    px = player.position_x
                    py = player.position_y
                    shoted=True
                    player.aiming=False
                    aiming=False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.RIGHT=False
                if event.key == pygame.K_q:
                    player.LEFT=False
                if event.key == pygame.K_SPACE:
                    player.isjumping=False

        angle2 = equation_trajectory.angle(player.position_x+20, player.position_y+30, mouse.get_pos()[0],
                                            mouse.get_pos()[1])

        collision = 0

        if shoted :
            position = player.get_position()
            arrow = Arrow(position)
            if power>=15:
                power=15
            arrow.shot(t, power*25, angle, px, -py)

            arrow.show(screen)
            shoted, collision = arrow.collision(tiles, height, width)[0], arrow.collision(tiles, height, width)[1]

        if collision != 0 :

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

        screen.blit(power_bar, (20, height-power_bar.get_height()-20))
        list_point=[]
        if aiming:
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
            bow.draw_rectangle(screen, t, 24, height-power_bar.get_height()-16, number_arrow)

        if bow.state==1:
            screen.blit(pygame.transform.scale(pygame.image.load("assets/arrow_picto.png"), (30, 30)), (21, height-power_bar.get_height()+21))
        elif bow.state==-1:
            screen.blit(pygame.transform.scale(pygame.image.load("assets/portal_1.png"), (35, 35)),
                        (20, height - power_bar.get_height() + 18))

        portal_1.animate()
        portal_2.animate()
        screen.blit(portal_1.image, (portal_1.pos_x, portal_1.pos_y))
        screen.blit(portal_2.image, (portal_2.pos_x, portal_2.pos_y))
        #player.hit_x(tiles), player.hit_y(tiles)

        if possible1 and possible2 :

            if t_cooldown>=4:
                if player.rect.colliderect(portal_1.rect) :
                    sono.play_tp_sound()
                    if portal_2.state==-2:
                        player.speed_y = -(player.speed_y - 2)
                        player.position_y = portal_2.rect.y - 70
                        player.position_x=portal_2.rect.x+30
                        player.rect.y = portal_2.rect.y - 70
                        player.rect.x = portal_2.rect.x + 30

                    elif portal_2.state==2:

                        player.position_y = portal_2.rect.y + 30
                        player.position_x = portal_2.rect.x + 30
                        player.rect.y = portal_2.rect.y + 30
                        player.rect.x = portal_2.rect.x + 30

                    elif portal_2.state==-1:
                        player.speed_x = -(player.speed_x - 2)
                        player.position_y = portal_2.rect.y + 30
                        player.position_x = portal_2.rect.x - 30
                        player.rect.y = portal_2.rect.y - 30
                        player.rect.x = portal_2.rect.x - 30

                    elif portal_2.state == 1:
                        player.speed_x = -(player.speed_x - 2)
                        player.position_y = portal_2.rect.y + 30
                        player.position_x = portal_2.rect.x + 30
                        player.rect.y = portal_2.rect.y - 30
                        player.rect.x = portal_2.rect.x + 30

                    player.rectx.y = player.rect.y - 5
                    player.rectx.x = player.rect.x - 5
                    t_cooldown = 0

                elif player.rect.colliderect(portal_2.rect):
                    sono.play_tp_sound()

                    if portal_1.state==-2:
                        player.speed_y = -(player.speed_y-2)
                        player.position_y = portal_1.rect.y-70
                        player.position_x = portal_1.rect.x+30
                        player.rect.y= portal_1.rect.y-70
                        player.rect.x = portal_1.rect.x +30

                    elif portal_1.state==2:

                        player.position_y = portal_1.rect.y + 30
                        player.position_x = portal_1.rect.x + 30
                        player.rect.y = portal_1.rect.y +30
                        player.rect.x = portal_1.rect.x + 30

                    elif portal_1.state==-1:
                        player.speed_x = -(player.speed_x - 2)
                        player.position_y = portal_1.rect.y + 30
                        player.position_x = portal_1.rect.x - 30
                        player.rect.y = portal_1.rect.y - 30
                        player.rect.x = portal_1.rect.x - 30

                    elif portal_1.state == 1:
                        player.speed_x = -(player.speed_x - 2)
                        player.position_y = portal_1.rect.y + 30
                        player.position_x = portal_1.rect.x + 30
                        player.rect.y = portal_1.rect.y - 30
                        player.rect.x = portal_1.rect.x + 30

                    player.rectx.y = player.rect.y - 5
                    player.rectx.x = player.rect.x - 5
                    t_cooldown = 0
        else :
            if player.rect.colliderect(portal_1.rect) or player.rect.colliderect(portal_2.rect) :
                font = pygame.font.Font(None, 20)
                text_cant_play = font.render("Vous ne pouvez pas vous téléporter", True, (255, 255, 255))
                cant_play_rect = pygame.Rect(320, 490, 260, 35)
                pygame.draw.rect(screen, (0, 0, 0), cant_play_rect)
                screen.blit(text_cant_play, (335, 500))

        player.hit_x(tiles), player.hit_y(tiles)
        if rect_end.colliderect(player.rect) :
            time.sleep(0.2)
            return "game", level+1

        #pygame.draw.rect(screen, 'black', portal_1.rect)
        #pygame.draw.rect(screen, 'black', portal_2.rect)

        #pygame.draw.rect(screen, 'black', player.rect)
        pygame.draw.rect(screen, 'black', rect_end)
        #print(player.isgrounded)
        #print(player.speed_y)
        screen.blit(menu_button, menu_rect)
        pygame.display.flip()

