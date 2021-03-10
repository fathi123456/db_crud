import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="demo"
)
titre=""
p=0 
titre=input("donner le titre")
while p<=0:
    p=int(input("donner leprix"))
titre=input("donner le titre")
produit(titre,p)
def produit (titre,p)

mycursor = mydb.cursor()
sql = "INSERT INTO `produit`(`titre`, `prix`) VALUES( %s,%s)"
val = (titre, p)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
