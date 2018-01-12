# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:35:42 2018

@author: liu
"""
import numpy as np
def line_distance(l1=np.array([[4,0,0],[0,3,0]]),l2=np.array([[4,3,1],[4,3,-4]])):
    #求出线段的向量
    arr1,arr2=l1[1]-l1[0],l2[1]-l2[0]
    #求两个向量的叉乘
    temp=np.cross(arr1,arr2)
    #取l1、l2上两点，得到第三个向量
    arr3=l2[0]-l1[0]
    cos_angle=np.abs(sum(arr3*temp))/(np.sqrt(sum(temp**2))*np.sqrt(sum(arr3**2)))
    #np.linalg.norm()为向量两点的距离，
    return (np.linalg.norm(l2[0]-l1[0])*cos_angle)

print(line_distance(np.array([[4,0,0],[0,3,0]]),np.array([[4,3,1],[4,3,-4]])))
