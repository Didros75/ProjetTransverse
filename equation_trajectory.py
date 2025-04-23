    # Centralise toutes les éuqations liées au trajectoires qu'on utlise

from math import *

def trajectory(v0,theta,t,g, x, y) :
    """
    Calcule la trajectoire que va suivre la flèche

    :param v0: vitesse initiale (float)
    :param theta: angle (float)
    :param t: temps (float)
    :param g: gravité (float)
    :param x: position en x (float)
    :param y: position en y (float)
    :return: un tuple de float représentant les coordonnées
    """
    Xposition = v0 * cos(theta) * t + x
    Yposition = (-1/2) * ((g*t)**2) + (v0+20) * sin(theta) * t + y
    coordinate = [Xposition, Yposition]
    return coordinate

def power(dt) :
    """
    Calcule la puissane actuelle de la flèche

    :param dt: le temps que l'utilisateur reste appuyé sur le bouton gauche (float)
    :return: La nouvelle puissance de la flèche (float)
    """
    Pmin = 50 #puissance minimal
    CP = 2 #coefficient de proportionnalité de la puissance de la flèche
    P = CP * dt + Pmin
    return P

def angle(posiX_player,posiY_player,posiX_mouse,posiY_mouse):
    """
    Calcul de l'angle de tir à l'aide de la souris

    :param posiX_player: La position en x du joueur (float)
    :param posiY_player: La position en y du joueur (float)
    :param posiX_mouse: La position en x de la souris (float)
    :param posiY_mouse: La position en y de la souris (float)
    :return: l'angle entre le joueur et l'endroit où le joueur veut tirer (float)
    """
    delta_x  = posiX_mouse-posiX_player
    delta_y = posiY_player-posiY_mouse
    theta_radiant = atan2(delta_y, delta_x)
    return theta_radiant

def angle_arrow(v0,theta,t,g):
    """
    Calcul de l'angle de la flèche

    :param v0: vitesse initiale (float)
    :param theta: angle (float)
    :param t: temps (float)
    :param g: gravité (float)
    :return: angle que suit la flèche
    """
    Vx = v0 * cos(theta)
    Vy = -g*t + v0 * sin(theta)
    theta_radiant=atan2(Vy , Vx)
    return theta_radiant

def trajectory_line(v0,theta,t,g, x, y) :
    """
    Calcule la trajectoire que va suivre l'aide (la trajectoire que va suivre la flèche)

    :param v0: vitesse initiale (float)
    :param theta: angle (float)
    :param t: temps (float)
    :param g: gravité (float)
    :param x: position en x (float)
    :param y: position en y (float)
    :return: un tuple de float représentant les coordonnées de l'aide
    """
    Xposition = v0 * cos(theta) * t + x
    Yposition = (1/2) * ((g*t)**2) + (v0+20) * sin(theta) * t + y
    coordinate = [Xposition, Yposition]
    return coordinate