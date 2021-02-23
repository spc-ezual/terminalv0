def simp(nume,deno): #sert a trouver le plus grand denominateur commun
    a=nume
    b=deno
    if a<b:
            a,b=b,a
    while b!=0:
            a,b=b,a%b
    return a

def simp2(nume,deno):#sert a simplifier une fraction par le pgdc
    pgdc=simp(nume,deno)
    nume//=pgdc
    deno//=pgdc
    if nume%deno==0:
        return nume//deno

    else:
        return [nume,deno]

def signe(nume,deno):
    if deno <0:
        if nume<0:
            return bool(True)
        if nume>0:
            return bool(False)
    else:
        if nume<0:
            return bool(False)
        if nume>0:
            return bool(True)

class fraction:
    def __init__(self,nume,deno):
        self.positif=signe(nume,deno)
        if nume<0:
            nume*=-1
        if deno <0:
            deno*=-1
        self.nume=nume
        self.deno=deno

def addition(nb1,nb2):
        if type(nb2)==fraction:

            if nb1.positif == False and nb2.positif==True:
                nume=(-nb1.nume)*nb2.deno+nb2.nume*nb1.deno

            elif nb2.positif==False and nb1.positif==True:
                nume=nb1.nume*nb2.deno+(-nb2.nume)*nb1.deno

            elif nb1.positif==False and nb2.positif==False:
                nume=(-nb1.nume)*nb2.deno+(-nb2.nume)*nb1.deno

            else:
                nume=nb1.nume*nb2.deno+nb2.nume*nb1.deno
            deno=nb1.deno*nb2.deno

            if nume==0:
                return "0"

            if nume<0:
                signe=-1
                nume*=-1

            else:
                signe=1

            fract=simp2(nume,deno)

            if type(fract)==list:
                fract[0]=signe*fract[0]
                return "{}/{}".format(fract[0],fract[1])

            else:
                if signe==-1:
                    fract*=-1
                return fract

        elif type(nb2)==int:
            if nb2<0:
                print(soustraction(nb1,nb2))
            else:
                deno=nb1.deno
                if not nb1.positif:
                    nume=(-nb1.nume)+nb2*nb.deno
                else:
                    nume=nb1.nume+nb2*nb.deno
                if nume<0:
                    signe=-1
                    nume*=-1
                else:
                    signe=1
                fract=simp2(nume,deno)

                if type(fract)==list:
                    fract[0]=signe*fract[0]
                    return "{}/{}".format(fract[0],fract[1])
                else:
                    fract=signe*fract
                    return fract

        elif type(nb2)==float:
            fract2=mise_frac(nb2)
            fraction_provisoir=fraction(fract2[0],fract2[1])
            print(addition(nb1,fraction_provisoir))


        else:
            print("aucun calcule posible")

def soustraction(nb1,nb2):
        if type(nb2)==fraction:

            if nb1.positif == False and nb2.positif==True:
                nume=(-nb1.nume)*nb2.deno-nb2.nume*nb1.deno

            elif nb2.positif==False and nb1.positif==True:
                nume=nb1.nume*nb2.deno-(-nb2.nume)*nb1.deno

            elif nb1.positif==False and nb2.positif==False:
                nume=(-nb1.nume)*nb2.deno-(-nb2.nume)*nb1.deno

            else:
                nume=nb1.nume*nb2.deno-nb2.nume*nb1.deno
            deno=nb1.deno*nb2.deno

            if nume==0:
                return "0"

            if nume<0:
                signe=-1
                nume*=-1

            else:
                signe=1

            fract=simp2(nume,deno)

            if type(fract)==list:
                fract[0]=signe*fract[0]
                return "{}/{}".format(fract[0],fract[1])

            else:
                if signe==-1:
                    fract*=-1
                return fract

        elif type(nb2)==int:

            if nb2<0:
                print(addition(nb1,nb2))

            else:

                deno=nb1.deno


                if not nb1.positif:
                    nume=(-nb1.nume)-nb2*nb.deno
                else:
                    nume=nb1.nume-nb2*nb.deno
                if nume<0:
                    signe=-1
                    nume*=-1
                else:
                    signe=1
                fract=simp2(nume,deno)

                if type(fract)==list:
                    fract[0]=signe*fract[0]
                    return "{}/{}".format(fract[0],fract[1])
                else:
                    fract=signe*fract
                    return fract

        elif type(nb2)==float:
            fract2=mise_frac(nb2)
            fraction_provisoir=fraction(fract2[0],fract2[1])
            print(soustraction(nb1,fraction_provisoir))



        else:
            print("aucun calcule posible")

