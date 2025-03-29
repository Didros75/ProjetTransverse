    # Gère les intéractions du jeu complet

import Game
import Menu
import pygame

def begin_game() :
    pygame.init()
    world = 0
    level = 0
    width = 900
    height = 600
    screen = pygame.display.set_mode((width, height))

    game = Menu.menu(screen, level, height, width)
    continue_to_play = Game.game(level, game, screen, height, width, world)
    while continue_to_play == 1 :
        level += 1
        game = Menu.menu(screen, level, height, width)
        continue_to_play = Game.game(level, game, screen, height, width, world)

if __name__ == "__main__" :
    begin_game()