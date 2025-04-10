"""import math
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
saut=-10
position=0
sol_resistance=0.1
player_rect=pygame.Rect(50, 50, 30, 30)
balle_circle=pygame.Rect(50, 50, 10, 10)
angle=0
vitesse_actuelle=0
vitesse_actuelle_x=0
temps=0
droite=False
gauche=False
tenu=True
isgrounded=False
ralenti = False
clic=False

while continuer:
    ecran.fill(blanc)
    pygame.draw.rect(ecran, noir, sol_rect)
    pygame.draw.rect(ecran, noir, player_rect)
    pygame.draw.circle(ecran, noir, (balle_circle[0], balle_circle[1]), 10)

    if tenu==True:
        balle_circle.y=player_rect.y
        balle_circle.x=player_rect.x

    player_rect.x += vitesse_x

    if not ralenti:
        player_rect.x += vitesse_x
        vitesse_y+=gravité
        vitesse_actuelle = vitesse_y
    else:
        vitesse_x=vitesse_actuelle_x/20
        vitesse_y=vitesse_actuelle/20

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
                vitesse_y=saut
            if event.key == pygame.K_RIGHT:
                droite=True
            if event.key == pygame.K_LEFT:
                gauche=True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                clic=True
                ralenti=False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                clic=False
                ralenti=False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                droite=False
            elif event.key == pygame.K_LEFT:
                gauche=False
    if droite:
        if vitesse_x<2:
            vitesse_x+=0.7

    if gauche:
        if vitesse_x > -2:
            vitesse_x-=0.7

    if clic:
        position = pygame.mouse.get_pos()
        angle=math.atan((position[0]-player_rect[0])/(position[1]-player_rect[1]))
        angle=math.degrees(angle)
        print(angle)

    if vitesse_x > 0:
        vitesse_x-=sol_resistance
    elif vitesse_x < 0:
        vitesse_x+=sol_resistance


    if player_rect.y>800:
        player_rect.y=0

    pygame.display.flip()
    pygame.time.delay(10)
    temps+=1
    if temps%100==0:
        print(temps/100)

pygame.quit()"""