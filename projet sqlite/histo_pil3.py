import sqlite3
import datetime
import base64
import hashlib
import os
from io import BytesIO

from tkinter import *
from PIL import Image



def __recuperation_date_heure__():
    date=datetime.datetime.now()
    return ("{}/{}/{}".format(date.year,date.month,date.day),
            "{}:{}".format(date.hour,date.minute))

def ajout_historique(image,nom=None):
    connection=sqlite3.connect("Historique.db")
    cursor=connection.cursor()
    try:
        cursor.execute("""CREATE TABLE historique (date TEXT,
                                               heure Text ,
                                               nom text,
                                               mode text,
                                               data BLOB  ,
                                               taille text,
                                               id text primary key)""")
    except:
        pass
    mode=image.mode
    date,heure=__recuperation_date_heure__()
    taille=image.size
    image.save("nom_random_pour_etre_sur_que_personne_ne_lutilise.jpg")
    with open("nom_random_pour_etre_sur_que_personne_ne_lutilise.jpg","rb") as image_file:
        data=base64.b64encode(image_file.read())
    insert="insert into historique values (?,?,?,?,?,?,?)"

    h = hashlib.new('sha256')
    h.update(data)
    cle=h.hexdigest()
    valeur=(date,heure,nom,mode,data,str(taille),cle)
    try:
        cursor.execute(insert, valeur)
    except sqlite3.IntegrityError:
        cursor.execute("select date,heure from historique WHERE id='{}'".format(cle))
        date_et_heure=cursor.fetchone()
        print("l'image a déjà été sauvgardé le {}".format(date_et_heure))
        connection.rollback()
    finally:
        os.remove("nom_random_pour_etre_sur_que_personne_ne_lutilise.jpg")
        connection.commit()
        connection.close

def interogation(date=None,Heure=None,Nom=None,Id=None):
    """Interogation possible:
            date
            date+heure
            nom
            Id
    """
    connection=sqlite3.connect("Historique.db")
    cursor=connection.cursor()
    try :
        if date!=None and Heure==None:
            cursor.execute("select * from historique where date='{}'".format(date))
        elif date!=None and Heure!=None:
            cursor.execute("select * from historique where date='{}' and heure='{}'".format(date,Heure))
        elif Nom!=None:
            cursor.execute("select * from historique where nom='{}'".format(Nom))
        elif Id!=None:
            cursor.execute("select * from historique where id='{}'".format(Id))

        rep=cursor.fetchall()



    except:
        print("une erreur est survenue")
        connection.rollback()
        return
    finally:
        connection.close
    return rep
def recuperation_image(Id):
    connection=sqlite3.connect("Historique.db")
    cursor=connection.cursor()
    cursor.execute("select data from historique where id='{}'".format(Id))
    img = Image.open(BytesIO(base64.b64decode(cursor.fetchone()[0])))
    return img

def visualisation(Id):
    connection=sqlite3.connect("Historique.db")
    cursor=connection.cursor()
    cursor.execute("select data from historique where id='{}'".format(Id))
    img = Image.open(BytesIO(base64.b64decode(cursor.fetchone()[0])))
    return img.show()
def requete():

    fenetre = Tk()

    champ_label = Label(fenetre, text="requete sql")




    var_entre_date = StringVar() # créer variable de choix
    var_entre_heure = StringVar()
    var_entre_nom = StringVar()
    var_entre_id = StringVar()
##    choix_date = Radiobutton(fenetre, text="date", variable=var_choix, value="rouge")
##    choix_heure = Radiobutton(fenetre, text="Heure", variable=var_choix, value="vert")
##    choix_nom = Radiobutton(fenetre, text="Nom", variable=var_choix, value="bleu")
##    choix_id = Radiobutton(fenetre, text="Id", variable=var_choix, value="Id")
    label_date=Label(fenetre,text='date')
    label_date_info=Label(fenetre,text="Format: année/mois/jours")
    label_heure=Label(fenetre,text='heure')
    label_heure_info=Label(fenetre,text='Format: heure:minute')
    label_nom=Label(fenetre,text='nom')
    label_id=Label(fenetre,text='id')
    date_entry=Entry(fenetre,textvariable=var_entre_date)
    heure_entry=Entry(fenetre,textvariable=var_entre_heure)
    nom_entry=Entry(fenetre,textvariable=var_entre_nom)
    id_entry=Entry(fenetre,textvariable=var_entre_id)

    bouton_lancement = Button(fenetre, text="recherche",command=lambda:requete_intero(var_entre_date.get(),var_entre_heure.get(),var_entre_nom.get(),var_entre_id.get()))
    print("ce qui est fait après que j'ai créé le boutton")

    label_date.grid(row=0,column=0)
    date_entry.grid(row=0,column=1)
    label_date_info.grid(row=0,column=2)
    label_heure.grid(row=1,column=0)
    heure_entry.grid(row=1,column=1)
    label_heure_info.grid(row=1,column=2)
    label_nom.grid(row=2,column=0)
    nom_entry.grid(row=2,column=1)
    label_id.grid(row=3,column=0)
    id_entry.grid(row=3,column=1)

    bouton_lancement.grid(row=4,column=1)


##    champ_label.pack()
##    choix_date.pack()
##    choix_heure.pack()
##    choix_nom.pack()
##    choix_id.pack()
##    bouton_quitter.pack()



    fenetre.mainloop()
def requete_intero(date,heure,nom,idd):
    if date=="":
        date=None
    if heure=="":
        heure=None
    if nom=="":
        nom=None
    if idd=="":
        idd=None
    print(date,heure,nom,idd)
    print(type(date),type(heure),type(nom),type(idd))
    print(interogation(date,heure,nom,idd))



if __name__ == '__main__':
    visualisation("e1909891607bc05bf94ff0f5774c6816ee9c326b9e6bafe3f255c658535d479b")
##    requete()
