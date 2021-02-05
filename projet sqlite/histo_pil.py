import sqlite3
import datetime
import base64
import hashlib
import os
from io import BytesIO
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
##    data=cursor.fetchone()
##    print(data,type(data))
    img = Image.open(BytesIO(base64.b64decode(cursor.fetchone()[0])))
    return img.show()

if __name__ == '__main__':
    a=interogation(Nom="mon super nom")
    ii=recuperation_image('057f1b2ce4fa67e40a9be13985593eb020d44314c98df14f4863396503c4e2e9')

