# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:42:53 2018

@author: liu
"""
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import  sobel
from scipy.ndimage import binary_fill_holes,label,generate_binary_structure,watershed_ift
from skimage.measure import regionprops
from skimage.data import coins

def area_filter(img,area_max):
    hist=list(np.histogram(img,bins=256,range=(0,256)))
    ls = regionprops(img)
    for i in range(0,len(ls)):
        if hist[0][i]<area_max:      img[img==hist[1][i]]=0
    return img

def couter_area(img):
    area=[]
    ls = regionprops(img)
    for i in ls:
        area.append(round(i.area,2))
    return area    
def couter_center(img):
    center=[]
    center.append([])
    center.append([])
    ls = regionprops(img)
    for i in ls:
        center[0].append(round(i.centroid[0],2))
        center[1].append(round(i.centroid[1],2))
    return center
#        lst.append()

img_gray = coins()
#分水岭不可以用高斯滤波，只能用锐化
#img_gray=gaussian_filter(img_gray,2)
fig1=plt.figure('原图')
edge = sobel(img_gray).astype(np.uint8)
# 制作掩膜
markers =np.zeros_like(img_gray).astype(np.int16)
markers[img_gray < 30] = 1
markers[img_gray > 150] = 2
img= np.zeros_like(img_gray, dtype=np.int16)
markers.astype(np.uint8)
#调用sicpy的分水岭
watershed_ift(input=img_gray.astype(np.uint8),markers= markers,output=img)
plt.subplot(121)
plt.imshow(img)


img=img//2
plt.subplot(121)
img_fill= np.zeros_like(img, dtype=np.uint8)
binary_fill_holes(img,output=img_fill)
img_fill*=255;
plt.imshow(img_fill)
img_lab= np.zeros_like(img_fill, dtype=np.uint8)
#创建标签
label(img_fill,generate_binary_structure(2, 1),output=img_lab)
plt.subplot(122)
#img_lab[img_lab==2]=0
#对像素点小于100的进行过滤
img_lab=area_filter(img_lab,100)
plt.imshow(img_lab)

couter_center(img_lab)

print('个数为:')
print(len(regionprops(img_lab)))
print('面积是:\n')
print(couter_area(img_lab))
print('-------------')
print('中心坐标是是:\n')
lst=couter_center(img_lab)
print('x:\n')
print(lst[1])
print('y:\n')
print(lst[0])
plt.show()
