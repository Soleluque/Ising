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


suma=0

with open("integral.txt", "r") as file:
    plots = csv.reader(file, delimiter = " ")
    for row in plots:
        x.append(float(row[0]))
        


for i in range(99999):
    suma+=(x[i*10]**2)
    
suma=suma/99999

print(suma)

plt.hist(x,bins=240)

#plt.axis([-1,1,0,18000])

plt.xlabel('x')
plt.ylabel('Numero de veces')
plt.title("Histograma")

plt.savefig("gaussiana05.png")


#plt.show()