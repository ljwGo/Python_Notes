# 把类当成一个参数传递到函数中,形成一个独立的副本
class MyClass():
	a = 1

def func(cls):
	cls.ad = 2
	return cls()

obj = func(MyClass)
MyClass = 1
print(MyClass)
print(obj.ad)

# 可以在函数内部创建类,但是作用域只限定在函数的内部,外部不可见
def func():
	class C():
		cbb = 10
	obj = C()
	return obj
obj = func()
print(obj.cbb)

# ### 类中的方法
'''
无参数的普通方法: 只能用类调用
绑定方法:
	1 绑定到类: 在调用时,自动传递self对象参数
	2 绑定到类: 在调用时,自动传递cls这个类参数
静态方法:
	无论是对象还是类都可以调用,把方法作为普通方法进行使用
'''

class Dog():
	def __init__(self,name):
		self.name = name
	# 无参数普通方法
	def eat():
		print('小狗喜欢吃屎')
	# 绑定到对象的方法
	def tail(self):
		print('小狗看见主人,喜欢摇尾巴')
	# 绑定到类的方法
	@ classmethod
	def jump(cls):
		print('小狗喜欢接')
	# 静态方法
	@ staticmethod
	def jiao():
		print('看见主人就洋洋叫')

obj = Dog('王文')
# 无参数普通方法
# obj.eat() error
Dog.eat()

# 绑定到对象的方法
obj.tail()
Dog.tail(obj) # 不推荐

# 绑定到类的方法
Dog.jump() # 推荐
obj.jump()

# 静态方法 : 有几个参数就传递几个参数,跟普通方法的调用一样
# Dog.jiao()
obj.jiao()

# ### property
'''
把方法变成属性:用来控制成员的 获取,设置,删除 
@property 获取
@方法名.setter 设置
@方法名.deleter 删除
'''
# 写法一
class MyClass():
	def __init__(self,name):
		self.name = name

	# 获取
	@property
	def username(self):
		return self.name

	# 设置
	@username.setter
	def username(self,val):
		self.name = val

	# 删除
	@username.deleter
	def username(self):
		del self.name

obj = MyClass('周永玲')
# 获取username 触发property修饰的方法
res = obj.username
print(res)

# 设置username 触发username.setter修饰的方法
obj.username = '王永林'
print(obj.username)

# del obj.username 触发username.deleter装饰器修饰的方法
del obj.username
# print(obj.username)

# 写法二
'''
class MyClass():
	def __init__(self,name):
		self.name = name
	# 获取属性
	def get_username(self):
		return self.name
	# 设置属性
	def set_username(self,val):
		self.name = val
	# 删除属性
	def del_username(self):
		del self.name

	# 获取方法,设置方法,删除方法
	username = property(get_username,set_username,del_username)

obj = MyClass('李四')
# 获取属性 自动触发get_username方法
res = obj.username
print(res)
# 设置属性 自动触发set_username方法
obj.username = '黄乐喜'
print(obj.username,type(obj.username))
# 删除属性 自动触发del_username方法
del obj.username
#print(obj.username)
'''