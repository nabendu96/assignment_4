# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:08:23 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

n=10000

#Box-Muller method to generate random numbers distributed according to a Gaussian distribution with mean=0 and variance=1
x1=np.random.rand(n)
x2=np.random.rand(n)
r=np.sqrt(-2*np.log(1-x1))
theta=2*np.pi*x2
x=r*np.cos(theta)            #1st set of Gaussian random numbers
y=r*np.sin(theta)            #2nd set of Gaussian random numbers

z=np.linspace(-5,5,1000)

plt.hist(x,range=(-5.0,5.0),bins=20,density=True,label=r'Box-Muller randoms')                    #density histogram of the generated numbers 
plt.plot(z,(1/np.sqrt(2*np.pi))*np.exp(-z*z/2),lw=3,color='r',label=r'Gaussian PDF')             #plotting Gaussian pdf
plt.xlabel(r'$x_i$',fontsize=20)
plt.ylabel(r'$PDF$',fontsize=20)
plt.legend()
plt.show()
