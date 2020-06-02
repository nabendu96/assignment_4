# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:52:12 2020

@author: nabendu
"""

#plotting of the numerical data obatined by running Prob_4.c

import numpy as np
import matplotlib.pyplot as plt

file=open('Prob_4.txt','r')
y=[]

for line in file:
    y.append(float(line))

z=np.linspace(0,5,1000)

mu=0.5              #mean

plt.hist(y,range=(0.0,5.0),bins=20,density=True,label=r'Transformation randoms')    
plt.plot(z,(1/mu)*np.exp(-z/mu),lw=3,color='r',label=r'exponential pdf')
plt.xlabel(r'$x_i$',fontsize=20)
plt.ylabel(r'$PDF$',fontsize=20)
plt.legend()
plt.show()
