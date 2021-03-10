import mysql.connector
#pip install mysql-connector
mydb = mysql.connector.connect(
host="localhost",
user="root", #username par defaut
passwd="", #password par defaut
database="demo"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT titre,prix from produit ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
