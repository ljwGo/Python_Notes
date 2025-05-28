# 1
def extendlist(val,list=[]):
	list.append(val)
	return list

list1 = extendlist(10)
print(list1) # [10] => 默认形参列表
list2 = extendlist(123,[])
print(list2) # [123] => 实参给与的列表,跟上面列表相比是两个不同的列表
list3 = extendlist('a')
print(list3) # [10,'a']

# 2
lst1 = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
lst2 = ['红心','黑桃','草花','方砖']
lst_new = [(j,i) for i in lst1 for j in lst2]
print(lst_new)

# 3
lst = ['abvarefwf','13441auihwaf','ad','v']
lst_new = []
for i in lst:
	if len(i) >= 3:
		lst_new.append(i.upper())

lst_new = [i.upper() for i in lst if len(i) >= 3]
print(lst_new)

# 4
M = [[1,2,3],[4,5,6],[7,8,9]]
lst = [i[2] for i in M]
print(lst)

# 5
lst = [i**2 for i in range(1,51) if i % 3 == 0]
print(lst)

# 6
lst = ['python%d期' % (i) for i in range(1,11)]
print(lst)

# 7
lst = [(i,i+1) for i in range(6)]
print(lst)

lst = [1,2,3,4,5,6]
lst = [i for i in enumerate(lst)]
print(lst)

# 8
lst = [i*2 for i in range(10)]
print(lst)
lst = [i for i in range(0,19,2)]
print(lst)

# 9
ll = ['alex','Wusir','老男孩','神秘男孩']
lst = []
for i in range(4):
	res = ll[i] + str(i)
	lst.append(res)
print(lst)

# lst = [[i['timestamp'],i['values']] for i in x['Values']]

# 10
'''
文件对象是迭代器
在遍历的时候,每遍历一次,获取一行数据
'''
from collections.abc import Iterable,Iterator
def mygen():
	with open('ceshi.txt',mode='r+',encoding='utf-8') as fp:
		for i in fp:
			yield i

# 11
def add(a,b):
	return a + b
def add(a,b):
	yield a + b

def func(n):
	if n == 1 or n == 2:
		return n
	return func(n-1) + func(n-2)

strvar = '14235'
lst = []
length = len(strvar)
i = length - 1
while i >= 0:
	lst.append(strvar[i])
	i -= 1
strvar_new = ''.join(lst)
print(strvar_new)

# 递归写法
strvar = '14235'
lth = len(strvar)
def func(lth,lst=[]):
	if lth == 0:
		return ''.join(lst)
	lst.append(strvar[lth-1])
	return func(lth-1)
res = func(5)
print(res)






