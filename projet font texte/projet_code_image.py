from image_texte import *
from image_triangles import *
import sys
from PIL import Image

def regroupement(triangle,texte):
    out=Image.alpha_composite(triangle,texte)
    noir=Image.new("RGB",out.size,"black")
    noir.paste(out,mask=out.split()[3])
    return noir
def creation_img(lh,nb,lien):
    triangle=image_triangle(lh,nb)
    texte=image_texte(lh,lien)
    return triangle.img,texte.img
def recupertion_argument():
    return sys.argv

if __name__ =="__main__":
##    argument=recupertion_argument()
    argument=["py",800,800,100,"README.md"]
    lh=(argument[1],argument[2])
    nb_triangle=argument[3]
    lien=argument[4]
    triangle,texte=creation_img(lh,nb_triangle,lien)
    out=regroupement(triangle,texte)
    out.save("texte_triangle.jpg")