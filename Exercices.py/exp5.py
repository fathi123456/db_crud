from exp4 import *
from exp3 import *

def ajoutformation(titre,formateur,prix,durée):
    while(titre==""):
        titre=input("donner le titre de formation :")
    while(formateur==""):
        formateur=input("donner le nom de formateur  :")
    while(prix<30):
        prix=int(input("donner le prix de formation :"))
    while(durée<10):
        durée=int(input("denner le nombre des heures :"))
    f=formation(titre,prix,durée,formateur)
    f.ajoutformation()
def ajoutcondidat(nom,prenom,adresse,teliphone):
    while(nom==""):
        nom=input("entrer le nom ")
    while(prenom==""):
        prenom=input("entrer prenom ")
    while(adresse==""):
        adresse=input("entrer adressse ")
    while(teliphone==""):
        teliphone=input("entrer le teliphone ")
    c=condidat(nom,prenom,adresse,teliphone)
    c.ajoutcondidat()
choix=""
while(choix!="q"):

    choix=input("tapez f pour ajouter une formation et c pour ajouter  un candidat q pour quitter")
    if(choix=="q"):
        break
    elif(choix=="c"):
        ajoutcondidat("","","","")
    elif(choix=="f"):
        ajoutformation("","",0,0)
    else:
        print("je ne comprend pas")