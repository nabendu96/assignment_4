# -*- coding: utf-8 -*-
"""
Created on Sun May 24 09:32:41 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

#magic numbers
a=1103515245           #multiplier
c=12345                #increment
m=2**31                #modulus
x=1                    #seed

n=10000

lcg=np.zeros(n)

#lcg algorithm to generate uniformly distributed random integers in the range [0,m)
for i in range(n):
    x=(a*x+c)%m
    lcg[i]=x
    
lcg=lcg/m            #to obtain random numbers in the range [0,1)

plt.hist(lcg,range=(0.0,1.0),density=True,label=r'density histrogram of lcg randoms')              #density histogram of the generated numbers
plt.plot(np.linspace(0,1,n),np.ones(n),lw=3,color='r',label=r'uniform pdf')                        #plotting uniform pdf
plt.xlabel(r'$x_i$',fontsize=20)
plt.ylabel(r'$PDF$',fontsize=20)
plt.legend()
plt.show()
