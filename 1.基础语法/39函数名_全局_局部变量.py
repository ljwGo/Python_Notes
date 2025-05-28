# ### 函数名的使用
# python中的函数可以向变量一样,动态创建,销毁,当参数传递,作为值返回,叫做第一类对象,其它语言功能有限

# 1 函数名是个特殊的变量,可以当做变量赋值
def func():
	print('我是func')

func_new = 1
print(func_new,type(func_new))
func_new = func
print(func_new,type(func_new))
func_new()

# 销毁函数
#del func_new
#func_new()

# 2 函数名可以作为容器类型数据的元素
def func1():
	print('我是func1...')
def func2():
	print('我是func2...')
def func3():
	print('我是func3...')

lst = [func1,func2,func3]
for i in lst:
	i()

# 3 函数名可以作为函数的参数
# 函数的定义处
def func4(func):
	func()

def func5():
	print('我是func5 函数...')

# 函数的调用处
func4(func5)

# 4 函数名可以作为函数的返回值
def func6(func):
	return func

def func7():
	print('我是func7 函数')

res = func6(func7)
print(res)
res()

# __doc__或者help查看文档
def fire_egg(something):
	'''
	:功能:炒菜的过程
	:param something: something 炒菜的名称
	:return: 返回做完的状态
	'''
	print('我要做的是:{}'.format(something))
	print('第一步:洗锅开火倒油,')
	print('第二部:打鸡蛋,搅拌,扔锅里')
	print('第三部:放调料,放盐,放糖,放西红柿')
	return 'ok'
fire_egg('西红柿炒鸡蛋')
help(fire_egg)

'''
功能:炒鸡蛋的过程
参数:something 炒菜的名称
返回值:返回做完的状态
'''


# ### 全局变量 和 局部变量
'''
局部变量:在函数内部的变量就是局部变量
全局变量:在函数外部,或者在函数内部使用global关键字声明的变量就是全局变量

作用域:作用的范围

如果是局部变量,作用域只限定在函数的内部;
如果是全局变量,作用域横跨整个文件
'''

#局部变量
def func():
	a = 10
	# 获取局部变量
	print(a)
	#修改局部变量
	a = 8
	print(a)

func()

#全局变量
b = 90
# 获取全局变量
print(b)
# 修改全局变量
b = 91
print(b)

# 3 在函数内部可以直接获取全局变量
def func2():
	# 1 可以在函数内部利用global进行全局变量的修改
	global b
	b = 100
	print(b)
	b += 10
func2()
print(b)

# 4 可以利用global在函数内部定义一个全局变量
def func():
	global d
	d = 110
func()
print(d)

'''
global:
	1如果函数外存在当前这个变量,利用global可以在函数内部对全局变量进行修改;
	2如果函数外不存在当前这个变量,利用global可以在函数内部定义一个全局变量;

'''

# ### 函数的嵌套
'''
函数和函数之间可以互相嵌套
	嵌套在内层的叫做内函数
	嵌套在外层的叫做外函数

'''
def outer():
	def inner():
		print('我是inner函数')

# 1 内部函数可以直接在函数外部调用么 不行
# inner

# 2 调用外部函数后,内部函数可以在函数外不掉用吗 不行
# outer()
# inner()

# 3 内部函数可以在函数内部调用吗 可以
# outer()

# 4 内部函数在函数内部调用时,是否有先后顺序

# 定义三个函数 outer函数中有inner,inner函数中有smallmr,调用smaller
def outer():
	def inner():
		def smaller():
			print('我是smaller函数')
		smaller()
	inner()
outer()

# 寻找变量的调用顺序采用LEGB原则(即就近原则)
'''
B: python内置模块的命名空间
G: 函数外部所在的命名空间
E: 外部镶嵌函数的作用域
L: 当前函内的作用域
依据就近原则,从下往上,从里向外,一次寻找
'''

# ### nonlocal 用来修饰局部变量
'''
nonlocal 符合LEGB原则
1 用来修改当前作用域上一级的局部变量
2 如果上一级没有,就向上一级一次寻找
3 如果再也找不到了,直接报错
'''

def outer():
	a = 13
	def inner():
		a = 15
		print(a)
	inner()
	print(a)
outer()

def outer():
	a = 13
	def inner():
		nonlocal a
		a = 15
		a = 100
		print(a)
	inner()
	print(a)
outer()

# 2 如果上一级没有,在向上一级依次寻找
def outer():
	def inner():
		b = 100
		def smaller():
			nonlocal b
			b = 111
			print(b)
		smaller()
		print(b)
	inner()
outer()

# 3 如果再也找不到,直接报错 nonlocal 只修改局部变量

# 4 不通过nonlocal,是否可以修改局部变量(列表不是变量)
def outer():
	lst = [1,2,3]
	def inner():
		lst[-1] += 10
	inner()
	print(lst)
outer()


