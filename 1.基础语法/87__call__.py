# ### __call__ 魔术方法
'''
	触发时机: 把对象当做函数调用的时候自动触发
	功能: 模拟函数化操作
	参数: 参数不固定,至少一个self参数
	返回值: 看需求
'''
# 1 基本语法
class MyClass():
	def __call__(self):
		print('call方法被触发')
obj = MyClass()
obj()

# 2 洗衣服的过程 可以使用__call__统一调用方法
class Wash():
	def __call__(self,something):
		print('这是{}的方法'.format(something))
		obj.step1()
		obj.step2()
		obj.step3()
		return something

	def step1(self):
		print('把衣服扔进洗衣机里,把洗衣粉扔进洗衣机里,搅拌')

	def step2(self):
		print('加水,开启快关,把门关上')

	def step3(self):
		print('把衣服拿出来,晒一晒')

obj = Wash()
'''
# 方法一
obj.step1()
obj.step2()
onj.step3()
'''
# 方法二
# obj()
res = obj('洗衣服')
print(res)

# 模拟int方法,自定义类
'''bool int float 字符串'''
import math
class MyInt():

	def myfunc(self,num,sign=1):
		res = num.lstrip('0')
		if  res == "":
			return 0
		return eval(res) * sign

	def __call__(self,n):
		# 判断是不是bool
		if isinstance(n,bool):
			if n == True:
				return 1
			else:
				return 0
		# 判断是不是int
		elif isinstance(n,int):
			return n
		# 判断是不是字符串
		elif isinstance(n,float):
			if n > 0:
				return math.floor(n)
			else:
				return math.ceil(n)
		# 判断是不是字符串
		elif isinstance(n,str):
			sign = 1
			# 判定是否带符号 + -
			if (n[0] == '+' or n[0] == '-') and n[1::].isdecimal():
				if n[0] == '+':
					sign = 1
				elif n[0] == '-':
					sign = -1
				return self.myfunc(n[1::],sign)
			elif n.isdecimal():
				return self.myfunc(n)
			else:
				return '老弟,这个算不了'
		else:
			return '老弟这个算不了'

myint = MyInt()
res = myint(False)
res = myint(20)
res = myint(-641.55)
res = myint('-00000000')
print(res)






