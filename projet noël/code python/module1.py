from PIL import Image, ImageDraw
def carré(calc,abcd,rep,coul):
    ab=(abcd[1][0]-abcd[0][0])/3
    if ab<1 or rep==0:
        return calc.rectangle((abcd[0],abcd[2]),coul)
    e,f=(abcd[0][0]+ab,abcd[0][1]),(abcd[0][0]+2*ab,abcd[0][1])
    l,k=(abcd[0][0],abcd[0][1]+ab),(abcd[0][0],abcd[0][1]+2*ab)
    g,h=(abcd[1][0],abcd[1][1]+ab),(abcd[1][0],abcd[1][1]+ab*2)
    j,i=(abcd[3][0]+ab,abcd[3][1]),(abcd[3][0]+2*ab,abcd[3][1])
    m,n,o,p=    (e[0],l[1]),\
                (f[0],l[1]),\
                (f[0],k[1]),\
                (e[0],k[1])
    aeml,efnm,fbgn,ngho,ohci,poij,kpjd,lmpk=(abcd[0],e,m,l),\
                                            (e,f,n,m),\
                                            (f,abcd[1],g,n),\
                                            (n,g,h,o),\
                                            (o,h,abcd[2],i),\
                                            (p,o,i,j),\
                                            (k,p,j,abcd[3]),\
                                            (l,m,p,k)
    carres=[aeml,efnm,fbgn,ngho,ohci,poij,kpjd,lmpk]
    for x in range(8):
        carré(calc,carres[x],rep-1,coul)

def creation_tapi(rep,taille=1000,font=(0,0,0),coul=(255,255,255)):
    ima=Image.new("RGB",(taille,taille),font)
    calc=ImageDraw.Draw(ima)
    a,b,c,d=(20,20),\
            (taille-20,20),\
            (taille-20,taille-20),\
            (20,taille-20)
    carré(calc,(a,b,c,d),rep,coul)
    ima.save("tttttt.jpg")

creation_tapi(10,10000)

