import pygame
from sound_manager import SoundManager

def skin(screen, height, width, skin_num=0):
    sono = SoundManager(False)
    button_size=75
    skin=int(skin_num)
    list_name=["Dark archer", "Crimson sniper", "Robin Hood", "Solar shooter"]
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (370, 350))
    skin_1= [pygame.image.load(f"assets/0/l0_sprite_{i}.png") for i in range(1, 5)]
    skin_2= [pygame.image.load(f"assets/1/l0_sprite_{i}.png") for i in range(1, 5)] #90  sur https://pinetools.com/adjust-hue-image
    skin_3=[pygame.image.load(f"assets/2/l0_sprite_{i}.png") for i in range(1, 5)] #200
    skin_4 = [pygame.image.load(f"assets/3/l0_sprite_{i}.png") for i in range(1, 5)]

    skins=[skin_1, skin_2, skin_3, skin_4]
    menu_button = pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_size, button_size))
    exit_button = pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_size, button_size))
    right_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/right.png"), (button_size, button_size))
    left_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/left.png"), (button_size, button_size))
    font = pygame.font.Font(None, 50)
    little_font = pygame.font.Font(None, 40)
    skin_text=font.render("Skin :", 1, (255, 255, 255))

    menu_rect = pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    exit_rect = pygame.Rect(width - button_size - 35, 35, exit_button.get_width(), exit_button.get_height())
    right_rect=pygame.Rect(width/2+130, height/2-10, right_button.get_width(), right_button.get_height())
    left_rect=pygame.Rect(width/2-130-left_button.get_width(), height/2-10, right_button.get_width(), right_button.get_height())

    screen.blit(background, (0, 0))

    screen.blit(menu_button, menu_rect)
    screen.blit(exit_button, exit_rect)


    index=0
    in_game = True
    while in_game:
        skin_name=little_font.render(list_name[skin], 1, (255, 255, 255))
        screen.blit(board, (width / 2 - board.get_width()/2, 150))
        screen.blit(skin_text, (width / 2 - 45, 190))
        screen.blit(skin_name, (width / 2 - len(list_name[skin])*7, 410))
        screen.blit(right_button, right_rect)
        screen.blit(left_button, left_rect)

        screen.blit(skins[skin][int(index)], (width/2-skins[skin][int(index)].get_width()/2, height-skins[skin][int(index)].get_height()-200))
        index += 0.03
        if index > len(skins[skin]):
            index = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    in_game = False
                    pygame.quit()
                if menu_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()

                    return "menu", str(skin)

                if right_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    if skin == len(skins)-1:
                        skin = 0
                    else:
                        skin += 1
                if left_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    if skin == 0:
                        skin = len(skins)-1
                    else:
                        skin -= 1
        pygame.display.flip()