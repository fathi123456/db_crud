  
import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="centre"
)

class condidat:
    def __init__(self,nom,prenom,adresse,teliphone):
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.teliphone=teliphone
    def affiche(self):
        print("le condidat est appelé %s %s et son adresse est %s et son teliphone est %s :"%(self.nom,self.prenom,self.adresse,self.teliphone))
    def ajoutcondidat(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO `condidat`(`nom`, `prenom`, `adressse`, `teliphone`) VALUES  (%s, %s,%s,%s)"
        val = (self.nom,self.prenom,self.adresse,self.teliphone)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "condidat ajouter")

#f2=condidat("fathi","zebaa","mareth","29730654")
#f2.affiche()