from moudle import *
def show_analysis(img1):
#    img1=imread('1.png',True)
#    edge=sobel(img1.astype(np.int))
    #阈值操作
    lst=np.array([1]*200+[0]*55)  
    img1=lst[img1.astype(np.int32)]
    #填充洞
    binary_fill_holes(img1,output=img1)
    
    #标记并面积过滤
    img2=img1
    label(img1,generate_binary_structure(2, 1),output=img2)
    ls= regionprops(img2)
    lst=np.array([0]*(len(ls)+1))  
    #面积以及偏心率过滤                
    for i in ls:
        if i.area<1200: lst[i.label]=0
        else: lst[i.label]=i.label
    img1=lst[img2.astype(np.int32)]
    #去除了后label还是不变，重新label
    label(img1,generate_binary_structure(2, 1),output=img2)
    return img2
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
