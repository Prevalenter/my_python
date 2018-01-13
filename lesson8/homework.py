# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:54:54 2018

@author: liu
"""

from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np
#显示直方图
def show_hist(img1):
    fig=plt.figure()
    hist=np.histogram(img1,bins=255)
    hist0,hist1=hist[0],hist[1]
    #很奇怪，这里的hist0与hist1的长度不同，所以进行切片处理
    plt.plot(hist1[0:255],hist0)
    plt.show()
def on_press(event):
    '''
    print("my position:" ,event.button,event.xdata, event.ydata)
    print(x,y)
    '''
    x=int(event.xdata)
    y=int(event.ydata)
    print(img_gray[x-4:x+4,y-5:y+5])
    
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
       
img_gray = imread('lena.png',True)
#显示灰度图
fig=plt.figure()
plt.imshow(img_gray,cmap='gray')
fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()
show_hist(img_gray)

#阈值梯度处理并显示
img_bench=bench_deal(img_gray)
fig=plt.figure()
plt.imshow(img_bench,cmap='gray')
#打印梯度图鼠标点击处附件七个点

plt.show()
#显示梯度图的直方统计图
show_hist(img_bench)
fig=plt.figure()
#显示假彩色图
plt.imshow(img_gray)
plt.show()


