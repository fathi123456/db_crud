#classe principale
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="fathi"
)    
class produit:
    def __init__(self,titre,prixu,prixv,quantite):
        self.titre=titre
        self.prixu=prixu
        self.prixv=prixv
        self.quantite=quantite
    def gain_brute(self):
        gain=(self.prixv-self.prixu)*self.quantite
        return gain
    def taxe(self):
        if(self.prixv<100):
            return self.prixv*0.04
        elif(self.prixv<500):
            return self.prixv*0.09
        else:
            return self.prixv*0.12
    mycursor = mydb.cursor()
    sql = "INSERT INTO `produit`(titre`, `produitu`, `produitv`, `quantité`)  VALUES (%s, %s,%s,%s)"
    val = (titre,produitu,produitv,quantite)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    

#programme de test
pr1=produit("MSI gamer",3700,4100,2)
chiffre=pr1.gain_brute()
print("votre chiffre de gain estimé est de : %s"%(chiffre))
