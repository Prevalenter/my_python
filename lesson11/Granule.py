# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:59:37 2018

@author: liu
"""
from moudle import *
from Analysis import show_analysis
from scipy.ndimage import standard_deviation
def show_Granule():
    img1=imread('1.png',True)
    img_gray=img1
    img2 =np.zeros_like(img1).astype(np.int16)
    img2=show_analysis(img1)
    
    ls= regionprops(img2)
    #偏心率过滤
    lst=np.array([0]*(len(ls)+1))  
    #面积以及偏心率过滤                
    for i in ls:
#        print(i.eccentricity)
        if i.eccentricity>0.7:
            lst[i.label]=0
        else:
            lst[i.label]=i.label
    img1=lst[img2.astype(np.int32)]
    img_temp=img1
    
    #去除了后label变化，重新label
    label(img1,generate_binary_structure(2, 2),output=img2)
    ls= regionprops(img2)
    index = range(0,len(ls))
    std=list(standard_deviation(img_gray,img2,index))

#标准差区分是否带核
    lst=np.array([0]*255)
    for i in std:
        if i>30 : lst[std.index(i)]=255
    img1=lst[img2.astype(np.int32)]
    plt.subplot(121)
    plt.imshow(img2)    
    plt.subplot(122)
    plt.imshow(img1)
    plt.show()    
if __name__ == "__main__":
    show_Granule()
