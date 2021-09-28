#Application 15
from random import randint
print(randint(1,6))

#Application 16
import math
v0 = float(input("Entrez la valeur initiale"))
v0x = round(v0*math.cos(math.radians(60)),2)
v0y = round(v0*math.sin(math.radians(60)),2)
print("Coordonnées de la vitesse (",v0x,",",v0y,")")
