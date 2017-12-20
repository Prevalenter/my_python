#find out the prime number(0-100)
print('the prime number is (0-100):')
#isp 为是否为质数的标志位
isp=1
#i = int(input())

#判断i是不是质数
for i in range(2,101):
    for j in range(2,i):
        #如果取余等于0，则跳出,并把标志位置0
        if i %j==0 :
            isp=0
            break
    if isp==1:
        print(i)
    isp=1
    
        
