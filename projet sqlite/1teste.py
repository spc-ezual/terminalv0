import sqlite3

connection=sqlite3.connect('data.db')

cursor=connection.cursor()
cursor.execute("drop table TESTE")
cursor.execute("CREATE TABLE TESTE ( NOM TEXT ,PRENOM TEXT,ID INTEGER PRIMARY KEY IDENTITY(1,1))")
try :
    cursor.execute("INSERT INTO TESTE VALUES ('kevin','gnnn',)")
    cursor.execute("INSERT INTO TESTE VALUES ('A','5',)")

##except sqlite3.OperationalError:
##
##    print ("Il y eu un probleme lors de l'enregistrement ")
##    connection.rollback()

finally:
    connection.commit()
    connection.close()
