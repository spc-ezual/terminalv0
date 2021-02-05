#exo 1
def fibo(x):
    fibonaci=[1,1]
    for i in range (x-2):
        fibonaci.append(fibonaci[i+1]+fibonaci[i])
    return fibonaci[-1]
print(fibo(25))

#-----------------------------------------
#exo 2
liste_eleves = ['a','b','c','d','e','f','g','h','i','j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi =  []    
    for compteur in range(...):
        if liste_notes[compteur] == ...:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[...])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = ...
            liste_maxi = [...]
            
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)
