def Fibona(m):
    '循环方式'
    lst=[1,1]
    for i in range(2,m):lst.append(lst[i-1]+lst[i-2])
    return lst

#递归方式
def Fibona1(m):
    '递归方式,m为第M个'
    if m<=2:return 1
    else: return Fibona1(m-1)+Fibona1(m-2)
def get_n_Fibona1(n):
    lst=[]
    for i in range(1,n+1):lst.append(Fibona1(i))
    return lst

#这个循环方式
print(Fibona(10))
#这个递归方式
print(get_n_Fibona1(10))
'''

#这个循环方式

print(Fibona(10))

#这个递归方式

print(get_n_Fibona1(10))
#递归方式
#max为最大循环次数,level为当前递归等级
lst=[1,1]
def Fibona_01(level):
    if level<=2:
        if(level==1):return lst
        return 1
    else:
        temp=Fibona_01(level-1)+Fibona_01(level-2)
        if not temp in lst:
            lst.append(temp)
        return temp
'''
