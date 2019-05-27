#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:50:47 2019

@author: matias
"""

import csv
import statistics as st
import numpy as np
import matplotlib.pyplot as plt

xs=[]
ys=[]
j=0
b=[]
e=[]

vm=[]

for i in range(191):
    xs.append([])
    ys.append([])
   

with open("magnetizaciona.txt", "r") as file:
    plots = csv.reader(file, delimiter = " ")
         
    for row in plots:
        if len(row)==1:
            b.append(float(row[0]))
            j=j+1
        if len(row)==2:
            xs[j-1].append(float(row[0]))
            ys[j-1].append(float(row[1]))
        


for i in range(191):
    vm.append(st.mean(ys[i]))
    
for i in range(191):
    vm[i]=vm[i]/256
    
        
for i in range(191):
    e.append(st.mean(ys[i]))
    

for i in range(191):
    e[i]=b[i]*e[i]
    e[i]=-e[i]
    
b=np.array(b)
            


plt.plot(b,vm,"o",label="Datos")
plt.plot(b,np.tanh(b),"-r",label="Ajuste teorico")

plt.xlabel('B*')
plt.ylabel('Magnetizacion')
plt.title("Magnetizacion por sitio en funcion del campo B/T")

plt.legend()

plt.savefig("magnetizaciona.png")


plt.show()

plt.plot(b,e,"o",label="Datos")
plt.plot(b,-256*b*np.tanh(b),"-r",label="Ajuste teórico")


plt.xlabel('B*')
plt.ylabel('Energia')
plt.title("Energia en funcion del campo B/T")

plt.legend()

plt.savefig("energiaa.png")


plt.show()


#print(st.mean(y))

#print(np.max(y))
#print(np.min(y))