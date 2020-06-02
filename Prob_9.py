# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:01:32 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

#the function to be sampled (need not be normalized)
def f(x):
    if(3<x<7):
        return(1.0)
    else:
        return(0.0)

nsteps=100000
theta=0.0

theta_arr=[]

theta_prime_arr=[]

for i in range(nsteps):
    theta_prime=theta+np.random.standard_normal()     #proposed theta #proposal pdf is Gaussian #numpy.random.standard_normal(): draw sample from a standard normal distribution with mean=0 and sd=1
    theta_prime_arr.append(theta_prime)    
    r=np.random.rand()
    #mcmc algorithm: we will stay in higher probable region
    if(f(theta)!=0.0):
        if(f(theta_prime)/f(theta)>r):
            theta=theta_prime
    else:
        theta=theta_prime
    theta_arr.append(theta)

#plotting Markov chain
plt.plot(theta_prime_arr,'.g',label=r'proposed points')
plt.plot(theta_arr,'.-r',label=r'Markov chain')
plt.xlabel(r'$step$',fontsize=20)
plt.ylabel(r'$\theta$',fontsize=20)
plt.title(r'Markov Chain',fontsize=20)
plt.legend()
plt.show()

z=np.linspace(3,7,1000)

#plotting pdf
plt.hist(theta_arr,range=(3.0,7.0),density=True,label=r'Metropolis randoms')
plt.plot(z,np.ones(1000)*0.25,lw=3,color='r',label=r'uniform pdf')
plt.xlabel(r'$x_i$',fontsize=20)
plt.ylabel(r'$PDF$',fontsize=20)
plt.title(r'PDF of uniform deviates using Metropolis algo',fontsize=20)
plt.legend()
plt.show()
