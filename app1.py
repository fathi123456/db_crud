p=0
t=0
while t<1.20 or t>2.5:
    t=float(input("donner votre taille t:"))
while p<30 or p>200:
    p=float(input("donner votre poids p:"))
imc=p//(t*t) 
if imc>=0 and imc<20:
    print("personne maigre")
elif imc>=20 and imc<=25:
    print("personne idéal")
elif imc>25 and imc<30:
    print("personne superpoid")
else:
    print("personne opesé ")
g=0
while g<0.1 or g>3:
    g=float(input("entre glycemie :"))
if g>=0.1 and g<0.7:
    print("hypoglycemie")
elif g>=0.7 and g<1.2:
    print("glycemie ideal")
else:
    print("huperglycemie")
r=0
while r<40 or r>200:
    r=int(input("entrer rythme cardiaque:"))
if r>=40 and r<60:
    print("insuffisance")
elif r>=60 and r<=75:
    print("rythme ideal")
else:
    print("rythme fort")
