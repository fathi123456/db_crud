class athlete:
    def __init__(self,nom,prenom,adresse,age,sport):
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.age=age
        self.sport=sport
    def affiche(self):
        print("athlete: %s %s %s ans"%(self.nom,self.prenom,self.age))
    def categorie(self):
        if (self.age>5 and self.age<12):
            return "mineur"
        elif(self.age>=12 and self.age<=18):
            return "genior"
        else:
            return "senior"
        



a1=athlete("ali","selmi","gabes",20,"footbal")
a2=athlete("karim","farid","mareth",18,"basketbool")
a3=athlete("imed ","samir","gabes",23,"box")
a1.affiche()
a3.affiche()
cat=a2.categorie()
a2.affiche()
print( cat)

