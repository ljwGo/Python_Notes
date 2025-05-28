# ### __new__ 魔术方法
'''
	触发时机: 实例化类生成对象的时候触发(触发时机在__init__之前)
	功能: 控制对象的创建过程
	参数: 至少一个cls接受当前的类,其他根据情况决定
	返回值: 通常返回对象或者None
'''
# 1 基本语法
'''
借助object父类中的__new__魔术方法,创建对象
需要传递cls这个参数,代表的是本类,为本类创建对象,进行返回
'''
class MyClass2():
	b = 2
obj2 = MyClass2()

class MyClass1():
	a = 1
	def __new__(cls):
		print(cls) # <class '__main__.MyClass'>
		# 借助父类object,里面的__new__魔术方法创建对象
		# 返回本对象
		# return object.__new__(cls)
		# 返回其他类的对象
		# return obj2
		# 不返回任何对象
		#return None

'''
obj = MyClass1()
print(obj)
# 返回本类对象
print(obj.a)
# 返回其他类对象
print(obj.b)
'''

# 2 验证__new__和__init__两个方法的触发时间
'''
__new__ 用来创建对象
__init__ 用来初始化对象的
先创建再初始化
'''
class MyClass():
	def __new__(cls):
		print(1)
		return object.__new__(cls)

	def __init__(self):
		print(2)

obj = MyClass()

# 传一个参数的情况
class MyClass():
	def __new__(cls,name):
		return object.__new__(cls)

	def __init__(self,name):
		self.name = name

obj = MyClass('周永玲')

# 传多个参数的情况
class MyClass():
	# 多个参数下,用收集参数来保证形参实参一一对应
	def __new__(cls, *args, **kwargs):
		return object.__new__(cls)

	def __init__(self,name,skin,age):
		self.name = name
		self.skin = skin
		self.age = age

obj = MyClass('周友玲','绿色',108)
print(obj.name)
# 注意点
'''
如果__new__返回的不是自己本类的对象,不会触发__init__

'''
class MyClass():
	def __new__(cls):
		print(1)
		return obj2

	def __init__(self):
		print(2)

obj = MyClass()




