#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:00:22 2019

@author: sol
"""
import csv
import math as m
import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]

with open("pa.txt", "r") as file:
    plots = csv.reader(file, delimiter = " ")
    for row in plots:
        if float(row[1])!=0.0:
            x.append(float(row[1])) #pa
            y.append(float(row[0])) #delta
        
        
        
plt.plot(y,x)

plt.xlabel('Paso delta')
plt.ylabel('Probabilidad de aceptación')
plt.title("Probabilidad de aceptación en función de delta")

plt.savefig("padelta.png")





print(y[x.index(0.508267)])


       


