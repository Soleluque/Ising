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
xsd=[]
msd=[]
ceros=[]

vme=[]
ys2=[]

vm2=[]

chi=[]


for i in range(51):
    xs.append([])
    ms.append([])
    #es.append([])
    xsd.append([])
    msd.append([])
    ys2.append([])

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
            
for i in range(len(xs)):
    for k in range(len(xs[i])):
        if k%1024==0:
            xsd[i].append(xs[i][k])
            msd[i].append(ms[i][k])

for i in range(len(ms)):
    vmm.append(st.mean(msd[i]))
    
for i in range(len(vmm)):
    vmm[i]=vmm[i]/1024
    
    
for i in range(len(msd)):
    for k in range(len(msd[i])):
        ys2[i].append(msd[i][k])
        
for i in range(len(msd)):
    for k in range(len(msd[i])):
        msd[i][k]=msd[i][k]**2
        

for i in range(len(ys2)):
    
    vm2.append(st.mean(ys2[i])/1024)

for i in range(len(vmm)):
    chi.append(vm2[i]-(vmm[i]**2))
    
for i in range(len(chi)):
    chi[i]=chi[i]    


#for i in range(501):
#    vme.append(st.mean(es[i]))
    
j=np.array(j)

#plt.plot(xs[0],ms[0],"o--")
ajustem=(1-(np.sinh(2*j))**(-4))**(1/8)

for i in range(30):
    ceros.append(0)

plt.plot(j,np.abs(vmm),"o",label="Datos")
plt.plot(j,ajustem,"-r",label="Ajuste teorico")
plt.plot(j[:30],ceros,"-r") #esto así no va

plt.xlabel('J*')
plt.ylabel('Magnetizacion')
plt.title("Magnetizacion en funcion de J/T")

plt.legend()

plt.savefig("magnetizacionb.png")

plt.show()


plt.plot(j,chi,"o")

plt.xlabel("J*")
plt.ylabel("Suceptibilidad")
plt.title("Suceptibilidad Media por Sitio")

plt.savefig("suceptibilidadb.png")

plt.show()
    
#plt.plot(j,vme,"o")

#plt.xlabel("J*")
#plt.ylabel("Energia")
#plt.title("Energia en funcion de J/T")

#plt.legend()

#plt.savefig("energiab.png")

#plt.show()

        

