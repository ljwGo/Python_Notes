# ### 生成器
'''
# 生成器本质是迭代器,允许自定义逻辑的迭代器

# 迭代器和生成器区别
	迭代器本身是系统内置的,重写不了,而生成器使用户自定义的,可以重写迭代逻辑

# 生成器可以用两种方式创建:
	1生成器表达式 (里面是推导式,外面用圆括号)
	2生成器函数(用def定义,里面含有yield)
'''
from collections.abc import Iterable,Iterator
# 1 生成器表达式
gen = (i for i in range(5))
print(gen)

# 2 next
# res = next(gen)

# for
#for i in gen:
#	print(i)

# 3 list
lst = list(gen)
print(lst)

# 4 for + next
gen = (i for i in range(5))
for i in range(2):
	res = next(gen)
	print(res)


# ### 生成器函数
'''
# yield 类似于return
共同点在于:执行道这句话都会把值返回出来
不同点在于:yield每次返回值时,会记住上次离开时执行的位置,下次在调用生成器,会从上次执行的位置往下走
		 而return直接终止函数,每次从头调用
yield 6 和 yield(6) 2种写法都可以 yield 6 更像return 6 的写法推荐使用
'''
# 1 基本语法
# 生成器函数
def mygen():
	print('one')
	yield 1

	print('two')
	yield 2

	print('three')
	yield 3

# 初始化生成器函数 -> 生成器对象 -> 简称生成器
gen = mygen()
print(gen)

# 调用生成器
res = next(gen)
print(res)

res = next(gen)
print(res)

res = next(gen)
print(res)

'''
初始化生成器函数

第一次调用生成器
res = next(gen) print(one) yield 1 记录当前代码执行的状态,将1返回,返回到调用处,阻塞等待下一次调用

第二次调用生成器 从47行,上一次记录的位置,往下执行,print('two') yield 2 记录当前代码执行的状态,将2返回,返回到调用处,阻塞等待下一次调用
'''

# 2 改造生成器
def func():
	for i in range(1,101):
		yield '球衣号码{}'.format(i)
# 初始化生成器函数 -> 生成器对象 -> 简称生成器
gen = func()
for i in range(50):
	res = next(gen)
	print(res)

# 3 send send是把数据发送上一个yield
'''
# ### send
# next和send区别:
	next 只能取值
	send 不但能取值,还能发送值
# send注意点
	第一个send 不能给yield 传值 默认只能写None
	最后一个yield 接受不到send的发送值
'''

def mygen():
	print('start')
	res1 = yield 1
	print(res1)

	res2 = yield 2
	print(res2)

	res3 = yield 3
	print(res3)

	print('end')

# 初始化生成器函数 -> 生成器对象 -> 生成器
# 第一次向上一个yield发送,只能填None
gen = mygen()
val1 = gen.send(None)
print(val1)

print('<======>')
val2 = gen.send('one')
print(val2)

val3 = gen.send('two')
print(val3)

#val4 = gen.send('three')
#print(val4)
'''
val1 = gen.send(None)
第一次发送 因为要发送给上一个yield ,所以只能是None
print('start')
走到第一个yield,记录当期代码执行的状态,将1返回,val1接受数据,添加阻塞,等待下一次调用

第二次发送
val2 = gen.send('one') 从上一个yield记录开始往下执行,将2返回,而yield 1 接收到send发送的one数据,1更改为one
val2接受数据,添加阻塞,等待下一次调用
'''
# 4 yield from: 将一个可迭代对象变成一个迭代器返回
def mygen():
	yield [1,2,3,4]
	yield [2,2,2,2]
gen = mygen()
res = next(gen)
print(res)
res = next(gen)
print(res)

def mygen():
	yield from [1,2,3,4]
gen = mygen()
res = next(gen)
print(res)

# 5 斐波那契数列
# 1 1 2 3 5 8 13 21 34 55...
def myfib(maxlength):
	a,b=0,1
	i = 0
	while i < maxlength:
		#print(b)
		yield b
		a,b = b,a+b
		i += 1
gen = myfib(10)
#for i in gen:
#	print(i)




