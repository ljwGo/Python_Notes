# ### 高阶函数: 能够把函数当成参数传递的就是高阶函数
'''map reduce sorted filter'''

# map
'''
map(func,Iterable)
功能:
	把Iterable中的值,一个一个拿出来放到func函数中进行处理,把处理的结果扔到迭代器中,
参数:
	func : 自定义函数 或者 内置函数
	Iterable : 可迭代对象(容器类型数据 range对象 迭代器)
返回值:
	迭代器
'''
from collections.abc import Iterable,Iterator
#['1','2','3','4'] => [1,2,3,4]
lst = ['1','2','3','4']
lst_new = []
for i in lst:
	print(i,type(i))
	lst_new.append(int(i))
print(lst_new)

# map 改写
it = map(int,lst)
res = isinstance(it,Iterator)
print(res)

'''
代码解析:
首先从列表里拿出第一个数据'1'扔到int方法中进行强转,把强转的结果扔到迭代器里
然后从列表里拿出第一个数据'2'扔到int方法中进行强转,把强转的结果扔到迭代器里
然后从列表里拿出第一个数据'3'扔到int方法中进行强转,把强转的结果扔到迭代器里
然后从列表里拿出第一个数据'4'扔到int方法中进行强转,把强转的结果扔到迭代器里

最后返回迭代器
'''

# 1 next 获取迭代器中的数据
res = next(it)
print(res)

# 2 for 循环遍历
it = map(int,lst)
for i in it:
	print(i)

# 3 list 强制转换
it = map(int,lst)
lst = list(it)
print(lst)

# ### 2 [1,2,3,4] => [1,4,9,16]
lst = [1,2,3,4]
def mi(i):
	return i**2
# lambda 改写
# mi = lambda i : i**2
# 方法一
it = map(mi,lst)
# list强转迭代器为列表
lst_new = list(it)
print(lst_new)

# 方法二
lst_new = list(map(lambda i : i**2,lst))
print(lst_new)

# ### {97:'a',98:'b',99:'c'} => 给你['a','b','c'] 得到 [97,98,99]
# 反转字典
dic = {97:'a',98:'b',99:'c'}
dic_new = {}
for k,v in dic.items():
	dic_new[v] = k

lst = ['a','b','c']
lst_new = []
for i in lst:
	lst_new.append(dic_new[i])
print(lst_new)

# 用map进行改写
lst = ['a','b','c']
def func(n):
	dic = {97:'a',98:'b',99:'c'}
	dic_new = {}
	for k,v in dic.items():
		dic_new[v] = k
	return dic_new[n]

it = map(func,lst)
lstvar = list(it)
print(listvar)






