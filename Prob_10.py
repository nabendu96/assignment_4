# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:38:43 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner

#ln L function:
def log_likelihood(theta,x,y,yerr):
    a,b,c=theta
    model=a*x*x+b*x+c
    sigma2=yerr**2
    return(0.5*np.sum((y-model)**2/sigma2+np.log(2*np.pi*sigma2)))       # actually negative ln L
 

#prior distribution p(m; b|I).
#We are a priori ignorant about the parameters so we choose a uniform prior    
def log_prior(theta):
    a,b,c=theta
    if(-500.0<a<500 and -500.0<b<500.0 and 0.0<c<1000.0):
        return(0.0)
    return(-np.inf)

#posterior PDF:    
def log_probability(theta,x,y,yerr):
    lp=log_prior(theta)
    if not(np.isfinite(lp)):
        return(-np.inf)
    return(lp-log_likelihood(theta,x,y,yerr))

#reading the datas and storing them in arrays 
file=open('data.txt','r').read().split('\n')          #the file 'data.txt' contains the given datas 
del file[0:5]     #deleting the first 5 lines which contain no data 
x=[]
y=[]
yerr=[]
for line in file:
    index,x_data,y_data,yerr_data=line.split('&')
    x.append(float(x_data))
    y.append(float(y_data))
    yerr.append(float(yerr_data))

x=np.array(x)
y=np.array(y)
yerr=np.array(yerr)

#Now we can sample our posterior PDF using MCMC.
#Let us use 50 Markov chains.
#Where do we initialise them? Anywhere we want but a common idea to start near the optimum of the likelihood.
guess=(1.0,1.0,1.0)
soln=minimize(log_likelihood,guess,args=(x,y,yerr))

#We now initialise each of our 50 Markov chains near the optimum reported by the minimize function
nwalkers,ndim=50,3
pos=soln.x+1e-4*np.random.randn(nwalkers,ndim)

#We now use the emcee library to do the MCMC so that each Markov chain takes 4,000 steps.
sampler=emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x,y,yerr))
sampler.run_mcmc(pos,4000)

#We can look at the chains by plotting them:
samples=sampler.get_chain()

#best-fit values of the parameters
a_true=np.median(samples[:,:,0])
b_true=np.median(samples[:,:,1])
c_true=np.median(samples[:,:,2])

print('best-fit values of the parameters a, b and c are respectively',a_true,',',b_true,'and',c_true)

#one-sigma uncertainty is given by standard deviation
print('one-sigma uncertainties are respectively',np.std(samples[:,:,0]),',',np.std(samples[:,:,1]),'and',np.std(samples[:,:,2]))

plt.plot(samples[:,:,0],'k') # a values
plt.xlabel(r'step',fontsize=20)
plt.ylabel(r'a',fontsize=20)
plt.title('Markov Chains for the parameter a',fontsize=20)
plt.show()

plt.plot(samples[:,:,1],'k') # b values
plt.xlabel(r'step',fontsize=20)
plt.ylabel(r'b',fontsize=20)
plt.title('Markov Chains for the parameter b',fontsize=20)
plt.show()

plt.plot(samples[:,:,2],'k') # c values
plt.xlabel(r'step',fontsize=20)
plt.ylabel(r'c',fontsize=20)
plt.title('Markov Chains for the parameter c',fontsize=20)
plt.show()

#We can plot the posterior PDF using the corner library.
params=np.vstack([samples[i] for i in range(len(samples))])
fig=corner.corner(params,labels=['a','b','c'],truths=[a_true,b_true,c_true],show_titles=True)
plt.show()

#plotting the data with error bars
plt.errorbar(x,y,yerr=yerr,fmt='ok',capsize=5)

z=np.linspace(0,300,1000)

sample_model=np.random.randint(0,nwalkers*4000,200)

#plotting 200 randomly chosen models
for j in range(200):
    plt.plot(z,params[sample_model[j]][0]*z*z+params[sample_model[j]][1]*z+params[sample_model[j]][2],'silver')

#plotting best fit model
plt.plot(z,a_true*z*z+b_true*z+c_true,'r',label=r'best-fit')

plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.title(r'data with the best-fit model and 200 randomly chosen models',fontsize=20)
plt.legend()

plt.show()
