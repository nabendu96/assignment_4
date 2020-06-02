# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:34:25 2020

@author: nabendu
"""

#Monte Carlo integration

import numpy as np

N=1000000

#area of unit circle

#function to caluculate the square of radius vector of a given point
def f1(x,y):
    return(x*x+y*y)

count1=0

for i in range(N):
    #creating uniform random point in 2D box of length 2 unit
    x=np.random.uniform(-1,1)
    y=np.random.uniform(-1,1)
    #we count those points which are inside the unit circle
    if(f1(x,y)<=1):
        count1=count1+1    
    
V2=4*count1/N                      #area of the circle is given by the area of the box multiplied by the probalility that a chosen point in the box will be inside the circle  
print('area of unit circle =',V2)


#10d unit hypersphere

#function to caluculate the square of radius vector of a given point
def f2(r):
    return(np.sum(r*r))

dim=10
    
count2=0

for j in range(N):
    #creating uniform random point in 10D box of length 2 unit
    r=np.random.uniform(-1,1,dim)
    #we count those points which are inside the 10d unit hypersphere
    if(f2(r)<=1.0):
        count2=count2+1
                        
V10=2**dim*count2/N                #volume of the sphere is given by the volume of the box multiplied by the probalility that a chosen point in the box will be inside the sphere
print('volume of 10d unit hypersphere =',V10)
