import time
from PIL import Image, ImageDraw
from random import randint,uniform
from decimal import Decimal
from cmath import cos,sinh,sin,cosh,log
from math import ceil

def creation_mandelbrot(taille,debut_x=-2,debut_y=-1.5,fin_x=1,fin_y=1.5,pressision=500):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(quadratique(complex(0,0),co_point([k,j],taille[0],debut_x,fin_x,debut_y,fin_y),pressision)))
    return font_plan.save("mandelbrot.jpg")

def coul(longeur_Onde):
    couleur =()
    if longeur_Onde<60:couleur=(int(-(longeur_Onde-60)/(60-0)*255),0,255)
    elif longeur_Onde<110:couleur=(0,int((longeur_Onde-60)/(110-60)*255),255)
    elif longeur_Onde<130:couleur=(0,255,int(-(longeur_Onde-130)/(130-110)*255))
    elif longeur_Onde<200:couleur=(int((longeur_Onde-130)/(200-130)*255),255,0)
    elif longeur_Onde<265:couleur=(255,int(-(longeur_Onde-265)/(265-200)*255),0)
    elif longeur_Onde<=270:couleur=(255,0,0)
    else:couleur=(0,0,0)
    return couleur
def co_point(co,taille,debutx,finx,debuty,finy):
    r=debutx+((finx-debutx)/taille)*co[0]
    i=debuty+((finy-debuty)/taille)*co[1]
    return complex(r,i)
def puissance(z,constante,pressision):
    i=0
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<5 and rep<=pressision:
        rep+=1
        while dis<4 and i<271:
            z=z**2+constante**3-1.401155
            i+=1
            dis=z.imag**2+z.real**2
    return i
def sinu(z,constante,pressision):
    i=0
    if constante==0:return 271
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<200 and rep<=pressision:
        rep+=1
        while dis<200 and i<271:
            z=sinh(z)+(1/(constante**2))
            i+=1
            dis=z.imag**2+z.real**2
    return i




def cosi2(z,constante,pressision):
    i=0
    if constante==0:return 271
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<5 and rep<=pressision:
        rep+=1
        while dis<10 and i<271:
            z=z**0.89+5*constante-z**2
            i+=1
            dis=z.imag**2+z.real**2
    return i

def conjug(z,constante,pressision):
    i=0
    rep=1
    z=complex(0,1)
    dis=constante.imag**2+constante.real**2
    while dis<5 and rep<=pressision:
        rep+=1
        while dis<4 and i<271:
            z=z**2+sin(constante**3)
            z=z.conjugate()
            i+=1
            dis=z.imag**2+z.real**2
    return i

def lnnn(z,constante,pressision):
    i=0
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<5 and rep<=pressision:
        rep+=1
        while dis<2500 and i<271:
            z=cosh(log(z**2-constante**2))
            i+=1
            dis=z.imag**2+z.real**2
    return i

def ln (x):
##    if x>0:
        fract=(1-x)/(x + 1)
        nb_base=1
        somme=0
        for i in range(10000):
            somme=somme+(1/nb_base)*(fract**nb_base)
            nb_base+=2
        return -2*somme
def quadratique(z,constante,pressision):
    i=0
    rep=0
    dis=constante.imag**2+constante.real**2
    while dis<4 and rep<=pressision:
        i=0
        rep+=1
        if rep ==1:
            while dis<4 and i<470:
                z=z**2+constante
                i+=1
                dis=z.imag**2+z.real**2
        else:
            while dis<4 and i<270:
                z=z**2+constante
                i+=1
                dis=z.imag**2+z.real**2
    if rep==1:
        return i-200
    if rep>pressision:
        return i+1

    return i
creation_mandelbrot((5000,5000),0.00164372195,0.82246763327,0.00164372199,0.82246763331,1200)

##0.001643721971153
##0.822467633298876i

##-1.74995768370609350360221450607069970727110579726252077930242837820286008082972804887218672784431700831100544507655659531379747541999999995
##0.00000000000000000278793706563379402178294753790944364927085054500163081379043930650189386849765202169477470552201325772332454726999999995
##creation_mandelbrot((10,10),-1.74995768369,-0.000000000001,-1.74995768371,0.000000000001,5000000)
##creation_mandelbrot((2500,2500),-1.74995768370605,-0.00000000000005,-1.74995768370614,0.00000000000005)

##def cosin(constante):
##    if constante==complex(0,0):return 300
##    i=0
##    z=constante
##    while z.imag**2+z.real**2<50 and i<201:
##        z=cos(z/constante)
##        i+=1
##    if i ==201:return(401)
##    return i+100
##creation_mandelbrot((2000,2000),-1.75,-1.75,1.75,1.75)

##creation_mandelbrot((500,500),-2,-2,2,2,300)