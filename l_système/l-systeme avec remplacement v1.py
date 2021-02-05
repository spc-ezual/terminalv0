from math import cos
def calcule_courbe_de_Weierstrass(x):
    somme=cos(x)
    for i in range(1,500):
        somme= somme+ (1/(2**i))*cos(x*(4**i))
    print(somme)

def wie(x):
    return cos(x)+(1)/(2) *cos(4*x)+(1)/(4)* cos(16*x)+(1)/(8)* cos(64* x)+(1)/(16) *cos(256* x)+\
            (1)/(32) *cos(32*32* x)+(1)/(64) *cos(64*64 *x)+(1)/(128) *cos(128*128 *x)+(1)/(256) *cos(256*256 *x)

class l_syst:
    def __init__(self,Variable,Constantes,Axiome,Règle,angle=90,avance=20):
        """
        variable :
            type liste
            variable dans le l-système
        constante :
            type liste
            constante
        axiome:
            type sting
            axiome de départ
        règle :
            type liste
            (x,y,u,v,.....)
            x -> y , u -> v ,.....
        angle:
            type entier
            angle pour certaine constante
        avance:
            type entier
            longeur de deplacement
        """
        self.angle=angle
        self.axiome=Axiome
        self.règle=Règle
        self.constante=Constantes
        self.variable=Variable
        self.avance=avance
        self.pas_actuel=1
        self.__creation_variable__()
        self.direction=0
    def __creation_variable__(self):
        variable_remplacement=["╚","╔","╩","╦","╠","═","╬","é","è","ë","ê","æ",
                               "û","ü","µ","à","â","ä","ç","ï","î","ô","ö","_",
                               "ÿ","$","£","¤","Ê","Â","Î","Ô","Û","Ë","Ä","Ü",
                               "Ï","Ö","©","®","Æ","¿","░","▒","▓","ð","Ð","¶",
                               "ı","┘","┌","█","▄","¦","Ì","▀","±","‗","ß","þ",
                               "Þ","½","¼","¾","│","┤"]
        indice_remplacement=0
        remplacement_definitif=[]
        for i in self.variable:
            if i in variable_remplacement:
                del variable_remplacement[variable_remplacement.index(i)]
        for i in self.variable:
            for j in range(0,len(self.règle),2):
                if i in self.règle[j]:
                    remplacement_definitif.append((i,variable_remplacement[indice_remplacement]))
                    self.règle[j]=variable_remplacement[indice_remplacement]
                    indice_remplacement+=1
        self.remplacement=remplacement_definitif






    def __maj_sense__(self,angle):
        self.direction=(self.direction+angle)%360

    def avance_de_1 (self):
        actuel=self.axiome
        for i in range (len(self.remplacement)):
                actuel=actuel.replace(self.remplacement[i][0],self.remplacement[i][1])
        print(actuel)
        for i in range (0,len(self.règle),2):
            actuel=actuel.replace(self.règle[i],self.règle[i+1])
        print(actuel)


"""
    F : Se déplacer d’un pas unitaire  ;
    + : Tourner à gauche d’angle α ;
    - : Tourner à droite d’un angle α  ;
    & : Pivoter vers le bas d’un angle α;
    ^ : Pivoter vers le haut d’un angle α  ;
    < : Roulez vers la gauche d’un angle α  ;
    > : Roulez vers la droite d’un angle α ;
    | : Tourner sur soi-même de 180°  ;
    [ : Sauvegarder la position courante ;
    ] : Restaurer la dernière position sauvée .
"""
a=l_syst(["a","b","c","â"],["+","-"],"abc",["a","bc","b","ac","c","â","â","e"],)