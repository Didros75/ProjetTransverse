    # Gère le menu (paramètres, bouton jouer etc...)

import pygame

def menu(screen, level, height, width):
    #pygame.draw.rect(screen, "black", pygame.Rect(0, 0, width, height))
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    screen.blit(background, (0, 0))
    font=pygame.font.Font(None, 60)
    text_play = font.render("Jouer", True, (255, 255, 255))
    play_rect = pygame.Rect(400, 250, 150, 50)
    pygame.draw.rect(screen, (0, 0, 0), play_rect)
    screen.blit(text_play, (400, 250))
    pygame.display.flip()
    in_game = True
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    in_game = False
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
                return False
    return True