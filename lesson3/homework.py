import os
def get_homework(path='namelist.txt'):
    """
    path为存放git clone的地址，默认为namelist.txt
    """
    f=open('namelist.txt')
    lines=f.readlines()
    f.close()
    for i in lines:
        block=i.split('/')
        print(block[-2])
        #判断是否存在文件，防止重复创建出错
        if os.path.exists(block[-2])==False:os .mkdir(block[-2])
        #第一次字符串为clone的地址，第二个是为了将clone保存在相应的文件夹
        os.system('git clone %s %s'%(i[:-1],block[-2]))
        f.close()
        deal_homework(block[-2])
    print('您已经完成所有的git clone...')
    print('如果您希望添加路径到namelist.txt中，可直接调用path_add(),然后再次调用get_homework()')
def deal_homework(dir,level=1):
    """
    处理clone到的文件夹数据，将遍历到的文件名字打印处
    其中屏蔽了'.git' 和'.gitignore'
    """
    #把目录和文件名合成一个路径
    files = os.listdir(dir)
    for i in files:
        #去除无关的文件
        if(i=='.git' or i=='.gitignore'):continue
        #将文件名连接
        #此处很奇葩，不能直接用字符串+'\'
        dir_temp=os.path.join(dir,i)
        if os.path.isdir(dir_temp):
            block_temp=dir_temp.split('\\')
            print('-'*(level)*3,block_temp[-1]) 
            deal_homework(dir_temp,level+1)
        else:
            block_temp=dir_temp.split('\\')
            print('-'*(level)*3,block_temp[-1])
def path_add(dir):
    f=open('namelist.txt','a')
    f.write(dir+'\n')
    f.close() 
get_homework()

