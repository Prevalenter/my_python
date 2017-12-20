#find out 100 Fibonacci sequence

#times是找出的个数
times=2
now =1
before=now
#打印第一个和第二个数
print('the 1 Fibonacci sequence is 1')
print('the 1 Fibonacci sequence is 1')

while(times<100):
    #将当前数值存贮再变量temp中
    temp=now
    #进行移动
    now=now+before
    #更新before,并增加times
    times+=1
    before=temp
    print('the ',times,' Fibonacci sequence is ',now)
    
    
    
