# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:39:01 2018

@author: liu
"""
from moudle import * 
from Analysis import show_analysis
from skimage.morphology import watershed,h_maxima
from scipy.ndimage import distance_transform_edt,binary_dilation
def show_Connected():
    img1=imread('1.png',True)
    img2 =np.zeros_like(img1).astype(np.int16)
    img2=show_analysis(img1)
    
    ls= regionprops(img2)
    #偏心率过滤
    lst=np.array([0]*(len(ls)+1))  
    #面积以及偏心率过滤                
    for i in ls:
        if i.eccentricity<0.7 : lst[i.label]=0
        else : lst[i.label]=i.label
    img1=lst[img2.astype(np.int32)]
    
    #这里要用copy，否则会跟着变化
    img_temp1=img1.copy()

    #去除了后label还是不变，重新label
    label(img1,generate_binary_structure(2, 2),output=img2)    
 
     #将距离变换图像反转
    lst=[i for i in range(256)]
    lst=np.array(lst[::-1])
    img2=distance_transform_edt(img2)

    markers=h_maxima(img2,2)
    markers=binary_dilation(markers, structure=generate_binary_structure(2, 2))
    label(markers,generate_binary_structure(2, 2),img1) 
    img2=lst[img2.astype(np.int32)]   

    #分水岭
    img2=watershed(img2,img1,watershed_line=True)
    lst=np.array([1]+[0]*254)
    #提取出边界
    edg=lst[img2]

    plt.subplot(121)
    lst=np.array([0]+[1]*254)
    img1=lst[img_temp1]
    plt.imshow(img1)

    plt.subplot(122)
    img2=edg*img1+img1
    plt.imshow(img2)
    
    plt.show()  

if __name__ == "__main__":
    show_Connected()



