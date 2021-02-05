#Créé par Marcus
#exo 1
def rechercheMinMax(tableau):
    if len(tableau)==0:return {'min':None,'max':None}
    max,min=tableau[0],tableau[0]
    for j in tableau:
        if j < min:
            min=j
        if j > max :
            max = j
    return {'min':min,'max':max}
#--------------------------------------------
#exo 2 
from random import shuffle

class carte :
    def __init__ (self,c,v):
        self.couleur=c
        self.valeur=v
    def getnom(self):
        if self.valeur>1 and self.valeur<11:return self.valeur
        elif self.valeur==11:return "Valet"
        elif self.valeur==12:return"Dame"
        elif self.valeur==13:return "Roi"
        else :return "As"
    def getcouleur(self): return ["pique","coeur","carreau","trefle"][self.couleur]

class paquetdecarte:
    def __init__(self): self.contenue=[]
    def remplir(self):
        for j in range (4):
            for i in range (1,14):
                self.contenue.append(carte(j,i))
#    def melangerLesCarte(self):
#        shuffle(self.contenue)


    def getcarte(self,position):return self.contenue[position-1]


# Faute du sujet la 20éme carte est le 7 coeur et non le 6 
# car l'on commence par la 1ere carte et non la carte n°0
"""
As  de  pique  n° 1
2  de  pique  n° 2
3  de  pique  n° 3
4  de  pique  n° 4
5  de  pique  n° 5
6  de  pique  n° 6
7  de  pique  n° 7
8  de  pique  n° 8
9  de  pique  n° 9
10  de  pique  n° 10
Valet  de  pique  n° 11
Dame  de  pique  n° 12
Roi  de  pique  n° 13
As  de  coeur  n° 14
2  de  coeur  n° 15
3  de  coeur  n° 16
4  de  coeur  n° 17
5  de  coeur  n° 18
6  de  coeur  n° 19
7  de  coeur  n° 20
8  de  coeur  n° 21
9  de  coeur  n° 22
10  de  coeur  n° 23
Valet  de  coeur  n° 24
Dame  de  coeur  n° 25
Roi  de  coeur  n° 26
As  de  carreau  n° 27
2  de  carreau  n° 28
3  de  carreau  n° 29
4  de  carreau  n° 30
5  de  carreau  n° 31
6  de  carreau  n° 32
7  de  carreau  n° 33
8  de  carreau  n° 34
9  de  carreau  n° 35
10  de  carreau  n° 36
Valet  de  carreau  n° 37
Dame  de  carreau  n° 38
Roi  de  carreau  n° 39
As  de  trefle  n° 40
2  de  trefle  n° 41
3  de  trefle  n° 42
4  de  trefle  n° 43
5  de  trefle  n° 44
6  de  trefle  n° 45
7  de  trefle  n° 46
8  de  trefle  n° 47
9  de  trefle  n° 48
10  de  trefle  n° 49
Valet  de  trefle  n° 50
Dame  de  trefle  n° 51
Roi  de  trefle  n° 52
"""