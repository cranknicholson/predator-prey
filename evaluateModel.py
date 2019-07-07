# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:49:09 2019

@author: Henrik
"""

def calc(x,y):
        beta=3
        gamma=1
        delta=3
        alpha=0.3
        a=[]
        a.append(alpha*x-beta*x*y)
        a.append(-gamma*y+delta*x*y)
        return(a);
        