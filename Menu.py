    # Gère le menu (paramètres, bouton jouer etc...)
from sound_manager import SoundManager
import pygame

def menu(screen, height, width):
    sono = SoundManager(False)
    button_height, button_width = 75, 187
    button=pygame.transform.scale(pygame.image.load('assets/meni_menu/bouton.png'), (button_width, button_height))
    settings_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/settings.png'), (button_height, button_height-3))
    exit_button=pygame.transform.scale(pygame.image.load('assets/meni_menu/X.png'), (button_height, button_height-3))

    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    screen.blit(background, (0, 0))
    font=pygame.font.Font(None, 60)
    text_play = font.render("Play", True, (255, 255, 255))

    play_rect = pygame.Rect(width/2-button_width/2, 270, button.get_width(), button.get_height())
    settings_rect = pygame.Rect(width/2-button_height-10, 350, settings_button.get_width(), settings_button.get_height())
    exit_rect = pygame.Rect(width/2+10, 350, exit_button.get_width(), exit_button.get_height())

    screen.blit(button, play_rect)
    screen.blit(settings_button, settings_rect)
    screen.blit(exit_button, exit_rect)
    screen.blit(text_play, (play_rect[0]+50,play_rect[1]+18 ,0, 0))


    pygame.display.flip()
    in_game = True
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "level"
                if settings_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    return "settings"
                if exit_rect.collidepoint(event.pos):
                    sono.play_button_sound()
                    pygame.quit()
                    return False


            if event.type == pygame.QUIT:
                pygame.quit()
                return False

