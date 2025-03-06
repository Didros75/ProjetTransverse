import math
import pygame
import time
from Map import Create_map

from pygame import mouse

import equation_trajectory
from Player import ThePlayer
from bow import Bow, Arrow
from bow import Portals
#from test import isgrounded
power = 0
pygame.init()
width=900
height=600
screen = pygame.display.set_mode((width, height))

game = True
player = ThePlayer(10, 10)
bow=Bow()
map = Create_map("Map.csv", screen)

# portal_blue=Portals((0, 0, 20, 50),"blue", screen)
portal_green=Portals((0, 0, 20, 50),"green", screen)
white=(255,255,255)
black=(0,0,0)
clock=pygame.time.Clock()
target_fps=60

isgrounded=False

#sol_test=pygame.Rect(0, 100, 500, 50)
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
            if player.aiming==False:
                if event.key == pygame.K_d:
                    player.facingLeft=False
                    player.RIGHT=True
                if event.key == pygame.K_q:
                    player.facingLeft=True
                    player.LEFT=True
                if event.key == pygame.K_SPACE:
                    if player.isgrounded:
                        player.jump()
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

    if aiming:
        bow.animation(dt, angle2)
        screen.blit(bow.image, (player.position_x,player.position_y))


    pygame.display.flip()