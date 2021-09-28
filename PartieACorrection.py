#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:36:42 2021

@author: nilsbarrellon
"""

#Application 4
n0 = 1.80
dx = 0.10
n1 = n0 - 2*dx
n2 = n1 - 2*dx
print("n1=",n1)
print("n2=",n2)

G=6.67e-11
mT = 5.97e24
R = 6371e3

g = G*mT / (R*R)
print("g=",round(g,2))

#Application 5
a = 9.8324
g = round(a,1)
print("g=",g,"N/kg")

L = [2,6,4,8,10]
print(7 in L)
L2 = L[1:4]
print(L2)
L[0]=1
print(L)
L.append(12)
print(L)
L.pop(2)
print(L)
print("Somme des élements=",sum(L))
print("maximum de la liste=",max(L))
print("Minimum de la liste=",min(L))
print("Nombre d'elements de la liste:",len(L))

#Application 5bis
cTitrant = float(input("Concentration titrant ="))
vEq = float(input("Volume équivalent ="))
vPE = float(input("Volume prise d'essai ="))
cTitre = cTitrant*vEq/vPE
print("La concentration du titré est ",round(cTitre,3)," mol/L")