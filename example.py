#!/usr/bin/env python
# coding: utf-8

#Author: Sanger Steel

from functions import *
from main import *
import numpy as np
from segmented_functions import *



x = np.linspace(1,10,300)
y=[20*np.cos(vals) + np.random.randint(-25,25) for vals in x]
#weights = np.random.normal(size=(300,))
y=np.array(y)
y=y.reshape((300,1))




sol=main(x,y)
params_best=sol[0]
params_poly = sol[3][0]
params_segmentedOne = sol[3][1]
params_segmentedTwo = sol[3][2]
params_segmentedThree = sol[3][3]




xold  = np.linspace(1,10,300)
x = np.linspace(1,10,1000)




func = seg_One(x,*params_segmentedOne)
func2 = poly.polyval(x,params_poly)
func3 = seg_Two(x,*params_segmentedTwo)
func4 = seg_Three(x,*params_segmentedThree)



plt.figure(figsize=(12,10))
plt.scatter(xold,y)
#plt.scatter(x,func,color='r',label='Piecewise fit (1 break)')
plt.plot(x,func,color='r',label='Piecewise fit (1 break)')
#plt.scatter(x,func3,color='b',label='Piecewise fit (2 breaks)')
#plt.plot(x,func3,color='b')
#plt.scatter(x,func4,color='g',label='Piecewise fit (3 break)')
#plt.plot(x,func4,color='g')
plt.plot(x,func2, color='black',label = 'Polynomial best fit')
#plt.scatter(x,func2, color='black',label = 'Polynomial best fit')
plt.legend()






