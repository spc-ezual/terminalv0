#exo 1
def rendu(nb):
    a_rendre=[0,0,0]
    while nb > 5:
        a_rendre[0]+=1
        nb-=5
    while nb > 2:
        a_rendre[1]+=1
        nb-=2
    while nb >= 1:
        a_rendre[2]+=1
        nb-=1
    return a_rendre

#erreur sujet au rendu de 89
#---------------------------------------------------
#exo 2
class Maillon :
    def __init__(self,v,suivant=None) :
        self.valeur = v
        self.suivant = suivant

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element , self.dernier_file)
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != null :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.valeur
            maillon.suivant = None
            return resultat
        return None 

f=File()
print(f.est_vide())
f.enfile(2)
print(f.affiche())
f.enfile(5)
f.enfile(8)
print(f.affiche())
f.defile()
f.defile()
f.defile()
print(f.est_vide())
