# ### 模式方法
'''
__init__ 构造方法
触发时机:实例化对象,初始化的时候触发
功能:为对象添加成员
参数:参数不固定,至少一个self参数
返回值:无

'''
# 1 基本语法
class MyClass():
	def __init__(self):
		self.name = '黄乐喜'

# 实例化对象
obj = MyClass()
print(obj.__dict__)
print(obj.name)

# 2 传递2个参数
class MyClass():
	def __init__(self,name):
		# self.成员属性 = 值
		self.name = name
# 实例化对象
obj = MyClass('李诗韵')
print(obj.name)

# 3 多个对象
'''同一个类,可以实例化出多个对象,而对象和对象之间,彼此独立'''
class Children():
	def __init__(self,name,skin):
		self.name = name
		self.skin = skin

	def eat(self):
		print('小孩天生会吃')

	def drink(self):
		print('小孩天生会喝')

	def __sleep(self):
		print('小孩天生会睡觉')

	def pub(self):
		# 在类中,只能使用对象,属性/方法 或 类.属性/方法进行调用
		print('该对象成员name是{},该对象skin是{}'.format(self.name,self.skin))

# 实例化一个对象
obj = Children('大铁锤','粉色')
obj.pub()

# 实例化第二个对象
obj = Children('王刚蛋','黑色')
obj.pub()

# 实例化第三个对象
wangbaoqiang = Children('王宝强','绿色')
wangbaoqiang.pub()









