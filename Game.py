import pygame
from Map import Create_map
from pygame import mouse
import Menu
import equation_trajectory
from Player import ThePlayer
from bow import Bow, Arrow
from Portal import Portal

power = 0
pygame.init()
width=900
height=600
screen = pygame.display.set_mode((width, height))

game = Menu.menu(screen)
player = ThePlayer(0, 0)
bow=Bow()
portal_1=Portal(-75, -75)
portal_2=Portal(-75, -75)
map = Create_map("Maps/map2.csv", screen)

white=(255,255,255)
black=(0,0,0)

clock = pygame.time.Clock()
target_fps=60
power_bar=pygame.image.load("assets/power_bar.png")
power_bar=pygame.transform.scale(power_bar,(225,75))
# isgrounded=False

aiming=False
shoted=False
angle=0
angle2=0
t=0
t_cooldown=0
number_arrows = 0

while game:
    dt=clock.tick(60) * 0.001 * target_fps
    tiles = map.load_map()

    if player.death() :
        player = ThePlayer(0, 0)

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

    # Fonction pour changer les flèches dans la classe arrow possible ???

    if collision != 0 :

        position_portal = arrow.position_portal(collision)

        number_arrows += 1
        if number_arrows > 1:
            number_arrows = 0

        if number_arrows == 1 :
            portal_2.state = arrow.portal_state
            new_position = portal_2.change_position(collision, tiles, position_portal, arrow.portal_state)
            portal_2.pos_x, portal_2.pos_y = new_position[0], new_position[1]
        else :
            portal_1.state = arrow.portal_state
            new_position = portal_1.change_position(collision, tiles, position_portal, arrow.portal_state)
            portal_1.pos_x, portal_1.pos_y = new_position[0], new_position[1]

    player.animate(angle2)
    player.move_y(dt)
    player.move_x(dt)
    player.draw(screen)
    t+=0.1
    t_cooldown+=0.1

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
    chargement=True

    if t_cooldown>=4:
        if player.rect.colliderect(portal_1.rect) :

            if portal_2.state==-2:
                player.speed_y = -(player.speed_y - 2)
                player.position_y = portal_2.rect.y - 70
                player.position_x=portal_2.rect.x+30
                player.rect.y = portal_2.rect.y - 70
                player.rect.x = portal_2.rect.x + 30

            elif portal_2.state==2:
                player.speed_y = -(player.speed_y - 2)
                player.position_y = portal_2.rect.y + 50
                player.position_x = portal_2.rect.x + 30
                player.rect.y = portal_2.rect.y - 50
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

            if portal_1.state==-2:
                player.speed_y = -(player.speed_y-2)

                player.position_y = portal_1.rect.y-70
                player.position_x = portal_1.rect.x+30
                player.rect.y= portal_1.rect.y-70
                player.rect.x = portal_1.rect.x +30


            elif portal_1.state==2:

                player.speed_y = -(player.speed_y - 2)
                player.position_y = portal_1.rect.y + 50
                player.position_x = portal_1.rect.x + 30
                player.rect.y = portal_1.rect.y - 50
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


    player.hit_x(tiles), player.hit_y(tiles)
    #pygame.draw.rect(screen, 'black', player.rect)
    #pygame.draw.rect(screen, 'black', player.rectx)


    pygame.display.flip()