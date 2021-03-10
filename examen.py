class matiere:
    def __init__(self,titre,ds,tp,ef,coef):
        self.titre=titre 
        self.ds=ds
        self.tp=tp
        self.ef=ef 
        self.coef=coef
    def note(self):
        moyen=self.ds*0.3+self.tp*0.2+self.ef*0.5
        print("moyenne de %s est:  %s "%(self.titre,moyen))
mathematique=matiere("math",12,14,12,3)
arabe=matiere("arabe",13,15,8,2)
arabe.note()
mathematique.note()