#exo 1
def moyenne(tab):
    try:
        total=0
        for j in tab:
            total+=j
        moyen=total/len(tab)
        return moyen
    except ZeroDivisionError:
        raise ValueError ("Erreure la liste est vide")
#---------------------------------------------------------
#exo 2 

def tri(tab):
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = 1
            tab[i]=valeur
            j= j-1
    return tab
