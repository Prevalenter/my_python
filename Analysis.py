import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np
from scipy.ndimage import binary_fill_holes,label,generate_binary_structure,distance_transform_edt
from skimage.morphology import watershed
from skimage.measure import regionprops
from skimage.filters import  sobel

def show_analysis(img1):
    #阈值操作
    print(1)

    '''
    for i in ls_1:
        if i.area<1200:
            lst_1[i.label]=0
        else:
            lst_1[i.label]=i.label
    img1=lst_1[img2.astype(np.int32)]
    return img1

    plt.subplot(122)
    plt.imshow(img1)
    plt.show() 

    #距离变换并分水岭
    img2=distance_transform_edt(img1)
    lst=np.array(range(255))
    lst=lst[::-1]
    img1=lst[img2.astype(np.int32)]
    
    markers =np.zeros_like(img1).astype(np.int16)
    markers[img1 < 1] = 0
    markers[img1 <235] = 1
    markers=markers.astype(np.int)
    label(markers,generate_binary_structure(2, 1),output=img2)
   
    #调用sicpy的分水岭
    img2=watershed(edge.astype(np.uint8),img2,watershed_line=True)
    #创建索引
    lst=np.array([255]+[0]*255) 
    img2=lst[img2]
 #   img2=sobel(img2.astype(np.int))
    img2=img_temp+img2
    plt.subplot(122)
    plt.imshow(img2)
    plt.show()
'''
 
if __name__ == "__main__":
    fig1=plt.figure('show')
    img1=imread('1.png',True)
    img2 =np.zeros_like(img1).astype(np.int16)
    img2=show_analysis(img1)
    plt.subplot(121)
    plt.imshow(img1,cmap='gray')
    plt.subplot(122)
    plt.imshow(img2)
    plt.show()
