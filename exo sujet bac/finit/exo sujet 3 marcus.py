#exo 1
def multiplication(a,b):
    rep=0
    for i in range (b):
        rep = rep + a
    return rep

#-------------------------------------------------------
# exo 2
def dichotomie(tab, x):
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = debut
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = fin -1			
    return False
