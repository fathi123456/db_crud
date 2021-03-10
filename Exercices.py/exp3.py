import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="centre"
)
class formation:
    def __init__(self,titre,prix,durée,formateur):
        self.titre=titre
        self.prix=prix
        self.durée=durée
        self.formateur=formateur
    def affiche(self):
        print("la formation est formé de : %s %s %s %s"%(self.titre,self.prix,self.durée,self.formateur))
    def ajoutformation(self):
        mycursor = mydb.cursor()
        sql = "NSERT INTO `formation`(`titre`, `prix`, `duree`, `formateur`) VALUES  (%s, %s,%s,%s)"
        val = (self.titre,self.prix,self.durée,self.formateur)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "formation ajouter")


#f1=formation("python",300,20,"khalil")
#f1.affiche()