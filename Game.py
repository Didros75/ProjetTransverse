import math
import pygame
import time
from Map import Create_map

from pygame import mouse

import equation_trajectoire
from Player import ThePlayer
from bow import Bow
from bow import Portals

pygame.init()
width=1000
height=700
screen = pygame.display.set_mode((width, height))

game = True
player = ThePlayer(10, 10)
bow=Bow()
map = Create_map("Map.csv", screen)

portal_blue=Portals((0, 0, 20, 50),"blue", screen)
portal_green=Portals((0, 0, 20, 50),"green", screen)
white=(255,255,255)
black=(0,0,0)
clock=pygame.time.Clock()
target_fps=60

sol_test=pygame.Rect(0, 250, 500, 50)
aiming=False
shoted=False
angle=0
t=0
while game:
    dt=clock.tick(60) * 0.001 * target_fps
    map.load_map()
    if player.rect.colliderect(sol_test):
        player.collisions([sol_test])
    else:
        player.isgrounded=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
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
                aiming=True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1 and shoted==False:

                angle=equation_trajectoire.angle(player.position_x, player.position_y, mouse.get_pos()[0], mouse.get_pos()[1])
                t=0
                print(angle)
                shoted=True
                aiming=False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.RIGHT=False
            if event.key == pygame.K_q:
                player.LEFT=False
            if event.key == pygame.K_SPACE:
                player.isjumping=False


    if aiming:
        bow.animation(dt)
        screen.blit(bow.image, (player.position_x,player.position_y))
    if shoted:
        pygame.draw.rect(screen, black, (bow.shot(t, 200, angle, player.position_x, -player.position_y)[0], -bow.shot(t, 200, angle, player.position_x, -player.position_y)[1], 50, 50))
        if -bow.shot(t, 200, angle, player.position_x, -player.position_y)[1]>height:
            portal_blue.state=True
            shoted=False

    if portal_blue.state==True:
        portal_blue.apparition(player.position_x, player.position_y)
    player.animate()
    pygame.draw.rect(screen, black, sol_test)
    player.move_y(dt)
    player.move_x(dt)
    player.draw(screen)
    t+=0.1


    pygame.display.flip()