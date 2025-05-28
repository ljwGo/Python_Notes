# ### 1 如何使用类中的私有成员
class Plane():
	# 公有属性
	captain = '王文'
	# 私有属性
	__air_sister = 18

	# 公有绑定对象方法
	def fly1(self):
		print('飞机会飞,百公里油耗100L')

	# 公有无参数普通方法
	def fly2():
		print('飞机会飞,百公里油耗200L')

	# 私有绑定对象方法
	def __fly3(self):
		print('飞机会飞,百公里油耗300L')

	# 私有吴婵书普通方法
	def __fly4():
		print('飞机会飞,百公里油耗400L')

	# 定义一个公有方法,调取类中的成员
	def pub(self):
		# self => obj => obj.captain
		self.captain
		# 利用类内的公有方法,间接获取类中的私有成员
		self.__air_sister
		# 调用公有方法
		self.fly1()
		# 调用私有方法
		self.__fly3()

	# 定义一个公有普通方法,调取类中的成员
	def pub2():
		print(Plane.captain)
		print(Plane.__air_sister)
		Plane.fly2()
		Plane.__fly4()

# 实例化对象
obj = Plane()
# 1 私有成员的改名策略: _类名__私有名字
print(Plane.__dict__)
# 调用私有属性
print(Plane._Plane__air_sister)
# 调用私有方法
obj._Plane__fly3()

# self 形参接收到obj这个对象
obj.pub()
Plane.pub2()

# ### 2 删除类对象中的成员
'''删除的时候,看清该成员的归属'''
# 删除对象中的成员
# 直接del obj.captain会报错,因为在对象中没定义captain,类中的captain不会被复制到对象中
# 删除属性
obj.captain = '朱景城'
print(obj.captain)
del obj.captain
print(obj.captain)

print(obj.__dict__)

# 删除方法
obj.func1 = lambda : print('可恶')
obj.func1()
del obj.func1

# 删除类中的成员
# 删除属性
del Plane.captain
print(Plane.captain)

# 删除方法
del Plane.pub
Plane.pub(obj)

# 删除私有成员
# del 私有名





