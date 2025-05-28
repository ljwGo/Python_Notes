# ### 1 滑动序列:可滑动的序列 自定义一个函数 根据参数n的值 变成对应个元素的容器(zip)
listvar = [1,2,3,4,5,6,7,8,9]
# map filter enumerate zip


lst1 = listvar[0::2]
lst2 = listvar[1::2]
zip(listvar[0::2],listvar[1::2])

'''
lst = [[1,2],[3,4],[5,6]]
def func(a,b,c):
	print(a)
	print(b)
	print(c)
func(*lst)
'''

listvar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def func(lstvar,n):
	return list(zip(*[listvar[i::n] for i in range(n)]))
res = func(listvar,3)
it = list(map(list,res))
print(it)

# 简化
func = lambda listvar,n : list(zip(*[listvar[i::n] for i in range(n)]))

# ### 2 res多少?
def func():
	return [lambda x : i*x for i in range(4)]
res = [m(2) for m in func()]
print(res)

'''
循环四次,往列表里插入了4个函数变量
此刻i 等于 3
再循环的时候,一次循环获取这个列表中的一个元素,是一个个的函数
m(2) => return i*x => 3 * 2 => 6
因为循环的是4次,所以在列表里是4个6
'''
def func():
	lst = []
	for i in range(4):
		# 函数的定义处
		def newfunc(x):
			return i*x
		lst.append(newfunc)
	return lst
res =[m(2) for m in func()]

print(func())
'''
[<function func.<locals>.newfunc at 0x003F77C0>, <function func.<locals>.newfunc at 0x0067E340>, <function func.<locals>.newfunc at 0x0067E2F8>, <function func.<locals>.newfunc at 0x0067E3D0>]
'''

# ### 3 结果是多少
'''
定义时,不回去调用生成器里面的代码
只有在调用时,才会执行生成器函数或者表达式里面的内容
(next for list 是在调用生成器,这时才会触发里面的代码)
for n in [2,10] 循环两次之后,最后得到的是数据是n = 10
'''
def add(a,b):
	return a + b
def test():
	for r in range(4):
		yield r
# 初始化生成器函数 -> 生成器对象 -> 简称生成器
g = test() # (0,1,2,3)

for n in [2,10]:
	g = (add(n,i) for i in g)
print(list(g))

g = (add(n,i) for i in g) # add(10,1) => 11 add(10,2) => 12 add(10,3) => 13
g = (add(n,i) for i in g) # add(10,11) => 21 add(10,12) => 22 add(10,13) => 23

# 调用生成器
print(list(g))
# n => 10
