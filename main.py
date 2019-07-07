# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:36:21 2019
Predator Prey
@author: Henrik
"""
import matplotlib as mlp
import matplotlib.pyplot as plt
import evaluateTimeLoop
import evaluateModel
import calculateTimeStep
import numpy as np


    
y0 = 0.2
x0 = 0.9
T=100
n=300
k=0.001
N=4*n**2*k*T
euler=False

result=evaluateTimeLoop.calc(y0,x0,T,N,evaluateModel.calc,calculateTimeStep.calc,euler)
y=np.arange(len(result[0]))
plt.plot(y,result[0], 'g')
plt.plot(y,result[1],'red')

plt.grid(True)
plt.show


