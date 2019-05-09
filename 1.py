#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:54:06 2019

@author: sol
"""

import csv
import math as m
import matplotlib.pyplot as plt

x=[]
y=[]

suma=0

with open("integral.txt", "r") as file:
    plots = csv.reader(file, delimiter = " ")
    for row in plots:
        x.append(float(row[0]))
        
X=list(set(x))

X.sort()
        
for i in range(len(X)):
    y.append(m.exp((-(X[i])**2)/2))
    


for i in range(len(X)-1):
    suma+=(X[i]**2)*y[i]*(X[i+1]-X[i])

print(suma)

plt.plot(X,y,"o")

plt.xlabel('exp(-x2/2)')
plt.ylabel('x')
plt.title("Distribución Gaussiana")

plt.savefig("gaussiana05.png")


plt.show()