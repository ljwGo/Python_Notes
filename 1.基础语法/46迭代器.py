# ### 迭代器
'''
迭代器: 能被next方法调用,并且不断返回下一个值的对象,是迭代器(对象)

特征:迭代器会生成惰性序列,他通过计算把值依次的返回,一边循环一边计算而不是一次性得到所有数据
优点:需要数据的时候,一次取一个,可以大大节省内存空间,而不是一棍脑的把所有数据放进内存
总结:
	1 惰性序列,节省空间内存
	2 遍历获取值的时候使用next,方向不可逆
	3 迭代器可以遍历无限大的数据
'''

# 可迭代对象
'''
如果数据成员中含有__iter__方法,就是可迭代对象
dir 查看该数据的内部成员
'''
setvar = {'a','b','c','d'}
lst = dir(setvar)
print(lst)

res = '__iter__' in lst
print(res)

for i in setvar:
	print(i)

# 迭代器
'''
# 1 如何定义一个迭代器
	1.iter(可迭代对象)
	2.可迭代对象.__iter__()
# 2 如何判断一个迭代器
	1.内部成员中,含有__iter__和__next__两个方法的是迭代器
	2,fron collections import Iterator,Iterable
# 3 如何调用一个迭代器
	使用next方法可以调用迭代器,返回里面的内容

可迭代对象 -> 迭代器
不可直接调用 -> 可直接调用
'''

# 定义一个迭代器
setvar = {'a','b','c','d'}
it = iter(setvar)
# 判断一个迭代器
lst = dir(it)
print(lst)

#方法一
res = '__iter__' in lst and '__next__' in lst
print(res)

#方法二
from collections.abc import Iterator,Iterable
res = isinstance(it,Iterator)
print(res)

# 3 调用迭代器
res = next(it)
res = next(it)
res = next(it)
res = next(it)
#res = next(it) 在调用就报错了
print(res)

# 4 重置迭代器
it = iter(setvar)
print(next(it))

# 把range对象变成迭代器
it = range(10).__iter__()
res1 = isinstance(it,Iterator)
res2 = isinstance(it,Iterable)
print(res1,res2)

res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)

# 方法二 for
print('<======>')
for i in it:
	print(i)

# 方法三 for + next
it = range(10).__iter__()
for i in range(5):
	res = next(it)
	print(res)




