# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:33:11 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

#the error function (erf)
def f(x):
    return(np.sqrt(2/np.pi)*np.exp(-x*x/2))

#the non-trivial envelop function discussed in the class
def g(x):
    return(1.5*np.exp(-x))

N=100000

x=np.random.rand(N)
x=-np.log(1-x)                     #transformation method to get points under the exponential 
y=np.random.rand(N)*g(x)           #for each x let us get a value of y that is uniformly random between 0 and g(x) 

x_good=[]
y_good=[]

x_bad=[]
y_bad=[]

#rejection of bad points
for i in range(N):
    if(y[i]<f(x[i])):
        x_good.append(x[i])
        y_good.append(y[i])
    else:
        x_bad.append(x[i])
        y_bad.append(y[i])

z=np.linspace(0.0,10,1000)

plt.hist(x_good,range=(0.0,10.0),bins=20,density=True,label=r'density histrogram of rejection randoms')           #density histogram of the good points
plt.plot(z,f(z),lw=3,color='r',label=r'erf')                                                                      #plotting erf
plt.xlabel(r'$x_i$',fontsize=20)
plt.ylabel(r'$PDF$',fontsize=20)
plt.legend()
plt.show()

#plotting to show the good and bad points
plt.plot(x_good,y_good,'.g',label=r'good points')
plt.plot(x_bad,y_bad,'.c',label=r'bad points')
plt.plot(z,f(z),lw=3,color='r',label=r'erf')
plt.plot(z,g(z),lw=3,color='k',label=r'the nontrivial envelop')
plt.xlim(0.0,10.0)
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$f(x)$',fontsize=20)
plt.legend()
plt.show()
