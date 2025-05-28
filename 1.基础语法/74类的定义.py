class Car: # 定义一个类
	color = '黄色的' # 成员属性
	def didi(self):	# 成员方法
		print(self.color+'车会滴滴滴的叫')
mycar = Car()
# 适用对象调用一个属性
print(mycar.color)

# ### oop 面向对象程序开发
'''
用几大特征表达一类事物类更像是一张图纸,表达的是一个抽象概念
对象是类的实例,类是对象的模板
'''

# 1 类的定义
class Car:
	pass
class Car():
	pass
class Car(object):
	pass

# 2 类的实例化
class Car():
	pass
# 实例化对象 产生obj对象
obj = Car()

# 3 类的基本结构
class Car():
	# 成员属性
	color = '绿色'
	# 成员方法
	def didi(self):
		print('小车会滴滴的叫')

# 语法上允许,但是严禁使用
class Car():
	if 5 == 5:
		print(12345)

# 改成
class Car():
	def func(self):
		if 5 == 5:
			print(1234)

# 4 类的命名
'''
驼峰命名法:推荐使用大驼峰命名法 -> mycar =
'''
class MyHouse():
	pass