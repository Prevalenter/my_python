'''
实现对复制下的文本进行统计
'''
import urllib.request
#引入正则模块，实现以多个字符分割
import re
def statistic(txt,n):
    dic = {}
    #拆分并统计字符文本，以非文本字符拆分
    for i in re.split('\W+',txt):
        if not i in dic:dic[i] = 1
        else: dic[i] += 1
    item= dic.items()
    n_item = [(i[1], i) for i in item]
    #对其进行排序，true为正序
    n_item.sort(reverse=True)
    item = [i[1] for i in n_item]
    #打印的前n个单词以及出现的频率
    for i in range(n):print(item[i])   
f=open('txt123.txt',encoding= 'utf-8')
#read()对整个文本进行读取
lines=f.read()
f.close()
#temp=re.split('\W+',lines)
#print(temp)
statistic(lines,10)
