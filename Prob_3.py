# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:26:13 2020

@author: nabendu
"""

import numpy as np
from timeit import default_timer as timer

n=10000

start_time1=timer()                 #starting time for lcg algorithm

a=1103515245           
c=12345                
m=2**31                
x=1                    

lcg=np.zeros(n)

for i in range(n):
    x=(a*x+c)%m
    lcg[i]=x
    
lcg=lcg/m

end_time1=timer()                   #ending time for lcg

print('time taken to produce 10000 uniform deviates between 0 and 1 for lcg =',end_time1-start_time1)

start_time2=timer()                 #staring time for the case of numpy random function

numpy_random=np.random.rand(n)

end_time2=timer()                   #end time for the numpy

print('time taken to produce 10000 uniform deviates using numpy.random.rand() =',end_time2-start_time2)
