# ### 集合推导式
# 与列表推导式相似

# ### 字典推导式
'''
enumerate(iterable,[start=0])
功能:枚举;将索引号和iterable中的值,一个一个拿出来配对组成元组放入迭代器中
参数:
	iterable:可迭代数据(容器类型数据,range对象,迭代器)
	start:可以选择开始的索引号(默认从0开始)
返回值:迭代器
'''
from collections.abc import Iterable,Iterator
# 基本语法
lstvar = ['李德亮','王文','莉莉丝']
it = enumerate(lstvar)
print(it)
res = isinstance(it,Iterator)
print(res)
res = dir(it)
print(res)
res = '__iter__' in dir(it)
print(res)

# 从 5 小标开始枚举
lst = list(enumerate(lstvar,start=5))
print(lst)

# 2 zip
'''
zip(iterable,... ...)
功能:将多个iterable中的值,一个一个拿出来配对组成元组放入迭代器中
参数:iterable
返回值:迭代器
多出来无人配对的元素,会自动的舍弃掉
'''

lst1 = [1,2,3,4,]
lst2 = ['a','b','c']
it = zip(lst1,lst2)
lst = list(it)
print(it,lst)

# 1转换成字典推导式
lstvar = ['李德亮','王文','莉莉丝']
dic = dict(enumerate(lstvar))
print(dic)

# 2
lstvar = ['李德亮','王文','莉莉丝']
dic = {a:b for a,b in enumerate(lstvar,start=5)}
print(dic)

# 使用zip形成字典

# 小案列 把dic1中的键和dic2中的值 组合在一起变成新字典
dic1 = {'cpx':'身材高大魁梧','zjc':'爱走神','zyl':'活泼好动'}
dic2 = {'a':'草配线','b':'主进程','c':'邹荣玲'}
lst1 = dic1.keys()
lst2 = dic2.values()
res = dict(zip(lst1,lst2))
print(res)
dic = {k:v for k,v in zip(lst1,lst2)}

#dic = {k:v for k in lst1 for v in lst2 if index(k) == index(v)}
print(dic)











