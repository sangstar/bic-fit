#!/usr/bin/env python
# coding: utf-8

# Author: Sanger Steel

from functions import *




def main(x,y,**kwargs):
    """ 
    Fits polynomial and piecewise fits to data given,
    and determines the best fits using BIC. Note that
    for the return arrays, the ordering is as follows:
    polynomial best fit, segmented regression best fit
    with 1, 2 and 3 model breaks garnering indices 0 
    to 3 respectively. 
    
    Args:
        x (array-like) : x data
        y (array-like) : y data. Must have dimension (N,1).
        weights (array-like): weights to data. Default None.
        
    Returns:
        params[n] : the parameters for the best fit. n is 
                    the index of the best fit, which ranges
                    from 0 to 3. 
        BICS[n]   : the BIC score of the best fit. n is
                    the index of the best fit, which ranges
                    from 0 to 3.
        BICS      : The BIC scores of all fits used.
        params    : The parameters for each fit used. 
    """    
    
    weights = kwargs.get('weights', None)
    BICS = []
    params=[]
    param,score = polynom_best_fit(x,y,weight=weights)
    BICS.append(score)
    params.append(param)
    param,score = segmentedRegression_one(x,y,sigma=weights)
    BICS.append(score)
    params.append(param)
    param,score = segmentedRegression_two(x,y,sigma=weights)
    BICS.append(score)
    params.append(param)
    param,score = segmentedRegression_three(x,y,sigma=weights)
    BICS.append(score)
    params.append(param)
    best = min(BICS)
    best_index = np.where(BICS == best)
    if best_index[0][0] == 0:
        print(str(len(params[0])-1)+'- degree polynomial optimal')
        return params[0],BICS[0],BICS,params
    if best_index[0][0] == 1:
        print('Piecewise fit optimal (1 breakpoint)')
        return params[1],BICS[1],BICS,params
    if best_index[0][0] == 2:
        print('Piecewise fit optimal (2 breakpoints)')
        return params[2],BICS[2],BICS,params
    if best_index[0][0] == 3:
        print('Piecewise fit optimal (3 breakpoints)')
        return params[3],BICS[3],BICS,params
        



    
    

