import matplotlib.pyplot as plt
from numpy import interp, linspace
from matplotlib import style

#Initialisation
dx = 0.001
decal = 100
composanteVer = 0.498
precision = 1000 #pour changer le nombre des digits affiché aprés la vérgule
print("Il faut savoir que pour des grandes valeur de dx il faut prendre des petite valeurs pour le decalage decal.")
print("------------------------------------------------")
print("Le plus dx est petite le plus des valeurs de pentes doivent etre calculée, le plus le temps nécessaire pour éffectuer le calcule. Ne pas dépasser 0.0001 au maximum.")#ila drti dx<0.0001 lpc dyalk aytplonta hit aykhso ihsb bzaaf dlmrat so bla matjrbha :)
print("------------------------------------------------")

#Les valeurs trouvées pendans l'éxpirience de dosage:
X = [3.5,4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14]
Y = [0.498,0.507,0.51,0.519,0.52,0.524,0.543,0.542,0.575,0.57,0.619,0.91,0.98,0.988,0.993,0.996,1.001,1.01,1.012,1.014,1.014,1.014,1.014,1.017,1.021,1.025,1.026,1.026,1.027,1.028,1.029]


def La_plus_grande_pente(NX,D): #cette fonction donne les cordonneés du point ou il'ya la plus grande variation
    #vous pouvez ajuster la valeur de 'decal' pour varier la position de la pente entre les deux pentes maximales
    penteMax = max(D)
    index_pr_pente_max = D.index(penteMax)
    nbr_pentes_max = D.count(penteMax)
    return (NX[index_pr_pente_max]+NX[index_pr_pente_max + nbr_pentes_max -1 + decal])/2

def derive(X,Y):
    d=[]
    NX = linspace(min(X),max(X),int((max(X)-min(X))/dx),endpoint=False)
    for i in NX:
        fx = interp(i, X, Y)
        fx_plus_dx = interp(i+dx, X, Y)
        d.append((fx_plus_dx-fx)/dx + composanteVer)
    return NX,d
    
print("Calcule de",int((max(X)-min(X))/dx),"pentes...")
print("------------------------------------------------")
NX,D = derive(X,Y)
print("Calcule terminé.")


#les cordonneés de la plus grange pente:
Xp = La_plus_grande_pente(NX,D)
Yp = interp(Xp, X, Y)

#Initialisation:
plt.suptitle('E = f(V)')
plt.xlabel('V(mL)')
plt.ylabel('E(V)')

#Creation du graph
plt.plot(X, Y)
plt.plot(NX, D, color='green')

#Creation du point (Xp,Yp)
plt.plot(Xp,Yp, marker='o')

#Creation de la ligne verticale
plt.axvline(x=Xp,color='orange',linestyle='--')


#Creation du text qui indique les cordonneés (Xp,Yp)
plt.text(Xp+0.3, Yp-0.05, f"({float(int(Xp * precision))/precision}mL,{float(int(Yp * precision))/precision}V)")
plt.show()

#Made by Jonas.





