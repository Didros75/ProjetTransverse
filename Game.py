import math
import pygame
import time
from Map import Create_map

from pygame import mouse

import equation_trajectory
from Player import ThePlayer
from bow import Bow, Arrow
from Portal import portal

power = 0
pygame.init()
width=900
height=600
screen = pygame.display.set_mode((width, height))

game = True
player = ThePlayer(10, 10)
bow=Bow()
portal_1=portal(100, 180)
portal_2=portal(550, 220)
map = Create_map("Map.csv", screen)


white=(255,255,255)
black=(0,0,0)
clock=pygame.time.Clock()
target_fps=60
power_bar=pygame.image.load("assets/power_bar.png")
power_bar=pygame.transform.scale(power_bar,(225,75))
isgrounded=False

aiming=False
shoted=False
angle=0
angle2=0
t=0
while game:
    dt=clock.tick(60) * 0.001 * target_fps

    tiles = map.load_map()
    player.hit_x(tiles), player.hit_y(tiles)


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
                    bow.state=-bow.state
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button==1:

                if shoted==False:
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



    if shoted :
        position = player.get_position()
        arrow = Arrow(position)
        if power>=15:
            power=15
        arrow.shot(t, power*25, angle, px, -py)
        arrow.show(screen)
        shoted = arrow.collision(tiles)

    """if portal_blue.state==True:
        portal_blue.apparition(player.position_x, player.position_y)"""
    player.animate(angle2)
    player.move_y(dt)
    player.move_x(dt)
    player.draw(screen)
    t+=0.1
    player.rectx.left=player.rect.left-5


    screen.blit(power_bar, (0, height-power_bar.get_height()))

    if aiming:
        bow.animation(dt, angle2)
        screen.blit(bow.image, (player.position_x, player.position_y))
        bow.draw_rectangle(screen, t, 65, height-power_bar.get_height()+27)

    if bow.state==1:
        screen.blit(pygame.transform.scale(pygame.image.load("assets/arrow_picto.png"), (30, 30)), (21, height-power_bar.get_height()+21))
    elif bow.state==-1:
        screen.blit(pygame.transform.scale(pygame.image.load("assets/portal_1.png"), (35, 35)),
                    (20, height - power_bar.get_height() + 18))

    portal_1.animate()
    portal_2.animate()
    screen.blit(portal_1.image, (portal_1.pos_x, portal_1.pos_y))
    screen.blit(portal_2.image, (portal_2.pos_x, portal_2.pos_y))
    portal_1.state=-1
    portal_2.state=-2

    pygame.display.flip()