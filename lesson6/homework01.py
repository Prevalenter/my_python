# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:57:44 2018

@author: liu
"""
"""
第一种方法
import numpy as np
def f(x,y):
    return y+1
print(np.fromfunction(f,(9,9),dtype=int)*np.fromfunction(f,(9,9),dtype=int).T)
"""
#第二种方法
import numpy as np
print((np.ones((9,9)).cumsum(axis=1))*(np.ones((9,9)).cumsum(axis=1)).T)


