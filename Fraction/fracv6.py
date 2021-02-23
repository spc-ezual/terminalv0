
def trouver_pgcd(nume : int, deno : int) -> int: #sert a trouver le plus grand denominateur commun
    a=nume
    b=deno
    if a<b:
            a,b=b,a
    while b!=0:
            a,b=b,a%b
    return a

def simp_entier(nume : float, deno : float) -> list:#sert a simplifier une fraction par le pgdc
    while nume%1 != 0:
        nume=nume*10
        deno=deno*10
    while deno%1 != 0:
        deno=deno*10        
        nume=nume*10
    pgdc=trouver_pgcd(nume,deno)
    nume//=pgdc
    deno//=pgdc
    return [nume,deno]

def signe(nume : int,deno : int) -> bool:
    if deno <0:
        if nume<0:
            return True
        if nume>0:
            return False
    else:
        if nume<0:
            return False
        if nume>0:
            return True
        
def mise_frac(x):
    signe=1
    if x<0:
        signe=-1
        x*=-1
    n,d,an,ad,nb = int(x),1,1,0,x 
    while abs(n/d-x)>1e-50:
         nb = 1/(nb%1)
         k,l = int(nb)*n+an,int(nb)*d+ad
         an,ad,n,d = n,d,k,l
    n*=signe
    return Fraction(n,d)

class ComparaisonError(Exception):

    def __init__(self,msg: str ='Vérifier votre comparaison' ) -> None :
        Exception.__init__(self,msg)

