from PIL import Image, ImageDraw

class image_texte:
    def set_texte(a,lien):
        fichier = open(lien, 'r')
        texte=""
        for ligne in fichier:
            texte+=ligne
        fichier.close()
        return texte

    def get_image(self):
        img=Image.new("RGBA",self.lh,(255,255,255,0))
        texte=ImageDraw.Draw(img)
        self.calc=texte
        texte.multiline_text((0,0), self.texte, fill=(255,255,255,255),spacing=self.traitement())

        self.img=img


    def traitement(self):
        space=10
        size=self.calc.textsize(self.texte,spacing=space)
        while size>self.lh:
            if space<0:return 1
            space-=0.1
            size=self.calc.textsize(self.texte,spacing=space)
        return space

    def sauve():
        pass
    def __init__(self,lh,lien):
        self.texte=self.set_texte(lien)
        self.lh=lh
        self.get_image()





if __name__=="__main__":
    a=image_texte((800,800),"README.md")
    p=a.texte
    img=a.img
    img.save("teste.jpg")
##    a=ImageDraw.multiline_textbbox((0,0),p)

