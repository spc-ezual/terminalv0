from PIL import Image, ImageDraw
from random import randint
class image_triangle:
    def __init__(self,lh,nb):
        self.lh=lh
        self.img=Image.new("RGBA",lh,(255,255,255,0))
        for i in range (nb):
            self.un_triangle()
##        self.img=self.img.filter(5)
    def un_triangle(self):
        triangle=Image.new("RGBA",self.lh,(255,255,255,0))
        triangle_dessin=ImageDraw.Draw(triangle)
        longueur,hauteur=self.lh
        longueur,hauteur=longueur-1,hauteur-1
        point=[]
        for i in range (3):
            point.append((randint(0,longueur),randint(0,hauteur)))
        triangle_dessin.polygon(point,(randint(0,255),randint(0,255),randint(0,255),75))
        img=Image.alpha_composite(self.img,triangle)
        self.img=img

    def get_image(self):
        return self.img

    def sauv(self):
        img=self.img
        img.save("image_triangle.jpg")



if __name__ == '__main__':
    a=image_triangle((800,800),100)
    img=a.img
    img.save("testeee.jpg")
    a.sauv