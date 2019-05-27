#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:33:47 2019

@author: sol
"""

import csv
import statistics as st
import numpy as np
import matplotlib.pyplot as plt

xs=[]
ms=[]
l=0
j=[]
#es=[]
#e=[]
vmm=[]

vme=[]

for i in range(500):
    xs.append([])
    ms.append([])
    #es.append([])
   

with open("magnetizacionb.txt", "r") as file:
    plots = csv.reader(file, delimiter = " ")
         
    for row in plots:
        if len(row)==1:
            j.append(float(row[0]))
            l=l+1
        if len(row)==2:
            xs[l-1].append(float(row[0])) #tiempo
            ms[l-1].append(float(row[1])) #magnetizacion
            #es[l-1].append(float(row[2])) #energia
            

for i in range(500):
    vmm.append(st.mean(ms[i]))
    
for i in range(500):
    vmm[i]=vmm[i]

#for i in range(500):
#    vme.append(st.mean(es[i]))
    
j=np.array(j)
ajustem=(1-(np.sinh(2*j))**(-4))**(1/8)


plt.plot(j,vmm,"o",label="Datos")
plt.plot(j,ajustem,"-r",label="Ajuste teorico")

#plt.xlabel('J*')
#plt.ylabel('Magnetizacion')
#plt.title("Magnetizacion en funcion de J/T")

#plt.legend()

#plt.savefig("magnetizacionb.png")

#plt.show()
    
#plt.plot(j,vme,"o")

#plt.xlabel("J*")
#plt.ylabel("Energia")
#plt.title("Energia en funcion de J/T")

#plt.legend()

#plt.savefig("energiab.png")

#plt.show()

        

