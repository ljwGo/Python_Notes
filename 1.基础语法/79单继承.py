# ### 继承 : 一个类除了自身所拥有的属性方法外,还获取了另外一个类的成员属性和方法
'''
面向对象的三大特征:封装,继承,多态
一个类可以继承另外一个类,那么当前类是子类(衍生类),被继承的类是父亲(基类,超类)
python中继承的种类:
	1 单继承
	2 多继承

object 是所有类的父亲

'''
class Human():
	hair = '褐色'
	__age = 18
	def eat(self):
		print('吃好吃的')
	def sleep(self):
		print('打呼噜')
	def __makebaby(self):
		print('....')

# 子类继承父类之后,子类可以调用父类的公有成员
class Man(Human):
	pass

obj = Man()
print(obj.hair)
obj.eat()

# 2 子类不可以调用父类的私有成员
'''
class Woman(Human):
	def pub(self):
		# 无法调用父类私有成员,可以调用公有成员
		print(self.age)
obj = Woman()
obj.pub()
'''

# 3 子类可以改写父类公有成员
class Children(Human):
	def eat(self):
		print('可爱的小孩')

obj = Children()
obj.eat()





