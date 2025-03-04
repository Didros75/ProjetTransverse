from math import*

import equation_trajectoire


#équation de trajectoire de la flèche et du portail, v0 est la vitesse initiale, theta est l'angle initial, t est le temps, g est la gravité

def trajectory(v0,theta,t,g, x, y) :
    Xposition = v0 * cos(theta) * t + x
    Yposition = (-1/2) * ((g*t)**2) + (v0+20) * sin(theta) * t + y
    coordonnee = [Xposition, Yposition]
    return coordonnee

def power(dt) : #dt est le temps que l'utilisateur reste cliqué sur le bouton gauche
    Pmin = 50 #puissance minimal
    CP = 2 #coefficient de proportionnalité de la puissance de la flèche
    P = CP * dt + Pmin
    return P

def angle(posiX_joueur,posiY_joueur,posiX_souris,posiY_souris): #calcul de l'angle de tir à l'aide de la souris
    delta_x  = posiX_souris-posiX_joueur
    delta_y = posiY_joueur-posiY_souris
    thetarad = atan2(delta_y, delta_x)
    return thetarad

def inclinaison_fleche(v0,theta,t,g):
    Vx = v0 * cos(theta)
    Vy = -g*t + v0 * sin(theta)
    inclinaison_rad=atan2(Vy , Vx)
    return inclinaison_rad