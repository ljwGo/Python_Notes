# ### 多继承 : 一个子类有多个父亲
class Father():
	f_property = '玉树临风,花见花开,一枝梨花压海棠'
	def f_hobby(self):
		print('抽烟喝酒,坑蒙拐骗偷')

class Mother():
	m_property = '俏皮可爱,沉鱼落雁,一枝红杏出墙来'
	def m_hobby(self):
		print('打麻将,买包包')

class Daughter(Father,Mother):
	pass

obj = Daughter()
print(obj.f_property)
obj.m_hobby()

# super的使用
'''
1 super 本身是一个类 super() 是一个对象,用于调用父类的绑定方法
2 super() 只能应用在绑定方法中,默认自动传递self对象(前提:super所在作用域存在self)
3 super用途:解决复杂的多继承调用顺序
'''
class Father():
	f_property = '玉树临风,花见花开,一枝梨花压海棠'
	def f_hobby():
		print('抽烟喝酒,坑蒙拐骗偷')

class Mother():
	m_property = '俏皮可爱,沉鱼落雁,一枝红杏出墙来'
	def m_hobby(self):
		print('打麻将,买包包')

class Son(Father,Mother):
	f_property = '头发是白的'
	m_property = '皮肤黑色'

	# 1 子类调用父类方法
	def skill1(self):
		print(Father.f_property)
		Father.f_hobby()
	# 2 利用self调用父类的成员属性和方法
	def skill2(self):
		print(self.m_property)
		self.m_hobby()
	# 3 利用super调用父类的成员属性和方法
	def skill3(self):
		print(super().f_property)
		super().m_hobby()

obj = Son()
obj.skill1()
obj.skill2()
obj.skill3()

'''
self 与 super 的区别
	self 在调用父类成员时,如果自己本类含有该成员,调用自己的,否则调用父类的
	super 永远只调用父类成员,不调用自己本类的
'''









