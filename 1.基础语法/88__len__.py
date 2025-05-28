# ### __str__ 魔术方法
'''
	触发时机: 使用print(对象)或者str(对象)的时候触发
	功能: 查看对象
	参数: 一个self接受当前对象
	返回值: 必须返回字符串类型
'''
class Cat():
	gift = '卖萌,喵喵喵'
	def __init__(self,name):
		self.name = name

	def cat_info(self):
		return '小猫的名字{},小猫的天赋{}'.format(self.name,self.gift)

	def __str__(self):
		return self.cat_info()

tom = Cat('汤姆')
# 方式一
print(tom)
# 方式二
res = str(tom)
print(res)

# __repr__ 魔术方法
'''
	触发时机: 使用repr(对象)的时候触发
	功能: 查看对象,与魔术方法__str__相似
	参数: 一个self接受当前对象
	返回值: 必须返回字符串类型
'''
class Mouse():
	gift = '偷奶酪'
	def __init__(self,name):
		self.name = name

	def mouse_info(self):
		return '小老鼠名字{},天赋{}'.format(self.name,self.gift)

	def __repr__(self):
		return self.mouse_info()
	# 在系统底层默认加入了如下一句话
		__str__ = __repr__

jerry = Mouse('杰瑞')
res = repr(jerry)
print(res)

# ### __bool__ 魔术方法
'''
	触发时机: 使用bool(对象)的时候自动触发
	功能: 强转对象
	参数: 一个self接受当前对象
	返回值: 必须是布尔类型
'''
class MyClass():
	def __bool__(self):
		return False

obj = MyClass()
res = bool(obj)
print(res)

# __add__ 魔术方法 (与之相关的__radd__ 反向加法)
'''
	触发时机: 使用对象进行运算相加的时候自动触发
	功能: 对象运算
	参数: 两个对象参数
	返回值: 运算后的值
'''
class MyClass():
	def __init__(self,num):
		self.num = num

	def __add__(self, other):
		print('add方法被触发')
		'''
		self 接受的是obj对象
		other 接受的是数字
		'''
		print(self)
		print(other)
		return self.num + other

	def __radd__(self,other):
		print(333)
		'''
		self 接收的是对象b
		other 接受的是3
		'''
		return self.num + other * 3

# 1 add 方法
obj = MyClass(10)
res = obj + 1
print(res)

# 2 radd 方法
b = MyClass(5)
res = 3 + obj

# 3 对象 + 对象
'''
先触发add方法
self 接受a
other 接受b
return self.num + other => return 10 + b
res = 10 + b

后触发radd方法
self 接受b
other 接受10
return self.num + other * 3 => 5 + 10 * 3
'''
res = obj + b
print(res)

# __sub__  减法    __mul__  乘法    __truediv  真触发
# __len__ 魔术方法
'''
	触发时机: 使用len(对象)的时候自动触发
	功能: 用于检测对象中或者类中某个内容的个数
	参数: 一个self接受当前对象
	返回值: 必须返回整形
'''
class MyClass():
	pty1 = 1
	pty2 = 2
	__pty3 = 3

	def func1(self):
		print(1)
	def func2(self):
		pass
	def __func3(self):
		pass
	def __len__(self):
		dic = MyClass.__dict__
		print(dic)
		'''
		# {'__module__': '__main__', 'pty1': 1, 'pty2': 2, '_MyClass__pty3': 3, 'func1': <function MyClass.func1 at 0x0051D4A8>, 'func2': <function MyClass.func2 at 0x0051D460>, '_MyClass__func3': <function MyClass.__func3 at 0x0051D418>, '__len__': <function MyClass.__len__ at 0x0051D3D0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
		# 方法一
		lst = []
		for i in dic:
			if not i.startwiths('__') and i.endwiths('__'):
				lst.append(i)	
		return len(lst)
		'''
		# 方法二
		return len([i for i in dic if not (i.startswith('__') and i.endswith('__'))])

obj = MyClass()
res = len(obj)
print(res)



