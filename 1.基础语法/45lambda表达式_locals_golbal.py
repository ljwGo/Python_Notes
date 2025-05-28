# ### locals 和 globals
# globals() : 返回字典,存放着全局作用域的所有内用,可以动态的创建变量
# globals()
'''在函数外,获取globals打印之前所有变量内容,形成字典,获取全局作用域的内容'''
a = 1
b = 2
res = globals()
c = 3
print(res)

a1 = 'asd'
b2 = 'afwa'
'''在函数内,获取globals调用之前的所有变量,形成字典,获取全局作用域的内容'''
def func():
	a = 1
	b = 2
	res = globals()
	c = 3
	print(res)
d = 'wfsz'
func()
c3 = 'wfawefsz'

# locals() :
# locals
'''在函数外,获取locals打印之前所有变量的内容,形成字典,获取全局作用域的内容'''
a = 1
b = 2
res = locals()
c = 3
print(res)

# 在函数内
'''在函数内,获取locals调用之前所有变量内容,形成字典,获取局部变量作用域的内容'''
def func():
	a = 1
	b = 2
	res = locals()
	c = 3
	print(res)
func()

#声明变量
wangwen = '真帅'

# globals创建一个全局变量 : 返回的是全局字典,通过在字典中添加键值对,来动态创建变量,键就是变量的名,值就是变量的值
dic = globals()
print(dic)
dic['yangmazi'] = '真聪明'
print(yangmazi)

# globals 创建多个全局变量
'''p1~p5 5个变量'''
def func():
	dic = globals()
	print(dic)
	for i in range(5):
		dic['p' + str(i)] = i
func()



# ### 匿名函数 : lambda表达式
'''
用一句话来表达只有返回值的函数
特点: 简介,高效
语法:
	lambda 参数 : 返回值
'''

# 1 没有参数的lambda 表达式
def func():
	return '我是func函数'

# 改写
func = lambda : '我是func函数'
res = func()
print(res)

# 2 有参数的lambda 表达式
def func(n):
	return type(n)

# 改写
func = lambda n : type(n)
res = func(4.44)
print(res)

# 3 带有判断条件的lambda 表达式
def func(n):
	if n % 2 == 0:
		return '偶数'
	else:
		return '奇数'
res = func(3)
print(res)

# 三目运算符
'''
真区间值 if 条件表达式 else 假区间值
如果条件表达式满足,
	就返回真区间值
	否则,返回假区间值
'''

def func(n):
	return '偶数' if n % 2 == 0 else '奇数'

res = func(3)
print(res)

# 改写
func = lambda n : '偶数' if n % 2 == 0 else '奇数'
res = func(4)
print(res)

#比较两个数的大小,返回最大值
def func(a,b):
	if a > b:
		return a
	elif a < b:
		return b

#改写
func = lambda a,b : a if a > b else b
res = func(2,3)
print(res)




