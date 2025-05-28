# ### oop 封装
'''
对象的相关操作
语法:
	对象.属性
	对象.方法

类中的绑定方法:
	1 绑定到对象:在调用当前方法时,系统自动1把该对象当成参数进行传递
	2 绑定到类:在调用当前方法时,系统自动把该类当成参数进行传递
'''
# 定义一个车类
class Car():
	# 公有属性
	color = '屎黄色的'
	# 私有属性
	__logo = '奥利a6'
	# 公有方法
	def drive(self):
		print('小车可以驾驶,载人拉客')
	# 私有方法
	def __price(self):
		print('车的成本价格保密')

# 实例化对象
obj = Car()

# 1 实例化的对象访问公有成员属性和方法
# 调用属性
print(obj.color)
# 调用方法
'''obj.drive 系统自动把obj这个对象传递给drive方法中,self这个参数进行接收'''
obj.drive()

# 2 实例化的对象动态添加公有成员属性和方法
# 添加属性
obj.color = '天蓝色'

# 添加方法
# 1 添加无参数方法
def engine():
	print('我是2.0发动机')
obj.engine = engine

print(obj.__dict__)
# __dict__查看对象或者类中的成员

# 2 添加有参方法
def getname(name):
	print('小车的是名字是',name)
obj.getname = getname
obj.getname('林肯加长版,前后加副轮')

# 升级 1
def carname(obj,name):
	print(obj.color)
	print(name)
obj.carname = carname
obj.carname(obj,'林肯加长板')

# 升级2 形成绑定方法(绑定到对象)
import types
# MethodType(绑定的函数,绑定的对象) 把这个方法绑定到那个对象上
obj.carname = types.MethodType(carname,obj)
obj.carname('林肯加长版') # 只需要

# 3 添加lambda表达式
obj.carlight = lambda : print('把车灯换成手电筒')
obj.carlight()