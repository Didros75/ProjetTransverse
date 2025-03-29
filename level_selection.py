import pygame
from sound_manager import SoundManager
def Level_selection(screen, height, width):
    button_dim=75
    sono = SoundManager(False)
    font = pygame.font.Font(None, 40)
    background = pygame.transform.scale(pygame.image.load("assets/Menu_image.jpg"), (width, height))
    menu_button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Home.png"), (button_dim, button_dim))
    menu_rect=pygame.Rect(35, 35, menu_button.get_width(), menu_button.get_height())
    board=pygame.transform.scale(pygame.image.load("assets/meni_menu/rectangle_long.png"), (500, 300))
    button=pygame.transform.scale(pygame.image.load("assets/meni_menu/Vide.png"), (button_dim-10, button_dim-10))
    chapter1_text=font.render("Chapter 1", True, (255, 255, 255))

    screen.blit(background, (0, 0))
    screen.blit(board, (width/2-250, 150))
    screen.blit(chapter1_text,(width/2-220, 180))
    screen.blit(menu_button, menu_rect)

    # la j'ai crée 5 bouttons avec chacun un rect et quand on clique sur un ca renvoie game (pour dire de lancer le jeu) et le numero du level selectionné, directement dans main, qui va mettre window a 'game' et lancer Game.game avec le level selectionné comme parametre

    buttons = []
    for i in range(5): #la j'ai crée 5 bouttons avec chacun un rect et quand on clique sur un ca renvoie game (pour dire de lancer le jeu) et le numero du level selectionné, directement dans main, qui va mettre window a 'game' et lancer Game.game avec le level selectionné comme parametre
        rect = pygame.Rect(240 + i * 85, 220, button_dim-10, button_dim-10)
        buttons.append((rect, str(i + 1)))

    for rect, number in buttons:
        screen.blit(button, rect)
        text = font.render(number, True, (255, 255, 255))
        screen.blit(text, (rect.x + 25, rect.y + 20))

    pygame.display.flip()
    in_game = True
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(pygame.mouse.get_pos()):
                    sono.play_button_sound()
                    return "menu", 0
                for rect, number in buttons:
                    if rect.collidepoint(event.pos):
                        sono.play_button_sound()
                        return "game", int(number)


            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()