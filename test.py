import math
import pygame

pygame.init()

ecran = pygame.display.set_mode((800, 800))

continuer = True


sol_rect=pygame.Rect(0, 250, 500, 50)
blanc=(250, 250, 250)
noir=(0, 0, 0)
vitesse_y=0
vitesse_x=0
gravité=0.5
sol_resistance=0.1
player_rect=pygame.Rect(50, 50, 50, 50)
balle_circle=pygame.Rect(50, 50, 20, 20)
angle=0
droite=False
gauche=False
tenu=True
isgrounded=False

while continuer:
    ecran.fill(blanc)
    pygame.draw.rect(ecran, noir, sol_rect)
    pygame.draw.rect(ecran, noir, player_rect)
    pygame.draw.circle(ecran, noir, (balle_circle[0], balle_circle[1]), 10)

    if tenu==True:
        balle_circle.y=player_rect.y
        balle_circle.x=player_rect.x

    player_rect.x += vitesse_x



    vitesse_y+=gravité
    player_rect.y+=vitesse_y
    if player_rect.colliderect(sol_rect):
        isgrounded=True
        player_rect.y=sol_rect.top-player_rect.height
        vitesse_y=0
    else:
        isgrounded=False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
            if event.key == pygame.K_SPACE and isgrounded:
                vitesse_y=-12
            if event.key == pygame.K_RIGHT:
                droite=True
            if event.key == pygame.K_LEFT:
                gauche=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                droite=False
            elif event.key == pygame.K_LEFT:
                gauche=False
    if droite:
        if vitesse_x<4:
            vitesse_x+=1

    if gauche:
        if vitesse_x > -4:
            vitesse_x-=1


    if vitesse_x > 0:
        vitesse_x-=sol_resistance
    elif vitesse_x < 0:
        vitesse_x+=sol_resistance


    if player_rect.y>800:
        player_rect.y=0

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()