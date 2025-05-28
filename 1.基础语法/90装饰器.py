# ### 装饰器
'''
定义:装饰器用于拓展原来函数功能的一种语法,返回新函数替换旧函数
优点:在本更改原函数代码的前提下 给函数拓展新的功能
语法:@
'''
# 1 装饰器的原型
def kuozhan(func):
	def newfunc():
		print('厕所前,蓬头垢面')
		func()
		print('厕所后,荣光焕发')
	return newfunc

def func():
	print('我是高富帅')

func = kuozhan(func)
func()

# 2 装饰器@符语法
'''
@符有两个作用:
	1 把@符下面的函数当成一个参数传递给装饰器
	2 装饰器装饰之后,把新函数返回,让新函数去替换就函数(实现在不改变原有代码的前提下,扩展型功能)
'''
def kuozhan(func):
	def newfunc():
		print('厕所前,衣衫褴褛')
		func()
		print('厕所后,光鲜亮丽')
	return newfunc

@kuozhan
def func():
	print('我是白富美')

func()

# 3 装饰器的嵌套
def kuozhan1(func):
	def newfunc():
		print('厕所前,饥肠辘辘')
		func()
		print('厕所后,酒足饭饱')
	return newfunc

def kuozhan2(func):
	def newfunc():
		print('厕所前,洗洗手')
		func()
		print('厕所后,簌簌口')
	return newfunc

@kuozhan2
@kuozhan1
def func():
	print('我是个屌丝')
# 装饰器方向是从下往上看
func()

# 4 用装饰器来装饰带有参数的函数
'''原函数有几个参数,装饰之后就是几个参数,不要大改'''
def kuozhan(func):
	def newfunc(who,where):
		print('厕所前,饥渴难耐')
		func(who,where)
		print('厕所后,满口雌黄')
	return newfunc

@kuozhan
def func(who,where):
	print('{}在{}解手'.format(who,where))

func('黄乐喜','鸟窝')

# 5 用装饰器装饰带有参数返回值的函数
def kuozhan(func):
	def newfunc(*args,**kwargs):
		print('厕所前,萎靡不振')
		res = func(*args,**kwargs)
		print('厕所后,兽性大发')
		return res
	return newfunc

def func(*args,**kwargs):
	dic = {'zyl':'钟永玲','zl':'张龙','zzl':'中赞林'}
	strvar = ''
	for i in args:
		strvar += i + '  '
	print('解手地点:' + strvar)
	lst = []
	for k,v in kwargs.items():
		if k in dic:
			res = dic[k] + '留下了' + v + '黄金'
			lst.append(res)
	return lst
res = func('电影院','水里',zyl='15克',zl='15斤',zzl='15吨',ww='没有')
print(res)

# 推导式 lst = [dic[k] + '留下了' + v + '黄金' for k,v in kwargs.item() if k in dic]

# 6 用类装饰器装饰原函数
class KuoZhan():
	def __call__(self,func):
		return self.kuozhan2(func)
	def kuozhan1(func):
		def newfunc1():
			print('厕所前,干净整齐')
			func()
			print('厕所后,臭气熏天')
		return newfunc1
	def kuozhan2(self,func):
		def newfunc():
			print('厕所前,人模狗样')
			func()
			print('厕所后,原形毕露')
		return newfunc

@ KuoZhan.kuozhan1
def func():
	print('厕所进行时...')
func()

# 方法二
@ KuoZhan() # @ obj => obj(func) 把对象当成函数使用,触发__call__方法
def func():
	print('厕所进行时...')
func()

# 7 用带有参数的装饰器装饰原函数
def outer(n):
	def kuozhan(func):
		def newfunc1(self):
			print(111)
			func(self)
		def newfunc2(self):
			print(222)
			func(self)
		if n == 1:
			return newfunc1
		elif n == 2:
			return newfunc2
		elif n == 3:
			return 5488
	return kuozhan

class MyClass():

	@ outer(1) # @kuozhan
	def func1(self):
		print('向前一小步,文明一大步')
	@ outer(2)
	def func2(self):
		print('来也匆匆,去也冲冲')
	@ outer(3)
	def func3(self):
		print('绿巨人觉得还行')

obj = MyClass()
# 扩展原函数新功能
obj.func1()
obj.func2()
# 把函数变成变量
print(obj.func3)

# 8 用带来参数的类装饰器装饰原函数
'''
如果参数是1,就为当前这个类添加成员属性和方法
如果参数是2,就为当前这个类中的run方法变成属性
'''
class KuoZhan():
	ad = '贵族茅厕,欢迎您来'
	def __init__(self,num):
		self.num = num

	def money(self):
		print('贵族茅厕,每小时收费100元')

	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	def kuozhan1(self,cls):
		def newfunc():
			self.addpty(cls)
			# 返回的是对象
			return cls()
		return newfunc

	def addpty(self,cls):
		cls.ad = self.ad
		cls.money = self.money

	def kuozhan2(self,cls):
		def newfunc():
			return self.chance(cls)
		return newfunc

	def chance(self,cls):
		if 'run' in cls.__dict__:
			cls.run = cls.run()
			return cls()
# 功能一
@ KuoZhan(1) # @obj => obj(Myclass) 把对象当成函数使用了,会触发__call__魔术方法
class MyClass():
	def run(self):
		return '亢龙有悔'
obj = MyClass()
print(obj.ad)
obj.money()

# 功能二
@ KuoZhan(2)
class MyClass():
	def run():
		return '亢龙有悔'
obj = MyClass()
print(obj.run)


