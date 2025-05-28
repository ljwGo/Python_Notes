'''
def outer(n):
	def zhuangshiqi(func):
		def newfunc():
			print(111)
			func()
			print(222)
		return newfunc

@ outer
def func():
	print(333)

print(func) # 返回值为 None
'''

'''
def tuozhan(func):
	def newfunc(name):
		print(111)
		func(name)
	return newfunc
@ tuozhan
def func(name):
	print('我的名字是{}'.format(name))
func('赖建威')
'''

'''
class KuoZhan():
	def __init__(self,x,add,app):
		self.x = x
		self.add = add
		self.app = app
		
	def __call__(self,cls):
		if self.x == 1:
			return self.kuozhan1(cls)
		
	
	def kuozhan1(self,cls):
		def newfunc():
			cls.add = self.add
			cls.app = self.app
			return cls()
		return newfunc
'''