class Fraction(object):

        def __init__(self,nume : float, deno : float) -> None:
                #object.__init__(Fraction)
                self.eval=nume/deno
                self.est_positif=signe(nume,deno)
                if nume<0:
                    nume*=-1
                if deno <0:
                    deno*=-1
                nume,deno=simp_entier(nume,deno)
                self.nume=int(nume)
                self.deno=int(deno)

        def __str__(self) -> str:
                if self.est_positif:
                        return  "{}/{}".format(self.nume,self.deno)
                else:
                       return "-{}/{}".format(self.nume,self.deno)
        
        def avec_signe(self) -> int:
                """
                return 
                """
                if self.est_positif:
                        return self.nume
                else:
                        return -1*self.nume
    
        def __add__(self,x : object) -> object:
                """
                return self+x
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self+x*self.deno,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction(nume_self*x.deno+nume_x*self.deno,self.deno*x.deno)
                if type(x)==complex:
                        return complex(self.eval+x.real,x.imag)

        def __radd__(self,x : object) -> object:
                """
                return x+self
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self+x*self.deno,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction(nume_self*x.deno+nume_x*self.deno,self.deno*x.deno)
                if type(x)==complex:
                        return complex(self.eval+x.real,x.imag)
        
        def __iadd__(self,x : object) -> object:
                """
                self+=x
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self+x*self.deno,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction(nume_self*x.deno+nume_x*self.deno,self.deno*x.deno)
                if type(x)==complex:
                        return complex(self.eval+x.real,x.imag)
                        
        def __sub__(self,x : object ) -> object :
                """
                return self-x
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self-x*self.deno,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction (nume_self*x.deno-nume_x*self.deno,self.deno*x.deno)
                if type(x)==complex:
                        return complex(self.eval-x.real,-x.imag)

        def __rsub__(self,x : object) -> object :
                """
                return x-self
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(x*self.deno-nume_self,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction (nume_x*self.deno-nume_self*x.deno,self.deno*x.deno)
                if type(x)==complex:
                        return complex(x.real-self.eval,x.imag)

        def __isub__(self,x : object) -> object :
                """
                self-=x
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self-x*self.deno,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction (nume_self*x.deno-nume_x*self.deno,self.deno*x.deno)

        def __mul__(self,x : object) -> object :
                """
                return self*x
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self*x,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction (nume_self*nume_x,self.deno*x.deno)
                if type(x)==complex:
                        return complex(self.eval*x.real,self.eval*x.imag)

        def __rmul__(self,x : object) -> object :
                """
                return x*self
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self*x,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction (nume_self*nume_x,self.deno*x.deno)
                if type(x)==complex:
                        return complex(self.eval*x.real,self.eval*x.imag)
        
        def __imul__(self,x : object) -> object :
                """
                self*=x
                """
                nume_self=self.avec_signe()
                if type(x)== float or type(x)==int:
                        return Fraction(nume_self*x,self.deno)
                if type(x)==Fraction:
                        nume_x=x.avec_signe()
                        return Fraction (nume_self*nume_x,self.deno*x.deno)

        def __truediv__(self,x : object) -> object :
                """
                return self/x
                """
                if type(x)== float or type(x)==int:
                        return  self*Fraction(1,x)
                if type(x)==Fraction:
                        return self*Fraction(x.deno,x.nume)

        def __rtruediv__(self,x : object) -> object :
                """
                return x/self
                """
                if type(x)== float or type(x)==int:
                        return  Fraction(x,self.eval)
                if type(x)==Fraction:
                        return Fraction

        def __itruediv__(self,x : object) -> object :
                """
                self/=x
                """
                if type(x)== float or type(x)==int:
                        return  self*Fraction(1,x)
                if type(x)==Fraction:
                        return self*Fraction(x.deno,x.nume)

        def __floordiv__(self,x : object) -> object :#div entiere
                """
                return self//x
                """
                if type(x)== float or type(x)==int:
                        x=Fraction(x,1)
                if type(x)==Fraction:
                        sortie=Fraction(self.nume,self.deno)
                        nb_rep=0
                        while sortie.eval >= x.eval:
                                sortie=sortie-x
                                nb_rep+=1       
                        if not self.est_positif:
                                return (nb_rep+1)*-1
                        return nb_rep

        def __rfloordiv__(self,x : object) -> object :
                """
                return x//self
                """
                if type(x)== float or type(x)==int:
                        x=Fraction(x,1)
                if type(x)==Fraction:
                        sortie=x
                        nb_rep=0
                        while sortie.eval >= self.eval:
                                sortie=sortie-self
                                nb_rep+=1     
                        if not self.est_positif:
                                return (nb_rep+1)*-1
                        return nb_rep

        def __ifloordiv__(self,x : object) -> object :#div entiere
                """
                self//=x
                """
                if type(x)== float or type(x)==int:
                        x=Fraction(x,1)
                if type(x)==Fraction:
                        sortie=Fraction(self.nume,self.deno)
                        nb_rep=0
                        while sortie.eval >= x.eval:
                                sortie=sortie-x
                                nb_rep+=1       
                        if not self.est_positif:
                                return (nb_rep+1)*-1
                        return nb_rep

        def __abs__(self) -> object :
                """
                return abs(self)
                """
                return Fraction(self.nume,self.deno)

        def __pow__(self,x : object) ->object:
                """
                return self**x
                """
                if type(x)==Fraction:
                        x=x.eval
                return mise_frac(self.eval**x)
        
        def __rpow__ (self,x : object) -> object:
                """
                return x**self
                """                
                if type(x)==Fraction:
                        x=x.eval
                return mise_frac(x**self.eval)
        
        def __ipow__(self,x : object) ->object:
                """
                self**=x
                """
                if type(x)==Fraction:
                        x=x.eval
                return mise_frac(self.eval**x)
        
        def __mod__(self,x : object) -> object:
                """
                return self%x
                """
                if type(x)==int or type(x)==float:
                        x=Fraction(x,1)
                if type(x)==Fraction:
                        sortie=Fraction(self.avec_signe(),self.deno)
                        while sortie>x:
                                print(sortie)
                                sortie-=x
                        return sortie

        def __rmod__(self,x : object) -> object:
                """
                return x%self
                """
                if type(x)==int or type(x)==float:
                        x=Fraction(x,1)
                if type(x)==Fraction:
                        sortie=Fraction(x.avec_signe(),x.deno)
                        while sortie>self:
                                sortie-=self
                        return sortie
                
        def __imod__(self,x : object) -> object:
                """
                self%=x
                """
                if type(x)==int or type(x)==float:
                        x=Fraction(x,1)
                if type(x)==Fraction:
                        sortie=Fraction(self.avec_signe(),self.deno)
                        while sortie>x:
                                print(sortie)
                                sortie-=x
                        return sortie
     
        def __eq__(self, x: object) -> bool:
                """
                return self==x
                """
                if type(x)==float or type(x)==int:
                        if self.eval==x:
                                return True
                        else :
                                return False
                if type(x)==Fraction:
                        if self.nume==x.nume and self.deno==x.deno and self.est_positif==x.est_positif:
                                return True
                        else:
                                return False
                if type(x)==complex:
                        if self.eval==x.real and x.imag==0:
                                return True
                        else:
                                return False
                return False

        def __ne__(self, x: object) -> bool:
            return False==(self==x)
        
        def __lt__(self, x: object) -> bool:
                """
                return self<x
                """
                if type(x)==float or type(x)==int:
                        if self.eval<x:
                                return True
                        else :
                                return False
                if type(x)==Fraction:
                        if self.eval<x.eval:
                                return True
                        else:
                                return False
                if type(x)==complex:
                        if self.eval<x.real and x.imag==0:
                                return True
                        else:
                                return False
                raise ComparaisonError
                
        def __le__(self, x: object) -> bool:
                """
                return self<=x
                """
                if type(x)==float or type(x)==int:
                        if self.eval<=x:
                                return True
                        else :
                                return False
                if type(x)==Fraction:
                        if self.eval<=x.eval:
                                return True
                        else:
                                return False
                if type(x)==complex:
                        if self.eval<=x.real and x.imag==0:
                                return True
                        else:
                                return False
                raise ComparaisonError
                        
        def __gt__(self, x: object) -> bool:
                """
                return self>x
                """
                if type(x)==float or type(x)==int:
                        if self.eval>x:
                                return True
                        else :
                                return False
                if type(x)==Fraction:
                        if self.eval>x.eval:
                                return True
                        else:
                                return False
                if type(x)==complex:
                        if self.eval>x.real and x.imag==0:
                                return True
                        else:
                                return False
                raise ComparaisonError
        
        def __ge__(self, x: object) -> bool:
                """
                return self>=x
                """
                if type(x)==float or type(x)==int:
                        if self.eval>=x:
                                return True
                        else :
                                return False
                if type(x)==Fraction:
                        if self.eval>=x.eval:
                                return True
                        else:
                                return False
                if type(x)==complex:
                        if self.eval>=x.real and x.imag==0:
                                return True
                        else:
                                return False
                
                raise ComparaisonError

        def __float__(self) -> float:
                """
                return float(self)
                """
                return self.eval
    
        def __int__(self) -> int:
                """
                return int(self)
                """
                return int(self.eval)
    
        def  __complex__(self) -> complex :
                """
                return complex(self)
                """
                return complex(self.eval,0)

        def __round__(self) -> int:
                """
                return round(self)
                """
                if self.eval//1<0.5 and self.eval//1>-0.5:
                        return int(self)
                else:
                        if self.est_positif:
                                return int(self)-1
                        else:
                                return int(self)+1

# J'ai refais la classe fraction de maniere bien plus evoluer qu'avans 
# Pourriez-vous me dire si selon vous il manque des methode ou si la class est complete
# Et s'auriez vous comment faire pour que l'objet fraction soit comme un int ou un float 
# pour que je puisse ecrire par exemple def __imod__(self,x : object) -> Fraction: sans avoir d'erreur .