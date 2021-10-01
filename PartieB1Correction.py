#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:19:53 2021

@author: nilsbarrellon
"""

#Application 6
nb = int(input("Entrez un nombre :"))
if nb == 0:
    print("Ce nombre est nul")
elif nb%2==0:
    print("Ce nombre est pair")
else:
    print("Ce nombre est impair")
 
#Application 7
a = 7
b = 51
c = 13
maxi = 0
if (a<b):
    if (b<c):
        maxi = c
    else:
        maxi = b
else:
    if (a<c):
        maxi = c
    else:
        maxi = a
print("Le maximum vaut ",maxi)

#Application 8
H = []
g = 10
m = 0.2
for t in range(0,11):
    H.append(0.5*g*t*t)
print(H)

Ep=[]
for i in range(0,11):
    Ep.append(m*g*H[i])
print(Ep)

M=[]
for element in Ep:
    if element<=200:
        M.append(element)
print(M)

#Application 10
N=[]
dx = 0.2
n = 2
while n>=0:
    N.append(round(n,1))
    n = n-dx
print(N)

#Application 11
n1 = 2.6
n2 = 1.2
while (n2>0) and (n1>0):
    n2 = round(n2-dx,1) 
    n1 = round(n1-2*dx,1)
if n1>n2:
    print("Le réactif limitant est R2 et il reste ",n1, "mol de R1")
else:
    print("Le réactif limitant est R1 et il reste ",n2, "mol de R1")
    

