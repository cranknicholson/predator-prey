# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:50:14 2019

@author: Henrik
"""

def calc(x,y,dt,evaluateModel,euler):
    if euler==True:
        
        x2=x+dt*evaluateModel(x+(dt/2)*evaluateModel(x,y,)[0],y)[0]
        y2=y+dt*evaluateModel(x,y+(dt/2)*evaluateModel(x,y)[1])[1]
        return x2,y2
    else:
        return x+dt*evaluateModel(x,y)[0],y+dt*evaluateModel(x,y)[1]
    