# ### 魔术方法 __del__ (构造方法)
'''
	触发时机: 当对象被内存回收的时候自动触发 [1.页面执行完毕回收所有变量 2.所有对象被del的时候]
	功能: 对象使用完毕后资源回收
	参数: 一个self接受对象
	返回值: 无
'''
# 1 基本使用
class Dog():
	def __init__(self,name):
		self.name = name
	
	def eatmeat(self):
		print('小狗喜欢吃肉包子')
		
	def __del__(self):
		print('构造方法被触发')

# 1 页面执行完毕后回收所有变量
obj = Dog('蛋蛋')
obj.eatmeat()

# 2 所有对象被del的时候
'''
两个变量指向同一个对象,其中删除obj这个变量的指向关系
还有一个变量在指向该对象,所以对象没有被删除,不能够触发结构方法__del__
'''
obj2 = obj
print('start')
del obj
print('end')

import os
# 3 读取文件操作
class ReadFile():
	# 创建对象
	def __new__(cls,file,*args,**kwargs):
		if os.path.exists(file):
			return object.__new__(cls)
		else:
			print('文件不存在')
	# 打开文件
	def __init__(self,file,mode='r',encoding='utf-8'):
		self.fp = open(file,mode = mode,encoding = encoding)
	# 读取文件
	def readfile(self):
		res = self.fp.read()
		return res
	# 关闭文件
	def __del__(self):
		self.fp.close()

obj = ReadFile('ceshi3000.txt')
res = obj.readfile()
print(res)

# 111111
# 构造方法被触发
		
		








