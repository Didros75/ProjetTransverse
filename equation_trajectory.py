from math import*



#équation de trajectoire de la flèche et du portail, v0 est la vitesse initiale, theta est l'angle initial, t est le temps, g est la gravité

def trajectory(v0,theta,t,g, x, y) :
    Xposition = v0 * cos(theta) * t + x
    Yposition = (-1/2) * ((g*t)**2) + (v0+20) * sin(theta) * t + y
    coordinate = [Xposition, Yposition]
    return coordinate

def power(dt) : #dt est le temps que l'utilisateur reste cliqué sur le bouton gauche
    Pmin = 50 #puissance minimal
    CP = 2 #coefficient de proportionnalité de la puissance de la flèche
    P = CP * dt + Pmin
    return P

def angle(posiX_player,posiY_player,posiX_mouse,posiY_mouse): #calcul de l'angle de tir à l'aide de la souris
    delta_x  = posiX_mouse-posiX_player
    delta_y = posiY_player-posiY_mouse
    theta_radiant = atan2(delta_y, delta_x)
    return theta_radiant

def angle_arrow(v0,theta,t,g):
    Vx = v0 * cos(theta)
    Vy = -g*t + v0 * sin(theta)
    theta_radiant=atan2(Vy , Vx)
    return theta_radiant