#exo 1
def recherhce(caractere,mot):
    return mot.count(caractere)

#----------------------------------------------
#exo 2

pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0,Pieces=[100,50,20,10,5,2,1]):
    if arendre == 0:
            return solution
    p = pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution, i+1)