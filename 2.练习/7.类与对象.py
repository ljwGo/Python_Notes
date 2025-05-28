# ### 作业

# 1
class Person():
	animal = '高级动物'
	soul = '有灵魂'
	language = '语言'

	def __init__(self,country,name,sex,age,height):
		self.country = country
		self.name = name
		self.sex = sex
		self.age = age
		self.height = height

	def eat(self):
		print('{}在吃饭'.format(self.name))

	def sleep(self):
		pass
	def work(self):
		pass

p1 = Person('中国','alex','未知',42,175)
p2 = Person('美国','武大','男',35,160)
p3 = Person('加拿大','黄乐喜','女',18,150)
p4 = Person(p1.country,p2.name,p3.sex,p2.age,p3.height)

# alex 在吃饭
p1.eat()
print(p1.animal)
print(p2.soul)
print(p3.language)

# 2
class Person():
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def func(self):
		lst = ['上山去砍柴','开车去东北','最爱大保健']
		for i in lst:
			print('{},{}岁,{},{}'.format(self.name,self.age,self.sex,i))
obj = Person('小明',10,'男')
obj.func()
obj2 = Person('老李',90,'男')
obj2.func()

# 3
class Game_role():
	def __init__(self,name,ad,hp):
		self.name = name
		self.ad = ad
		self.hp = hp

	def attack(self,other):
		print('{}攻击{},{}掉了{}血,{}还剩{}血'.format(self.name,other.name,other.name,self.ad,other.name,other.hp-self.ad))

gailun = Game_role('盖伦',10,100)
yasuo = Game_role('剑豪',20,80)
gailun.attack(yasuo)

# 4
import math
class Circle():
	def __init__(self,r):
		self.r = r

	# 计算周长
	def perimeter(self):
		return 2 * math.pi * self.r

	# 计算面积
	def area(self):
		#return math.pi * pow(self.pi,2)
		return math.pi * self.r ** 2

obj = Circle(10)
print(obj.perimeter)
print(obj.area())

# 5
class A():
	abc = 5

class B():
	def __init__(self,obj):
		self.pty = obj

obj1 = A()
obj2 = B(obj1)
print(obj2.pty.abc)
