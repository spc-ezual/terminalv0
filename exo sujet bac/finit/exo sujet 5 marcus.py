#Créer par Marcus
#exo1

def convertir (t) :
    res = 0
    for i in range(1,len(t)+1) :
        res += t[-i]*2**(i-1)
    return res
#-------------------------------------------------------------------------------
#exo 2

def tri_insertion(L) :
    n = len(L)
    if n == 0 :
        return L
    for j in range(1,n) :
        e = L[j]
        i = j
        while i > 0 and L[i-1] > e :
            L[i] = L[i-1]
            i = i - 1
        if i != j :
            for k in range (j,i,n) :
                L[k] = L[k+1]
            L[i] = e
    return L