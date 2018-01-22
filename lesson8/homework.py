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
#    fig=plt.figure()
    hist=np.histogram(img1,bins=256,range=(0,256))
#    hist0,hist1=hist[0],hist[1]
    plt.subplot(122)
    hist1=np.linspace(0,255,256)
    plt.plot(hist1,hist[0])
    plt.show()
def on_press(event):
    x=int(event.xdata)
    y=int(event.ydata)
    table_val=img_gray[x-3:x+4,y-3:y+4]
    print(table_val)
    fig3=plt.figure('7*7灰度值显示')
    plt.subplot(211)
    col_labels = ['col1','col2','col3','col4','col5','col6','col7']
    row_labels = ['row1','row2','row3','row4','row5','row6','row7']
    my_table = plt.table(cellText=table_val, colWidths=[0.12]*7,
                     rowLabels=row_labels, colLabels=col_labels,
                     loc='best')
    plt.show()
    plt.subplot(212)
    plt.imshow(table_val,cmap='gray')
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
       
img_gray = imread('123.png',True)
#显示灰度图
fig1=plt.figure('灰度及其直方图')
plt.subplot(121)
plt.imshow(img_gray,cmap='gray')
fig1.canvas.mpl_connect('button_press_event', on_press)
plt.show()
show_hist(img_gray)
#阈值梯度处理并显示
img_bench=bench_deal(img_gray)
fig2=plt.figure('梯度化图像及其直方图')
plt.subplot(121)
plt.imshow(img_bench,cmap='gray')
#打印梯度图鼠标点击处附件七个点
plt.show()
#显示梯度图的直方统计图
show_hist(img_bench)
fig3=plt.figure('假彩色图')
#显示假彩色图
plt.imshow(img_gray)
plt.show()

