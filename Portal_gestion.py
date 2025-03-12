import pygame


def gestion(player_speedx, player_speedy, portal1_pos, portal2_pos, portal1_state, portal2_state):
    if portal1_state == portal2_state:
        if portal1_state == 1 or portal1_state == -1:
            return portal2_pos, -player_speedx, player_speedy
        if portal1_state == 2 or portal1_state == -2:
            return portal2_pos, player_speedx, -player_speedy
    elif portal1_state != portal2_state:
        if portal1_state < 0 :
            return portal2_pos, -player_speedy, player_speedy-5
        else:
            if portal1_state > 0:
                return portal2_pos, player_speedy, player_speedx