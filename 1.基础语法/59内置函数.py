# ### 内置函数
# abs 绝度值函数
res = abs(-10)
print(res)

# round 四舍五入(n.5 n为偶数则舍去 n.5 n为奇数,则进一!) 奇进偶不进
res = round(13.56)
res = round(4.5)
res = round(5.5)
res = round(4.53)
res = round(4.9)
print(res)

# sum 计算一个序列的和
tuplevar = (1,2,3,4,5,6)
res = sum(tuplevar)
print(res)

# max 获取一个序列里边的最大值
# max 高阶函数的使用
def func(n):
	# print(n) # 参数是一个个的元组
	return n[1]
lst = [('长远',33),('李明辉',58),('李德亮',99),('历史源',-6)]
res = max(lst,key=func)

# min 获取一个序列里边的最小值
dic = {'任廷伟':60,'钟永玲':59,'黄乐喜':90,'李诗韵':-6}
def func(n):
	# print(n) 参数是字典的键
	return dic[n] # 通过键返回值,通过值排序,找出最小值对应的键
res = min(dic,key=func)
print(res)
# 排序和比较的是键对应的值(函数返回值),返回的是传送给对应函数的键(函数形参)

# pow 计算某个值的x次方
res = pow(2,3)
'''前两个数运算的值,在和第三个数取余'''
res = pow(2,3,3)
print(res)

# range 产生指定范围内数据的可迭代对象
for i in range(1,6,3):
	print(i)

# bin 将10进制数据转化为二进制
res = bin(255)
print(res)

# oct 将10进制数据转化为八进制
res = oct(255)
print(res)

# hex 将10进制数据转化为16进制
res = hex(255)
print(res)

# chr 将ASCII编码转换为字符
res = chr(97)
print(res) # 打印 a

# ord 将字符串转换为ASCII编码
res = ord('a')
print(res)

# eval 将字符串当做python代码执行(有局限性,不能创建变量)
strvar = 'print("我是大帅哥")'
print(strvar)
eval(strvar)

# exec 将字符串当做python代码执行(功能更强大)谨慎使用,存在安全隐患
strvar = 'a="文哥真帅"'
exec(strvar)
print(a)

dic = globals()
print(dic)
dic['wangwen'] = '宇宙第一男人'
print(wangwen)

# repr 不转义字符输出字符串
strvar = 'D:\nabc'
res = repr(strvar)
print(res)

# input 接受输入字符串
name = input('你好,你叫什么?')
print(name)

# hash 生成哈希值