def multiplication(nb1,nb2):

    if type(nb2)==fraction:
        deno=nb1.deno*nb2.deno
        nume=nb1.nume*nb2.nume
        fract=simp2(nume,deno)
        signe=1

        if nb1.positif==False :
            signe*=-1

        if nb2.positif==False:
            signe*=-1

        if type(fract)==list:
            fract[0]*=signe
            return "{}/{}".format(fract[0],fract[1])

        else:
            fract*=signe
            return fract

    elif type(nb2)==int:
        fraction_provisoir=fraction(nb2,1)
        print(multiplication(nb1,fraction_provisoir))

    elif type(nb2)==float:
            fract2=mise_frac(nb2)
            fraction_provisoir=fraction(fract2[0],fract2[1])
            print(multiplication(nb1,fraction_provisoir))

    else:
        print("aucun calcule posible")

def division (nb1,nb2):

    if type(nb2)==fraction:
        fraction_provisoir=fraction(nb2.deno,nb2.nume)
        print(multiplication(nb1,fraction_provisoir))
    elif type(nb2)==int:
        fraction_provisoir=fraction(1,nb2)
        print(multiplication(nb1,nb2))

    elif type(nb2)==float:
        fract2=mise_frac(nb2)
        fraction_provisoir=fraction(fract2[1],fract2[0])
        print(multiplication(nb1,fraction_provisoir))

    else:
        print("aucun calcule posible")


def mise_frac(x):
    signe=1

    if x<0:
        signe=-1
        x*=-1
    n,d,an,ad,nb = int(x),1,1,0,x #n et d sont respectivemrnt de numerateur et le denominateur ,#nb est le nombre x , an et ad sont respectivement l'ancien numerateur et denominateur

    while abs(n/d-x)>1e-500:        #regarde si la fraction est egale a environ 10^-6au nombre x
         nb = 1/(nb%1)
         k,l = int(nb)*n+an,int(nb)*d+ad
         an,ad,n,d = n,d,k,l
    n*=signe
    return [n,d]

def puissance(nb1,nb2):

    if type(nb2)==fraction or type(nb2)==int:

        if type(nb2)==int:
            if nb2<0:
                nume=nb1.deno**nb2
                deno=nb1.nume**nb2
            elif nb2>0:
                nume=nb1.nume**nb2
                deno=nb1.deno**nb2
            else:
                return "1"
            fract=[nume,deno]

        elif type(nb2)==fraction:
            if nb2.positif==True:
                nume=nb1.nume**nb2.nume
                deno=nb1.deno**nb2.nume
            else :
                nume=nb1.deno**nb2.nume
                deno=nb1.nume**nb2.nume
            fract=racine_nieme_puissance(nume,deno,nb2.deno)
        return"{}/{}".format(fract[0],fract[1])

    elif type(nb2)==float:
        fract=mise_frac(nb2)
        fraction_provisoir=fraction(fract[0],fract[1])
        print(puissance(nb1,fraction_provisoir))

    else:
        pass




def racine_nieme_puissance(nume,deno,n):
    nume=nume**(1/n)
    deno=deno**(1/n)

    if type(nume)==int and type(deno)==int:
        return [nume,deno]

    else:
        fract=mise_frac(nume/deno)
        return[fract[0],fract[1]]

def racine_n(nb1,n):
    rep=(nb1.nume/nb1.deno)

    if nb1.positif==True:

        if type(n)==int and n>0:
            rep**=(1/n)

            if n%2==1:
                rep2=rep*-1
                return rep,rep2

            else :
                return str(rep)

        else:
            return "n doit être un entier naturel non nul"
    elif nb1.positif==False:

        if type(n)==int and n>0 and n%2==1:
            rep**=(1/n)
            rep*=-1
            return rep

        else :
            return " n doit etre un entier naturel impair car la fraction est negative"

def ln (x):
    if type(x)==fraction and x.positif==True:
        return ln(x.nume)-ln(x.deno)
    elif type(x)==int and x>0 or type(x)==float and x>0:
        fract=(1-x)/(x + 1)
        nb_base=1
        somme=0
        for i in range(10**5):
            somme+=(1/nb_base)*(fract**nb_base)
            nb_base+=2
        return -2*somme


    else:
        return "{} n'est pas un nombre naturel non nul".format(x)
def loga(sur,nb1):
    pass

from decimal import *
from math import *
getcontext().prec= 10
a=fraction(8,5)
b=fraction(-7,6)
print(puissance(a,-0.25))
addition(a,2.075)
soustraction(a,8.07956)
print(mise_frac(8.07956))
c=fraction(95,843)

"""raise ValueError("liste vide")"""