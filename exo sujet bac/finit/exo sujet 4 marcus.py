#exo 1
def moyenne(tab):
        total=0
        for j in tab:
            total+=j
        moyen=total/len(tab)
        return moyen
# -------------------------------------------------
# exo 2

def dichotomie(tab, x):
    # cas du tableau vide
    if len(tab)==0:
        return False,1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[0]):
        return False,2
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = fin +1			
    return False,3