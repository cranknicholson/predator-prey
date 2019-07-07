# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:47:06 2019

@author: Henrik
"""
def calc(y0,x0,T,N,evaluateModel,calculateTimeStep,euler):

    dt=T/N
    y=[]
    x=[]
    y.append(y0)
    x.append(x0)
    i=1
    a=[]
    while i<N:
        
        
        a=calculateTimeStep(x[i-1],y[i-1],dt,evaluateModel,euler)
        y.append(a[1])
        x.append(a[0])
        i+=1
        
    return (x,y)
        