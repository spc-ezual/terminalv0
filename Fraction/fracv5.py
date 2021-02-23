def trouver_pgcd(nume,deno): #sert a trouver le plus grand denominateur commun
    a=nume
    b=deno
    if a<b:
            a,b=b,a
    while b!=0:
            a,b=b,a%b
    return a

def simp_entier(nume,deno):#sert a simplifier une fraction par le pgdc
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

def signe(nume,deno):
    if deno <0:
        if nume<0:
            return ""
        if nume>0:
            return "-"
    else:
        if nume<0:
            return "-"
        if nume>0:
            return ""

class ComparaisonError(Exception):
    def __init__(self,msg='Vérifier votre comparaison') :
        Exception.__init__(self,msg)

class fraction:
    def __init__(self,nume,deno):
        self.eval=nume/deno
        self.signe=signe(nume,deno)
        if nume<0:
            nume*=-1
        if deno <0:
            deno*=-1
        nume,deno=simp_entier(nume,deno)
        self.nume=int(nume)
        self.deno=int(deno)
        
    
    def __str__(self):
        return "{}{}/{}".format(self.signe,self.nume,self.deno)
    
    def avec_signe(self):
        if self.signe=="-":
            return self.nume*-1
        else:
            return self.nume

    def __add__(self, x):
        nume_self=self.avec_signe()
        if type(x)== float or type(x)==int:
            return fraction(nume_self+x*self.deno,self.deno)
        if type(x)==fraction:
            nume_x=x.avec_signe()
            return fraction (nume_self*x.deno+nume_x*self.deno,self.deno*x.deno)
        if type(x)==complex:
            return complex(self.eval+x.real,x.imag)
        

    def __sub__(self, x) :
        nume_self=self.avec_signe()
        if type(x)== float or type(x)==int:
            return fraction(nume_self-x*self.deno,self.deno)
        if type(x)==fraction:
            nume_x=x.avec_signe()
            return fraction (nume_self*x.deno-nume_x*self.deno,self.deno*x.deno)
        if type(x)==complex:
            return complex(self.eval-x.real,-x.imag)        
        
    def __mul__(self, x) :
        nume_self=self.avec_signe()
        if type(x)== float or type(x)==int:
            return fraction(nume_self*x,self.deno)
        if type(x)==fraction:
            nume_x=x.avec_signe()
            return fraction (nume_self*nume_x,self.deno*x.deno)
        if type(x)==complex:
            return complex(self.eval*x.real,self.eval*x.imag)
        
    
    
    def __truediv__(self, x) :
        if type(x)== float or type(x)==int:
            return  self*fraction(1,x)
        if type(x)==fraction:
            return self*fraction(x.deno,x.nume)

   
   
   
    def __floordiv__(self,x):#div entiere
        if type(x)== float or type(x)==int:
            x=fraction(x,1)
        sortie=fraction(self.nume,self.deno)
        nb_rep=0
        while sortie.eval >= x.eval:
            sortie=sortie-x
            nb_rep+=1       
        if self.signe=="-":
            return (nb_rep+1)*-1
        
        return nb_rep
    
    
    def __eq__(self, x):
        if type(x)==float or type(x)==int:
            if self.eval==x:
                return True
            else :
                return False
        if type(x)==fraction:
            if self.nume==x.nume and self.deno==x.deno and self.signe==x.signe:
                return True
            else:
                return False
        if type(x)==complex:
            if self.eval==x.real and x.imag==0:
                return True
            else:
                return False
        return False
    
    def __ne__(self, x):
        return False==(self==x)
    
    def __lt__(self,x):
        if type(x)==float or type(x)==int:
            if self.eval<x:
                return True
            else :
                return False
        if type(x)==fraction:
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
        
    def __le__(self,x):
        if type(x)==float or type(x)==int:
            if self.eval<=x:
                return True
            else :
                return False
        if type(x)==fraction:
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
                
    def __gt__(self,x):
        if type(x)==float or type(x)==int:
            if self.eval>x:
                return True
            else :
                return False
        if type(x)==fraction:
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
    
    def __ge__(self,x):
        if type(x)==float or type(x)==int:
            if self.eval>=x:
                return True
            else :
                return False
        if type(x)==fraction:
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
        
        
    
    
    
    
    def __mod__(self,x):
        if type(x)== float or type(x)==int:
            x=fraction(x,1)
        sortie=fraction(self.nume,self.deno)
        while sortie.eval >= x.eval:
            sortie=sortie-x        
        return sortie




    def __float__(self):
        return self.eval
    
    def __int__(self):
        return int(self.eval)
    
    
    def __round__(self):
        if self.eval//1<0.5 and self.eval//1>-0.5:
            return int(self)
        else:
            if self.signe=='-':
                return int(self)-1
            else:
                return int(self)+1
                
def mise_frac(x):
    signe=1
    if x<0:
        signe=-1
        x*=-1
    n,d,an,ad,nb = int(x),1,1,0,x #n et d sont respectivemrnt de numerateur et le denominateur ,#nb est le nombre x , an et ad sont respectivement l'ancien numerateur et denominateur

    while abs(n/d-x)>1e-50:        #regarde si la fraction est egale a environ 10^-6au nombre x
         nb = 1/(nb%1)
         k,l = int(nb)*n+an,int(nb)*d+ad
         an,ad,n,d = n,d,k,l
    n*=signe
    return fraction(n,d)

a=fraction(-7.4,8)
b=complex(0.1,1)
c=a-b
print(c)
b=round(a)
b=87|78
print(78>>5)
for i in range(4):
    print(100.89>>i,bin(100>>i))