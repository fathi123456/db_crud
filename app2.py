def imc(t,p):
    return p //( t*t ) 
def decrire(t,p):
    if(imc(t,p)<20):
        print("megre")
    elif(imc(t,p)<=25):
        print("ideal")
    elif(imc(t,p)<=30):
        print("surpoid")
    else:
        print("epese")
v=imc(1.77,62)
print("le imc est "+str(v))
decrire(1.77,62)

        

