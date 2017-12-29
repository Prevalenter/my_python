#这个循环方式
def Fibona(m):
    '循环方式'
    lst=[1,1]
    for i in range(2,m):lst.append(lst[i-1]+lst[i-2])
    return lst

#这个递归方式
def Fibona_02(level,lst=[1,1]):
    if level<=2:return 1
    else:
        temp=Fibona_02(level-1,lst)+Fibona_02(level-2,lst)
        #防止多次重复添加
        if not temp in lst:lst.append(temp)
        return temp

#这个循环方式
print(Fibona(10))
lst=[1,1]
Fibona_02(10,lst)
print(lst)
