# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:02:39 2018

@author: liu
"""
from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import uniform_filter, gaussian_filter, sobel
from scipy.ndimage import convolve1d
import numpy.ma as npm
def bench_deal(img1,lst=np.array([[50,100,200,255],[25,75,175,225]])):
    '''
    对图像进行划分区域灰度值归一化
    lst1为分割的分界点
    lst2为每个区域对应的灰度值
 '''
    lst_index=np.array([lst[1,0]]*(lst[0,0]))
    for i in range(1,len(lst[1])):
        lst_index=np.append(lst_index,np.array([lst[1,i]]*(lst[0,i]-lst[0,i-1])))
    img1=lst_index[img1.astype(np.int32)]
    
    return img1


img_gray1 = imread('01.png',True)
img_gray2 = imread('02.png',True)
#显示灰度图
img_gauss1 = gaussian_filter(img_gray1,3)
img_gauss2 = gaussian_filter(img_gray2,3)
#img_gauss = gaussian_filter(img_gray,1)
#img_gauss=(img_gauss//12)*12
fig1=plt.figure('处理对比')
plt.subplot(121)
plt.imshow(img_gray1,cmap='gray')
plt.subplot(122)
plt.imshow(img_gray2,cmap='gray')
fig2=plt.figure('高斯差分')
img_dog=(img_gray1-img_gray2).astype(np.int8)
img_dog=abs(img_dog)
plt.imshow(img_dog)
fig3=plt.figure('直方图')
hist=np.histogram(img_dog,bins=256,range=(0,256))
hist1=np.linspace(0,255,256)
plt.plot(hist1,hist[0],'r')
plt.show()
lst=list(hist[0])
index=lst.index(max(lst))
i=0
while(1):
    index+=1
    if(lst[index]-lst[index+1]<0):
        break
print(index)
fig4=plt.figure('end')    
plt.subplot(121)
img_mask=bench_deal(img_dog,lst=np.array([[int(index),256],[0,256]]))
plt.imshow(img_mask)
imgh = np.abs(sobel(img_mask, axis=1)).astype(np.float)
imgv = np.abs(sobel(img_mask, axis=0)).astype(np.float)
imghv = np.sqrt(imgh**2+imgv**2)
plt.subplot(222)
img_end1= npm.array(img_gray2, mask=imghv)
plt.imshow(img_end1)
img_end2= npm.array(img_gray1, mask=imghv)
plt.subplot(224)
plt.imshow(img_end2)





