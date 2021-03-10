classe principale
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="productsdb"
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
    def read(self):
        while(self.titre==""):
            self.titre=input("titre=? ")
        while(self.prixu<1):
            self.prixu=float(input("donner votre prix d'achat"))
        while(self.prixv<1 or self.prixv<self.prixu):
            self.prixv=float(input("donner le prix de vente"))
        while(self.quantite<1):
            self.quantite=int(input("donner la quantité"))
    def detailles(self):
    def add(self):
        mycursor = mydb.cursor() #placer le curseur en pointant sur la DB
        sql = "INSERT INTO `produit`( `titre`, `prixu`, `prixv`, `quantite`) VALUES  (%s, %s,%s,%s)" #syntaxe de query
        val = (self.titre,self.prixu, self.prixv,self.quantite) #paramétres de query
        mycursor.execute(sql, val) #demande d'exécution
        mydb.commit() #verification et validation
        print(mycursor.rowcount, "record inserted.") #informer le dev
    def afficher(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from produit")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)



#programme de test
"""
pr1=produit("MSI gamer",3700,4100,2)
chiffre=pr1.gain_brute()
print("votre chiffre de gain estimé est de : %s"%(chiffre))
taxes=pr1.taxe()
print("la taxe unitaire à payer est de %s"%(