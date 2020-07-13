#!/usr/bin/env python
# coding: utf-8

# In[300]:


import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, differential_evolution
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import warnings

# In[301]:





# In[302]:


def compute_BIC(y,model,variables):
    residual=y-model
    SSE=np.sum(residual**2)
  
    return np.log(len(y))*variables+len(y)*np.log(SSE/len(y))


# In[303]:


def polynom_best_fit(x,y,**kwargs):
    weights = kwargs.get('weight', None)
    deg = kwargs.get('max_deg', 6)
    bic_scores = []
    polynom_params= []
    for i in np.arange(0,deg):
        params=poly.polyfit(x,y,i,w = weights)
        params=[params[x][0] for x in np.arange(len(params))]
        polynom_params.append(params)
        model = poly.polyval(x,params)
        bic_scores.append(compute_BIC(y,model,len(params)))
    print(bic_scores)
    best = np.where(bic_scores == min(bic_scores))
    best_index = best[0][0]
    best_params = polynom_params[best_index]
    return best_params, min(bic_scores) 


# In[305]:


def segmentedRegression_one(x,y,sigma):
    
        def func(xVals,model_break,slopeA,slopeB,offsetA,offsetB):
            returnArray=[]
            for vals in xVals:
                if vals > model_break:
                    returnArray.append(slopeA * vals + offsetA)
                else:
                    returnArray.append(slopeB * vals + offsetB)


            return returnArray

        def sumSquaredError(parametersTuple):
            modely=func(x,*parametersTuple)
            warnings.filterwarnings("ignore") # do not print warnings by genetic algorithm

            return np.sum((y-modely)**2.0)

        def generate_genetic_Parameters():
            initial_parameters=[]
            x_max=np.max(x)
            x_min=np.min(x)
            y_max=np.max(y)
            y_min=np.min(y)
            slope=10*(y_max-y_min)/(x_max-x_min)

            initial_parameters.append([x_max,x_min])
            initial_parameters.append([-slope,slope])
            initial_parameters.append([-slope,slope])
            initial_parameters.append([y_max,y_min])
            initial_parameters.append([y_max,y_min])

            result=differential_evolution(sumSquaredError,initial_parameters,seed=3)

            return result.x

        geneticParameters = generate_genetic_Parameters()
        y = y.T
        y= y.flatten()
        piece1_params, pcov= curve_fit(func, x, y, p0=geneticParameters,sigma=sigma)

        model=func(x,*piece1_params)
        BIC_segReg_one=compute_BIC(y,model,5)
        return piece1_params,BIC_segReg_one
                             


# In[307]:


def segmentedRegression_two(x,y,sigma):
    def func(xVals,break1,break2,slope1,offset1,slope_mid,offset_mid,slope2,offset2):
            returnArray=[]
            for x in xVals:
                if x < break1:
                    returnArray.append(slope1 * x + offset1)
                elif (np.logical_and(x >= break1,x<break2)):
                    returnArray.append(slope_mid * x + offset_mid)
                else:
                    returnArray.append(slope2 * x + offset2)

            return returnArray

    def sumSquaredError(parametersTuple): #Definition of an error function to minimize
        model_y=func(x,*parametersTuple)
        warnings.filterwarnings("ignore") # Ignore warnings by genetic algorithm

        return np.sum((y-model_y)**2.0)

    def generate_genetic_Parameters():
            initial_parameters=[]
            x_max=np.max(x)
            x_min=np.min(x)
            y_max=np.max(y)
            y_min=np.min(y)
            slope=10*(y_max-y_min)/(x_max-x_min)

            initial_parameters.append([x_max,x_min]) #Bounds for model break point
            initial_parameters.append([x_max,x_min])
            initial_parameters.append([-slope,slope]) 
            initial_parameters.append([-y_max,y_min]) 
            initial_parameters.append([-slope,slope]) 
            initial_parameters.append([-y_max,y_min]) 
            initial_parameters.append([-slope,slope])
            initial_parameters.append([y_max,y_min]) 



            result=differential_evolution(sumSquaredError,initial_parameters,seed=3)

            return result.x

    geneticParameters = generate_genetic_Parameters() #Generates genetic parameters

    y = y.T
    y= y.flatten()

    piece2_params, pcov= curve_fit(func, x, y, geneticParameters,sigma=sigma) #Fits the data 
    



    model=func(x,*piece2_params)


    BIC_segReg_two=compute_BIC(y,model,8)
    
    return piece2_params,BIC_segReg_two


# In[309]:


def segmentedRegression_three(x,y,sigma):
    def func(xVals,break1,break2,break3,slope1,offset1,slope2,offset2,slope3,offset3,slope4,offset4):
            returnArray=[]
            for x in xVals:
                if x < break1:
                    returnArray.append(slope1 * x + offset1)
                elif (np.logical_and(x >= break1,x<break2)):
                    returnArray.append(slope2 * x + offset2)
                elif (np.logical_and(x >= break2,x<break3)):
                    returnArray.append(slope3 * x + offset3)
                else:
                    returnArray.append(slope4 * x + offset4)

            return returnArray
   
    def sumSquaredError(parametersTuple): #Definition of an error function to minimize
        model_y=func(x,*parametersTuple)
        warnings.filterwarnings("ignore") # Ignore warnings by genetic algorithm

        return np.sum((y-model_y)**2.0)

    def generate_genetic_Parameters():
            initial_parameters=[]
            x_max=np.max(x)
            x_min=np.min(x)
            y_max=np.max(y)
            y_min=np.min(y)
            slope=10*(y_max-y_min)/(x_max-x_min)

            initial_parameters.append([x_max,x_min]) #Bounds for model break point
            initial_parameters.append([x_max,x_min])
            initial_parameters.append([x_max,x_min])
            initial_parameters.append([-slope,slope]) 
            initial_parameters.append([-y_max,y_min]) 
            initial_parameters.append([-slope,slope]) 
            initial_parameters.append([-y_max,y_min]) 
            initial_parameters.append([-slope,slope])
            initial_parameters.append([y_max,y_min]) 
            initial_parameters.append([-slope,slope])
            initial_parameters.append([y_max,y_min]) 



            result=differential_evolution(sumSquaredError,initial_parameters,seed=3)

            return result.x

    geneticParameters = generate_genetic_Parameters() #Generates genetic parameters

    y = y.T
    y= y.flatten()

    piece3_params, pcov= curve_fit(func, x, y, geneticParameters,sigma=sigma) #Fits the data 

    model=func(x,*piece3_params)

    BIC_segReg_three=compute_BIC(y,model,11)
    
    return piece3_params,BIC_segReg_three


# In[311]:


# NOTE: This is only compatible with a y array of dimension (N,1)


# In[ ]:




