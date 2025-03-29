import pygame
from sound_manager import SoundManager
def settings(screen, height, width, sound, help):
    sono=SoundManager(False)
    button_height, button_width = 75, 187
    litle_button=50
    title_font = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 40)

    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_height, button_height))
    exit_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_height, button_height))
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (400, 300))

    x_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (litle_button, litle_button))
    y_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/Y.png'), (litle_button, litle_button))

    text_parametres = title_font.render("Settings :", True, (255, 255, 255))
    text_son=font.render("Sound : ", True, (255, 255, 255))
    text_aide=font.render("Help : ", True, (255, 255, 255))

    menu_rect=pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    exit_rect = pygame.Rect(width-button_height-35, 35, exit_button.get_width(), exit_button.get_height())

    son_x_rect=pygame.Rect(width/2+10, 210, x_button.get_width(), x_button.get_height())
    son_y_rect=pygame.Rect(width/2-y_button.get_width()-10, 210, y_button.get_width(), y_button.get_height())

    aide_x_rect=pygame.Rect(width/2+10, 260, x_button.get_width(), x_button.get_height())
    aide_y_rect=pygame.Rect(width/2-y_button.get_width()-10, 260, y_button.get_width(), y_button.get_height())

    screen.blit(background, (0, 0))

    screen.blit(board, (width/2-200, 150))
    screen.blit(text_parametres, (width/2-170, 170))
    screen.blit(text_son, (width/2-170, 220))
    screen.blit(text_aide, (width/2-170, 270))
    screen.blit(x_button, son_x_rect)
    screen.blit(y_button, son_y_rect)
    screen.blit(x_button, aide_x_rect)
    screen.blit(y_button, aide_y_rect)
    screen.blit(menu_button, menu_rect)
    screen.blit(exit_button, exit_rect)


    pygame.display.flip()

    in_game = True
    while in_game:
        if sound:
            pygame.draw.rect(screen, (27, 20, 100), (son_x_rect[0]+12, son_x_rect[1]+12, son_x_rect[2]-22, son_x_rect[3]-22))
            screen.blit(y_button, son_y_rect)
        else:
            pygame.draw.rect(screen, (27, 20, 100), (son_y_rect[0]+12, son_y_rect[1]+12, son_y_rect[2]-22, son_y_rect[3]-22))
            screen.blit(x_button, son_x_rect)
            
        if help:
            pygame.draw.rect(screen, (27, 20, 100), (aide_x_rect[0]+12, aide_x_rect[1]+12, aide_x_rect[2]-22, aide_x_rect[3]-22))
            screen.blit(y_button, aide_y_rect)
        else:
            pygame.draw.rect(screen, (27, 20, 100), (aide_y_rect[0]+12, aide_y_rect[1]+12, aide_y_rect[2]-22, aide_y_rect[3]-22))
            screen.blit(x_button, aide_x_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "menu", sound, help

                if son_x_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    sound=False
                if son_y_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    sound=True
                    
                if aide_x_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    help=False
                if aide_y_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    help=True


                if exit_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.quit()
                    return False

            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        pygame.display.flip()
