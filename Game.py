import math
import pygame
import time
from Player import ThePlayer

pygame.init()

screen = pygame.display.set_mode((1000, 700))

game = True
player = ThePlayer(10, 10)
white=(255,255,255)
black=(0,0,0)
clock=pygame.time.Clock()
target_fps=60
sol_test=pygame.Rect(0, 250, 500, 50)
while game:
    dt=clock.tick(60) * 0.001 * target_fps
    screen.fill(white)
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.RIGHT=False
            if event.key == pygame.K_q:
                player.LEFT=False
            if event.key == pygame.K_SPACE:
                player.isjumping=False




    player.animate()
    pygame.draw.rect(screen, black, sol_test)
    player.move_y(dt)
    player.move_x(dt)
    player.draw(screen)

    pygame.display.flip()