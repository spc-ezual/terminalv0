import time
from PIL import Image, ImageDraw
from random import randint,uniform

#------------------------------------------------------------------------------
# Equation quadratique qui verifie si un point part ou si il reste
#si il part on a le nombre i qui est le nombre nececaire d'itertion anvans que il ne parte

def quadratique(z,constante):
    i=0
    dis=constante.imag**2+constante.real**2
    while dis<4 and i<402:
        z=z**2+constante
        i+=1
        dis=z.imag**2+z.real**2
    return i

#-------------------------------------------------------------------------------
#associer un nombre a une longeur d'onde pour créé un degrader

def coul(longeur_Onde):
    couleur =()
    if longeur_Onde<60:couleur=(int(-(longeur_Onde-60)/(60-0)*255),0,255)
    elif longeur_Onde<110:couleur=(0,int((longeur_Onde-60)/(110-60)*255),255)
    elif longeur_Onde<130:couleur=(0,255,int(-(longeur_Onde-130)/(130-110)*255))
    elif longeur_Onde<200:couleur=(int((longeur_Onde-130)/(200-130)*255),255,0)
    elif longeur_Onde<265:couleur=(255,int(-(longeur_Onde-265)/(265-200)*255),0)
    elif longeur_Onde<=400:couleur=(255,0,0)
    else:couleur=(0,0,0)
    return couleur

#-------------------------------------------------------------------------------
#coordonner d'un pixel dans un plan de X sur Y longeur

def co_point(co,taille,debutx,finx,debuty,finy):
    r=debutx+((finx-debutx)/taille)*co[0]
    i=debuty+((finy-debuty)/taille)*co[1]
    return complex(r,i)

#-------------------------------------------------------------------------------
#Julia
#constante c toujours la meme

def creation_julia(taille,debut_x=-2,debut_y=-2,fin_x=2,fin_y=2):
    font_plan=Image.new("RGB",taille),complex(uniform(-1,1),uniform(-1,1))
    constante=complex(uniform(-1,1),uniform(-1,1))
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(quadratique(co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),constante)))
    return font_plan.save("julia_{}.jpg".format(constante))

#-------------------------------------------------------------------------------
#Mandelbrot
#constante c égale au point actuel

def creation_mandelbrot(taille):
    font_plan=Image.new("RGB",taille)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(quadratique(complex(0,0),co_point([k,j],taille,-2,1,-1.5,1.5))))
    return font_plan.save("mandelbrot.jpg".format(constante))

#-------------------------------------------------------------------------------
#chemin auto évitant
def chemin(calc,taille,point,pas,coul):
    point_actuel=point[-1]
    possibiliter=[(point_actuel[0]-pas,point_actuel[1]),\
    (point_actuel[0],point_actuel[1]-pas),\
    (point_actuel[0]+pas,point_actuel[1]),\
    (point_actuel[0],point_actuel[1]+pas)]

    for i in range (0,4):
        if possibiliter[i][0]<0 or possibiliter[i][0]>taille[0] or possibiliter[i][1]<0 or possibiliter[i][1]>taille[1]:
            possibiliter[i]=0
        elif possibiliter[i] in point:
            possibiliter[i]=0
    while 0 in possibiliter:
        del possibiliter[possibiliter.index(0)]

    if len(possibiliter)==0: return calc.line(point,coul,2)
    alea=randint(0,len(possibiliter)-1)
    point.append((possibiliter[alea]))
    chemin(calc,taille,point,pas,coul)

def creation_chemin(taille,font=(0,0,0),coul=(randint(10,256),randint(10,256),randint(10,256)),pas=10):
    chemin_auto=Image.new("RGB",taille,font)
    dessin=ImageDraw.Draw(chemin_auto)
    depart=[(taille[0]//2,taille[1]//2)]
    chemin(dessin,taille,depart,pas,coul)
    chemin_auto.save("chemin auto evitant.jpg")

#-------------------------------------------------------------------------------
#noise map

def map_noise(taille,echelle,couche,impacte,lacunariter,graine,multiplicateur_de_terre):
    world = np.zeros(taille)
    x_idx,y_idx = np.linspace(0, 1, taille[0]),np.linspace(0, 1, taille[1])
    monde_x, monde_y = np.meshgrid(x_idx, y_idx)
    world = np.vectorize(pnoise2)(monde_x*multiplicateur_de_terre,monde_y*multiplicateur_de_terre,octaves=couche,\
    persistence=impacte,lacunarity=lacunariter,repeatx=taille[0],repeaty=taille[1],base=graine)
    return np.floor((world+0.5) * 255).astype(np.uint8)

def coul_terrain(nb,matrice):
    if nb<matrice[0]:
        return (0,0,128)
    if nb<matrice[1]:
        return (0,148,149)
    if nb<matrice[2]:
        return (255,255,26)
    if nb<matrice[3]:
        return (0,128,0)
    if nb<matrice[4]:
        return (45,43,34)
    return (255,255,255)


def creation_map(taille,sortie="Couleur",echelle=0.5,couche=4,impacte=0.5,lacunariter=2,matrice=(60,120,140,170,210),graine=randint(0,100),multiplicateur_de_terre=2):
    map_neb=Image.fromarray(map_noise(taille,echelle,couche,impacte,lacunariter,graine),mode="L")
    if sortie=="Couleur":
        data=[]
        for i in range (taille[0]):
            for j in range(taille[1]):
                data.append(coul_terrain(map_neb.getpixel((i,j)),matrice))
        map_coul=Image.new("RGB",taille)
        map_coul.putdata(data)
        map_coul.save("carte aleatoire.jpg")
    else:map_neb.save("noise.jpg")

##a=Image.new("RGB",(250,250),(0,0,0))
##b=ImageDraw.Draw(a)
##b.line(((12,75),(75,86),(75,38),(98,75)),(255,255,255),2)
##a.show()
##creation_chemin((500,250))