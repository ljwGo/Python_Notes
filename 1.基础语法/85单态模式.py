# ### 单态模式 : 无论实例化对象多少次,都有且只有一个对象
'''为了节省空间,加快效率,提出单态模式'''
class Singleton():
	__obj = None
	def __new__(cls, *args, **kwargs):
		if cls.__obj is None:
			cls.__obj = object.__new__(cls)
		return cls.__obj

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)
print(obj1 is obj2)

# 2 单态模式 + 构造方法
class Singleton():
	__obj = None
	def __new__(cls,*args):
		if cls.__obj is None:
			cls.__obj = object.__new__(cls)
		return cls.__obj

	def __init__(self,name):
		self.name = name

obj1 = Singleton('李诗韵')
obj2 = Singleton('黄乐喜')
print(obj1.name)
print(obj2.name)













