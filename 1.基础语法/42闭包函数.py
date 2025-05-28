# ### 闭包函数
'''
生命周期从长到短:
	内置空间变量 > 全局空间变量 > 局部空间变量
	内置空间变量 : 在解释器退出之后,就会释放空间
	全局空间变量 : 在文件执行结束之后,就会释放空间
	局部空间变量 : 在调用完函数之后,就会释放空间
定义: 内函数使用了外函数的局部变量,外函数把内函数返回出来的过程,叫做闭包,这个函数就叫做闭包函数


'''

# 1 基本语法
def zuoyonglin_family():
	father = '王健林'
	def hobby():
		print('先设定一个小目标,赠他一个亿,这是我爸爸%s' % (father))
	return hobby

func = zuoyonglin_family() # func = hobby

'''
def func():
	a = 500
func()
print(a)
'''

# 获取闭包函数使用的变量 __closure__ , cell_contents(了解)
# 获取单元格对象,这个对象中含有延长生命周期的变量值
tuple = func.__closure__ #(<cell at 0x00582E50: str object at 0x0031E2F8>,)
print(tuple)
print(tuple[0])
# cell_contents 这个属性可以获取单元格对象中的值,如果有证明是一个闭包,如果没有,就不是一个闭包
print(tuple[0].cell_contents)
# 2 升级闭包函数
'''内函数使用了外函数的局部变量,那么这个局部变量与内函数发生绑定,延长该变量的生命周期'''
def huanglexi_family():
	jiejie = '马蓉'
	meimei = '马诺'
	money = 1000

	def jiejie_hobby():
		nonlocal money
		money -= 700
		print('爱包包,爱手表,爱首饰,家里的钱花的还剩下%s' % (money))

	def meimei_hobby():
		nonlocal money
		money -= 200
		print('宁愿在宝马里哭,也不愿意再自行车上面笑,家里的钱都败光了,还剩下%s' % (money))

	def big_master():
		return jiejie_hobby,meimei_hobby
	return big_master

func = huanglexi_family()
print(func)
tuple = func()
print(tuple) #(<function huanglexi_family.<locals>.jiejie_hobby at 0x002EB1D8>, <function huanglexi_family.<locals>.meimei_hobby at 0x002EB190>)
# 获取闭包函数
jiejie = tuple[0]
meimei = tuple[1]
# 调用函数
jiejie()
meimei()



