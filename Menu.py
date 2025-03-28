import pygame

def menu(screen):
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

    return True