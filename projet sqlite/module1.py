from histo_pil3 import *
from PIL import Image

image1=Image.new("RGB",(75,7788),(78,2,5))
image2=Image.new("RGB",(795,7568),(178,75,35))
image3=Image.open("mandelbrot_zoom.jpg")
ajout_historique(image1,'mon super nom')
ajout_historique(image2,'mon super nom')
ajout_historique(image3,'mon super nom')
ajout_historique(image1,'mon super nom')

requete()
visualisation("85744bdb323071ab5efa2ed30ef4a278a07fea2f5dc85adf0ee185644731b9df")
img=recuperation_image("1118a60890e56650d56d81a20f8c85d546be060d547d825927d1aa9031f572ed")
img.save("sa a marcher .jpg")