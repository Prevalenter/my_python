#用户界面
print('欢迎使用wahser，请选择需要的清洗模式:')
print('1、普通衣物')
print('2、毛衣')
print('3、自定义设置')

#根据预设模式对level和mode进行初始化
mode=int(input())
if mode == 1:
    level='low'
    times=3
    print('您已经选择普通衣物模式')
elif mode == 2:
    level='hight'
    times=5
    print('您已经选择毛衣模式')
else:
    print('您已经选择自定义模式，请输入水位:')
    level=input()
    print('请输入甩干次数:')
    times=int(input())

print('现在开始洗衣。。。')
if level=='low':
    print('注水 20L')
    print('搅拌 30min')
else:
    print('注水 50L')
    print('搅拌 60min')
print('放水')

for i in range(times):
    print('现在进行第 %d 次甩干'%(i+1))
    print('注入清水 30L')
    print('搅拌 20m')
    print('放水')
    print('甩干')
print('洗衣完成，谢谢使用！')
