# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:05:56 2020

@author: nabendu
"""

import numpy as np
import scipy.stats

p_s=np.array([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36])     #expected probabilities of possible scores

k=11-1     #dof = no of distinct values that our rn can have - 1 

#1st run
Y1=np.array([4,10,10,13,20,18,18,11,13,14,13])                          #observed counts 1
n1=np.sum(Y1)                                                           #total no of throw

V1=np.sum((Y1-n1*p_s)**2/(n1*p_s))                                      #calculating chi-squared statistic V

P1=1.0-scipy.stats.chi2.cdf(V1,k)                                       #calculating P(V>v) using chi-squared distribution
print('P(V>v) for run 1 =',P1)

#2nd run
Y2=np.array([3,7,11,15,19,24,21,17,13,9,5])                            #observed counts 2
n2=np.sum(Y2)                                                          #total no of throw

V2=np.sum((Y2-n2*p_s)**2/(n2*p_s))                                     #calculating V

P2=1.0-scipy.stats.chi2.cdf(V2,k)                                      #calculating P(V>v) using chi-squared distribution
print('P(V>v) for run 2 =',P2)    

#prescription of chi-squared test
if((P1<=0.01 or P1>0.99) and (P2<=0.01 or P2>0.99)):
    print('random numbers are not sufficiently random')
elif((0.01<P1<=0.05 or 0.95<P1<=0.99) and (0.01<P2<=0.05 or 0.95<P2<=0.99)):
    print('random numbers are suspect')
elif((0.05<P1<=0.1 or 0.9<P1<=0.95) and (0.05<P2<=0.1 or 0.9<P2<=0.95)):
    print('random numbers are almost suspect')   
elif((0.1<P1<=0.9) and (0.1<P2<=0.9)):
    print('numbers are sufficiently random')
else:
    print('nothing can be said from these 2 runs')
