from math import*

#trajectory equation of arrow and portal, v0 is initial speed, theta is the initial angle, t is time, g is the gravity

def trajectoire(v0,theta,t,g) :
    Xposition = v0 * cos(theta) * t
    Yposition = (-1/2) * ((g*t)^2) * v0 * sin(theta) * t
    coordonnee = []
    coordonnee[0] = Xposition
    coordonnee[1] = Yposition
    return coordonnee

def power(dt) : #dt is the time that us
    Pmin = 50 #minimal power
    CP = 2 #coefficient of proportionnality of the power from the arrow
    P = CP * dt + Pmin
    return P
