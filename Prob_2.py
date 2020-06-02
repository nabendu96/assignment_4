# -*- coding: utf-8 -*-
"""
Created on Sun May 24 07:55:01 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

n=10000

numpy_random=np.random.rand(n)        #generating uniformly distributed random numbers between 0 and 1 using numpy.random.rand()

plt.hist(numpy_random,range=(0.0,1.0),density=True,label=r'density histrogram of numpy randoms')            #density histogram of the generated numbers
plt.plot(np.linspace(0,1,n),np.ones(n),lw=3,color='r',label=r'uniform pdf')                                 #plotting uniform pdf
plt.xlabel(r'$x_i$',fontsize=20)
plt.ylabel(r'PDF',fontsize=20)
plt.legend()
plt.show()
