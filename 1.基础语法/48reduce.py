# ### reduce
'''
reduce(func,Iterable)
功能:
	从iterable中一次性拿出两个数据,扔到func函数进行运算,
	然后将运算的结果和Iterable中的第三个数据放到func中进行运算
	以此类推...
	最后返回运算的结果
参数:
	func : 自定义函数 或者 内置函数
	iterable : 可迭代对(容器类型数据,range对象,迭代器)
返回值:
	最后计算的结果
'''
# (1) [5,4,8,8] => 5488
# 方法一 字符串的拼接
lst = [5,4,8,8]
strvar = ''
for i in lst:
	strvar += str(i)
print(strvar)

# 方法二 用算数来做
'''
5 4 8 8
5*10 + 4 = 54
54 * 10 + 8 = 548
548 * 10 + 8 =5488
'''
lst = [5,4,8,8]
total = 0
# 1 变成迭代器
it = iter(lst)
# 2 获取前两个元素
num1 = next(it)
num2 = next(it)
total = num1 * 10 + num2
print(total)
# 3 计算剩余的数据
for i in it:
	total = total * 10 + i
print(total)

print('<======>')
total = 0
it = iter(lst)
for i in it:
	total = total * 10 + i
print(total)

# reduce
from functools import reduce
print(reduce)

# reduce 改写
def func(x,y):
	return x*10+y
print(func(5,4))

res = reduce(func,lst)
print(res)
'''
拿出 5 和 4 两个元素 扔到自定义的func函数中
x 接受 5 y 接受 4
return 5*10 + 4 => return 54

然后拿出54 和 8 两个元素 扔到自定义的func函数中
x 接受 54 y 接受 8
return 54 * 10 + 8 => return 548
'''

# '678' => 整形 678 (不让使用int)
def func2(n):
	dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return dic[n]
strvar = '678'
it = map(func2,strvar)
res = reduce(func,it)
print(res)

#res = reduce(func,strvar)
#print(res)


