# ### oop 封装
'''
类的相关操作
语法:
	类.属性
	类.方法


'''
class MyCar():
	# 公有属性
	oil = 2.0
	# 稀有属性
	__price = '80万'

	# 公有方法
	def oil_info(self):
		print('我的百公里油耗2.0')
	# 私有方法
	def __price(self):
		print('车的成本价格保密')

print(MyCar.__dict__)
# 实例化对象
obj = MyCar()
obj.oil_info()
# 1 定义的类访问公有成员属性和方法
# 调用属性
print(MyCar.oil)
# 调用方法
MyCar.oil_info(1)

# 2 定义的类动态添加公有成员属性和方法
# 添加属性
MyCar.logo = '丰田'
print(MyCar.logo)
# 添加方法(同对象,但无需使用type.MethodType,系统会自动添加自身)

# 调用类中的方法时,无法调用无参数方法
# obj.abc = 10
# print(MyCar.abc)
'''
总结:
	对象调用成员时,先找该对象中是否存在
	如果有调用自己的,如果没有,调类的(公有的)

	对象调用类中成员是单向的,类不能反过来调用对象中的成员
	
	无论是类还是对象,其中的成员都归属与自己本省,
	对象如果没有回去调用类中成员,但是类没有的话不会调用对象
	是单向的,对象和类都不能互相修改或者删除对方的成员
'''




