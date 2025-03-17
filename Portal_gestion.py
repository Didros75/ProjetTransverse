import pygame


def gestion(player_speedx, player_speedy, player_y, portal2_pos, portal1_state, portal2_state):
        if portal1_state == -2:
            return (portal2_pos[0],portal2_pos[1]), player_speedx, -(player_speedy-1), player_y-(10+2*player_speedy)
        elif portal2_state == 2:
            return (portal2_pos[0],portal2_pos[1]), player_speedx, player_speedy, player_y+10
        elif portal2_state == 1:
            return (portal2_pos[0],portal2_pos[1]), player_speedx, player_speedy, player_y
        elif portal2_state == -1:
            return (portal2_pos[0],portal2_pos[1]), -player_speedx, player_speedy, player_y