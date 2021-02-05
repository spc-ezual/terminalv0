#exo 1
def moyenne(tab):
    total_note=0
    nb_note=0
    for j in tab:
        total_note=j[0]*j[1]+total_note
        nb_note+=j[1]
    return total_note/nb_note
print(moyenne([(15,2),(9,1),(12,3)]))
#faute sujet 11,83 n'est pas 12,5
#----------------------------------------------------
#exo 2
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
print(pascal(5))
