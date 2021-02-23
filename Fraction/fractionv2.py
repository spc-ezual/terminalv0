def simplification(nomi,deno):
    i=2

    while i<=nomi and i<=deno:

        if nomi%i==0 and deno%i==0:
            nomi=nomi//i
            deno=deno//i

        else:
                i=i+1
    if nomi%deno==0:
        return nomi//deno

    else:
        return [nomi,deno]

class fraction :

    def __init__(nb1,deno,nomi):
        frac=simplification(nomi,deno)
        nb1.nomi=frac[1]
        nb1.deno=frac[0]

    def addition_entier(nb1,en):
        nomi=nb1.nomi+nb1.deno*en
        deno=nb1.deno
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac


    def addition_frac(nb1,nb2):
        copy_n1=nb1
        copy_n2=nb2
        nomi=copy_n1.nomi*copy_n2.deno+copy_n1.deno*copy_n2.nomi
        deno=copy_n1.deno*copy_n2.deno
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

    def sou_entier(nb1,en):
        nomi=nb1.nomi-nb1.deno*en
        deno=nb1.deno
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

    def sou_frac(nb1,nb2):
        copy_n1=nb1
        copy_n2=nb2

        nomi=copy_n1.nomi*copy_n2.deno-copy_n1.deno*copy_n2.nomi
        deno=copy_n1.deno*copy_n2.deno
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

    def multi_entier(nb1,en):
        nomi=nb1.nomi*en
        deno=nb1.deno
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

    def multi_frac(nb1,nb2):
        copy_n1=nb1
        copy_n2=nb2
        nomi=copy_n1.nomi*copy_n2.nomi
        deno=copy_n1.deno*copy_n2.deno
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

    def div_entier(nb1,en):
        deno=nb1.demo*en
        nomi=nb1.nomi
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

    def div_frac(nb1,nb2):
        copy_n1=nb1
        copy_n2=nb2
        nomi=copy_n1.nomi*copy_n2.deno
        deno=copy_n1.deno*copy_n2.nomi
        frac=simplification(nomi,deno)

        if type(frac)==list:
            fract=str(frac[0])+"/"+str(frac[1])
            return fract

        else:
            return frac

"""
    def simp(a,b):
        if a <b:
            a,b=b,a
        while b!=0:
            a,b=b,a%b
        return a
    def simp2(self):
        pgdc=fraction.simp(self.nume,self.deno)
        self.nume//=pgcd
        self.deno//=pgcd"""


a=fraction(-8,5)
b=fraction(7,6)


