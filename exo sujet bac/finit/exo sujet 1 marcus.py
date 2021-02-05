#exo 1
def recherche(liste ,element):
    nb=liste.count(element)
    if nb < 1:
        return len (liste)
    elif nb==1:
        return liste.index(element)
    else:
        indice=-1
        while liste[indice]!=element:
            indice-=1
        return len(liste)+indice
            

#---------------------------------------------------------------------------
#exo 2 
from math import sqrt

def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist =distance(tab[0], depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart)<min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point
