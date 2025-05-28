# ### 菱形继承
'''
	Human
Man		  Woman
	Children
'''
class Human():
	pty = 1
	def feelT(self):
		print('1天热了,退毛')
		print(self.pty)
		print('2天冷了,长毛')

class Man(Human):
	pty = 2
	def feelT(self):
		print('3喝啤酒,开空调,吃烤串')
		super().feelT()
		print('4洗热水脚,剃光头,喝白酒')

class Woman(Human):
	pty = 3
	def feelT(self):
		print('5吹空调,脱光光,喝热水')
		super().feelT()
		print('6穿貂皮,上火炕,喝热水')

class Children(Man,Woman):
	pty = 4
	def feelT(self):
		print('7打游戏,吃冰棍,敲代码')
		super().feelT()
		print('8穿棉袄,用暖宝宝')

obj = Children()
obj.feelT()

# python2.7版本深度优先 后来改为广度优先
'''
mro列表:方法调用顺序列表
	语法:类.mro() 使用C3算法计算,返回一个列表
	super() 就是按照这个列表的顺序,依次进行调用

'''
lst = Children.mro()
print(lst)
# [<class '__main__.Children'>,
# <class '__main__.Man'>,
# <class '__main__.Woman'>,
# <class '__main__.Human'>,
# <class 'object'>]

# super 就是用来解决多继承,复杂了调用关系(特别是成员名字相同的情况下)

print(object.__dict__)



