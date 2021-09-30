#petite fonction d'affichage plus propre pour les polynomes
def affiche_polynome(polynome,variable):
    po = ""
    polynome = list(polynome)
    polynome.reverse()
    for i in range(len(polynome)):
        if i>1:
            po += str(round(polynome[i],2))+variable+"^"+str(i)
            if i!=len(polynome)-1:
                po +=" + "
        elif i==1:
            po+= str(round(polynome[i],2))+variable+" + " 
        else:
            po+=str(round(polynome[i],2)) + " + "
    print(po)
 #Application 15
 from random import randint
 print(randint(1,6))
#
# #Application 16
 import math
 v0 = float(input("Entrez la valeur initiale"))
 v0x = round(v0*math.cos(math.radians(60)),2)
 v0y = round(v0*math.sin(math.radians(60)),2)
 print("Coordonnées de la vitesse (",v0x,",",v0y,")")

#Application 17
import numpy as np
import matplotlib.pyplot as plt
T = np.array([1,4,25,9])
print(2*T)
print(T+3)
print(T+[1,3,5,10])
print(T**2)
print(np.sqrt(T))
##########################
N = np.arange(0,5.5,0.5)
print(N)
M = np.linspace(0,5,11)
print(M)

#Application 18


###############################
print(np.roots([1,0,-1]))
##########################
affiche_polynome(np.polyfit([0,1,2,3,4,5],[-1,0,3,8,15,24],2),"x")
#
#######################
g = 10
v0 =10
x0 =3

terme2 = -0.5*g
sol = np.roots([-5,10,3])
for s in sol:
    if s>0 :
        print("Solution positive:",s)
##########################
#       
tableau_temps = np.linspace(0,10,21)
pos = []
for t in tableau_temps:
    pos.append(-5*pow(t,2)+10*t+3)
affiche_polynome(np.polyfit(tableau_temps,pos,2),"t")

#Application 19
x = [0, 0.45, 0.94, 1.37, 1.85, 2.28, 2.79, 3.20, 3.70, 4.12, 4.63]
dt = 0.2
m = 1
V=[]
for i in range(1,len(x)-1):
   V.append((x[i+1]-x[i-1])/(2*dt))
V=np.array(V)
Ec = V*(m/2)
print(Ec)

#Application 20
t = np.linspace(0,1,11)
print(t)
y = 5-5*t**2
print(y)  
plt.plot(t,y,color="red")
plt.grid()
plt.xlabel("t (en s)", fontsize=12)
plt.ylabel("y (en m)", fontsize=12)
plt.title("y=f(t)", fontsize=12)
plt.xlim(0,0.8)

#Application 21 : représenter un vecteur
for i in range(len(t)):
    plt.arrow(t[i],y[i],0,-1, head_width=0.05, head_length=0.15, fc='lightblue', ec='black')
plt.show()

#Application 22
import csv
with open("valeur.csv","r") as f:
    classeur = csv.reader(f,delimiter=",")
    tableau = []
    for ligne in classeur:
        tableau.append(ligne)
print(tableau)
t = []
x = []
for coordonnee in tableau:
    t.append(float(coordonnee[0].replace(",",".")))
    x.append(float(coordonnee[1].replace(",",".")))
print(t)
print(x)