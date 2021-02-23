def simplification(nomi,deno):
    i=2

    if deno<0:
        deno*=-1
    if nomi<0:
        nomi*=-1

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

def signe(nomi,deno):
    if deno <0:
        if nomi<0:
            return bool(a)
        if nomi>0:
            return bool(False)
    else:
        if nomi<0:
            return bool(False)
        if nomi>0:
            return bool(a)


class fraction:
    def __init__(nb1,deno,nomi):
        frac=simplification(nomi,deno)
        nb1.positif=signe(nomi,deno)
        nb1.nomi=frac[1]
        nb1.deno=frac[0]

    def addition(nb,nb2):
        if type(nb2)==fraction:
            if not nb.positif:
                nomi=(-nb.nomi)*nb2.deno+nb2.nomi*nb.deno
            if nb2.positif==false:
                nomi=nb.nomi*nb2.deno+(-nb2.nomi)*nb.deno
            if not nb.positif and  not nb2.positif==false:
                nomi=(-nb.nomi)*nb2.deno+(-nb2.nomi)*nb.deno
            else:
                nomi=nb.nomi*nb2.deno+nb2.nomi*nb.deno
            deno=nb.deno*nb2.deno
            if nomi<0:
                signe=-1
                nomi*=-1
            else:
                signe=1
            fract=simplification(nomi,deno)

            if type(fract)==list:

                if signe==-1:
                    fract[0]
                fract=str(fract[0])+"/"+str(fract[1])
                return fract

            else:
                if signe==-1:
                    fract*=-1
                return fract
        elif type(nb2)==int:
            deno=nb.deno
            if not nb.positif:
                nomi=(-nb.nomi)+int*nb.deno
            else:
                nomi=nb.nomi+int*nb.deno
            if nomi<0:
                signe=-1
                nomi*=-1
            else:
                signe=1
            fract=simplification(nomi,deno)

            if type(fract)==list:

                if signe==-1:
                    fract[0]
                fract=str(fract[0])+"/"+str(fract[1])
                return fract

            else:
                if signe==-1:
                    fract*=-1
                return fract



        else :
            print("aucun calcule posible")

    def addition(nb,nb2):
        if type(nb2)==fraction:
            if nb.positif == false:
                nomi=(-nb.nomi)*nb2.deno-nb2.nomi*nb.deno
            if nb2.positif==false:
                nomi=nb.nomi*nb2.deno+(-nb2.nomi)*nb.deno
            if nb.positif==false and nb2.positif==false:
                nomi=(-nb.nomi)*nb2.deno+(-nb2.nomi)*nb.deno
            else:
                nomi=nb.nomi*nb2.deno-nb2.nomi*nb.deno
            deno=nb.deno*nb2.deno
            if nomi<0:
                signe=-1
                nomi*=-1
            else:
                signe=1
            fract=simplification(nomi,deno)

            if type(fract)==list:

                if signe==-1:
                    fract[0]
                fract=str(fract[0])+"/"+str(fract[1])
                return fract

            else:
                if signe==-1:
                    fract*=-1
                return fract
        elif type(nb2)==int:
            deno=nb.deno
            if nb.positif == false:
                nomi=(-nb.nomi)-nb2*nb.deno
            else:
                nomi=nb.nomi-nb2*nb.deno
            if nomi<0:
                signe=-1
                nomi*=-1
            else:
                signe=1
            fract=simplification(nomi,deno)

            if type(fract)==list:

                if signe==-1:
                    fract[0]
                fract=str(fract[0])+"/"+str(fract[1])
                return fract

            else:
                if signe==-1:
                    fract*=-1
                return fract



        else :
            print("aucun calcule posible")

a=fraction(-8,5)
b=fraction(7,6)
print(type(a))

