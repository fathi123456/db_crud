  
import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="sante"
)
nom=""
age=0
etat=""
decision=""
while decision!="o":
    while age<12:
        age=(int(input("donner votre age")))
    while nom=="":
        nom=input("donner votre nom")
    while etat=="":
        etat=input("donner votre état de santé")

    # connexion mysql avec python
    mycursor = mydb.cursor()
    sql = "INSERT INTO `personne`( `nom`, `age`, `etat`) VALUES (%s, %s,%s)"
    val = (nom,age, etat)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    decision=input("arrêter ? (O pour oui)" )