# ### 多态 : 不同的子类对象,调用相同的父类方法,产生不同的执行结果
'''
	关键字: 继承 ,重写
	特点: 在不改变原有代码的前提下,而实现不同效果 , 多态针对的是对象
'''

# isinstance 判断对象是否是该类型[在一条继承链上即可]
#res = isinstance(obj_army,Army)
#print(res)

# issubclass 判断是否是子父关系
#res = issubclass(Army,ceshi)

class ceshi():
	pass

class Soldier():
	def attack(self):
		pass

	def back(self):
		pass

# 陆军
class Army(Soldier):
	def attack(self):
		print('[陆军]你砍我,我砍你,一刀999')

	def back(self):
		print('[陆军]撒腿就跑,畏罪潜逃')

# 海军
class Navy(Soldier):
	def attack(self):
		print('[海军]扔鱼叉,插死一个算一个')

	def back(self):
		print('[海军]跳海喂鱼')

# 空军
class AirForce(Soldier):
	def attack(self):
		print('[空军]意大利炮,射击')

	def back(self):
		print('[空军]直接跳伞,落地成盒')

# 创建陆军士兵
obj_army = Army()
# 创建海军士兵
obj_navy = Navy()
# 创建空军士兵
obj_air = AirForce()

# 给就为准备
listvar = [obj_army,obj_navy,obj_air]

# 将军下命令
strvar = '''
1 全体出击
2 全体撤退
3 空军上,其他人迅速撤离
'''

sign = True
while sign:
	print(strvar)
	num = input('将军,请下令')
	#if num.isdecimal():
	if num in ['1','2','3']:
		num = int(num)
		for i in listvar:
			if num == 1:
				i.attack()
			elif num == 2:
				i.back()
			elif num == 3:
				if isinstance(i,AirForce):
					i.attack()
				else:
					i.back()
	elif num.upper() == 'Q':
		sign = False
		break





