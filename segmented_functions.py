#!/usr/bin/env python
# coding: utf-8


import numpy as np

def seg_One(xVals,model_break,slopeA,slopeB,offsetA,offsetB):
    returnArray=[]
    for vals in xVals:
        if vals > model_break:
            returnArray.append(slopeA * vals + offsetA)
        else:
            returnArray.append(slopeB * vals + offsetB)


    return returnArray



def seg_Two(xVals,break1,break2,slope1,offset1,slope_mid,offset_mid,slope2,offset2):
        returnArray=[]
        for x in xVals:
            if x < break1:
                returnArray.append(slope1 * x + offset1)
            elif (np.logical_and(x >= break1,x<break2)):
                returnArray.append(slope_mid * x + offset_mid)
            else:
                returnArray.append(slope2 * x + offset2)

        return returnArray




def seg_Three(xVals,break1,break2,break3,slope1,offset1,slope2,offset2,slope3,offset3,slope4,offset4):
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






