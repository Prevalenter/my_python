def Fibona(m):
    '循环方式'
    now,before=1,1
#    print(now)
    lst=[]
    lst.append(now)
    for i in range(1,m):
        lst.append(now)
        before,now=now,now+before
    return lst

#递归方式
def Fibona1(m):
    '递归方式,m为第M个'
    if m<=2:return 1
    else: return Fibona1(m-1)+Fibona1(m-2)
def get_n_Fibona1(n):
    lst=[]
    for i in range(1,n+1):
        lst.append(Fibona1(i))
    return lst

#这个循环方式
print(Fibona(10))
#这个递归方式
print(get_n_Fibona1(10))
