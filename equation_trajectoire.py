from math import*

#équation de trajectoire de la flèche et du portail, v0 est la vitesse initiale, theta est l'angle initial, t est le temps, g est la gravité

def trajectory(v0,theta,t,g) :
    Xposition = v0 * cos(theta) * t
    Yposition = (-1/2) * ((g*t)**2) * v0 * sin(theta) * t
    coordonnee = [Xposition,Yposition]
    return coordonnee

def power(dt) : #dt est le delta de temps qui permet de savoir combien de temps l'utilisateur a gardé la souris cliqué pour la jauge de puissance
    Pmin = 50 #puissance minimal
    Pmax = 500 #puissance maximal
    CP = 2 #coefficient de proportionnalité de la puissance de la flèche
    P = CP * dt + Pmin
    if P > Pmax :
        P = Pmax
    return P