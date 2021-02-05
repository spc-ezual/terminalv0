from math import cos
from PIL import Image, ImageDraw
from math import radians,cos,sin
class l_syst:
    def __init__(self,Variable,Constantes,Axiome,Règle,angle=90,avance=20,
    img_taille=(10000,10000),font=(0,0,0),coul=(255,255,255),
    depart=(5000,5000),épaisseur_dessin=1,nom="l_système",dirrection=0):
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
        self.actuel=Axiome
        self.règle=Règle
        self.constante=Constantes
        self.variable=Variable
        self.avance=avance
        self.pas_actuel=0
        self.__creation_variable__()
        self.direction=0
        self.coul=coul
        self.image_taille=img_taille
        self.font=font
        self.depart=depart
        self.épaisseur=épaisseur_dessin
        self.nom=nom
        self.__verification_constante__()
        self.direction=-dirrection
    def __verification_constante__(self):
        liste_constante=["+","-","&","^","<",">","|","[","]"]
        for i in self.constante:
            if i not in liste_constante:
                raise ValueError("constante non existante")


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
        for i in range(0,len(self.variable),2):
            for j in range(0,len(self.règle),2):
                if self.variable[i] == self.règle[j]:
                    remplacement_definitif.append((self.variable[i],variable_remplacement[indice_remplacement]))
                    self.règle[j]=variable_remplacement[indice_remplacement]
                    indice_remplacement+=1
        self.remplacement=remplacement_definitif

    def __maj_sense__(self,angle):
        self.direction=(self.direction+angle)%360

    def avance_de_1 (self):
        actuel=self.actuel
        for i in range (len(self.remplacement)):
                actuel=actuel.replace(self.remplacement[i][0],self.remplacement[i][1])
        for i in range (0,len(self.règle),2):
            actuel=actuel.replace(self.règle[i],self.règle[i+1])
        self.actuel=actuel
        self.pas_actuel+=1

    def translation(self,a,angle,longeur):
        angle_radian=radians(angle)
        return (a[0]+longeur*cos(angle_radian),a[1]+longeur*sin(angle_radian))

    def __tracer_v__(self):
        retur=[]
        for i in range(0,len(self.variable),2):
            if self.variable[i+1]==True:
                retur.append(self.variable[i])
        return retur

    def tracer(self):
        img=Image.new("RGB",self.image_taille,self.font)
        dessin=ImageDraw.Draw(img)
        a_tracer=self.actuel
        point_actuel=self.depart
        v_a_tracer=self.__tracer_v__()
        for i in a_tracer:
            if i in v_a_tracer:
                nouveaux_point=self.translation(point_actuel,self.direction,self.avance)
                dessin.line((point_actuel,nouveaux_point),self.coul,self.épaisseur)
                point_actuel=nouveaux_point
            if i == "+":
                self.__maj_sense__(-self.angle)
            if i =="-":
                self.__maj_sense__(self.angle)
            if i == "[":
                point_sauv=point_actuel
            if i == "]":
                point_actuel=point_sauv
            if i == "|":
                self.__maj_sense__(180)
            if i == "&":
                if self.direction<=90 and self.direction>=-90:
                    self.__maj_sense__(self.angle)
                else:
                    self.__maj_sense__(-self.angle)
            if i == "^":
                if self.direction<=90 and self.direction>=-90:
                    self.__maj_sense__(-self.angle)
                else:
                    self.__maj_sense__(self.angle)
            if i=="<":
                angle_sauv=self.direction
                self.__maj_sense__(-self.angle)
                nouveaux_point=self.translation(point_actuel,self.direction,self.avance)
                dessin.line((point_actuel,nouveaux_point),self.coul,self.épaisseur)
                point_actuel=nouveaux_point
                self.direction=angle_sauv
            if i==">":
                angle_sauv=self.direction
                self.__maj_sense__(self.angle)
                nouveaux_point=self.translation(point_actuel,self.direction,self.avance)
                dessin.line((point_actuel,nouveaux_point),self.coul,self.épaisseur)
                point_actuel=nouveaux_point
                self.direction=angle_sauv
        img.save("{}.jpg".format(self.nom))
##a=l_syst(["A",True,"B",True],["+","-"],"A",["A","A-B--B+A++AA+B-","B","+A-BB--B-A++A+B"],60,avance=10,épaisseur_dessin=2)
##for i in range(6):
##    a.avance_de_1()
##a.tracer()