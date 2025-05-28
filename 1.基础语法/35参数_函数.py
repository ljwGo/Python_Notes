# ### 函数
# 函数的含义(包裹一部分代码,实现某一功能,达成某一个目的)
# 函数特点(可以反复使用,提高代码的复用性,提高开发效率,便于维护管理)
# 函数的基本格式
"""
# 定义一个函数
def 函数名():
	code1
	code2

# 调用函数
函数名()
"""
# 函数命名
'''
字母数字下划线,首字母不能为数字
严格区分大小写,且不能使用关键字
函数命名有意义,且不能使用中文哦

驼峰命名法:
	1 大驼峰命名法: 每个单词首字符大写 (class类)
	2 小驼峰命名法: 除了第一个单词首字符小写外,其他打次首字符都大写 (函数)

mycar => MyCar大驼峰
mycar => myCar小驼峰
mycar => my_car (推荐这个方法命名函数)
'''

'''
i = 1
while i < 10:
	j = 1
	while j <= i:
		print('%d*%d=%-2d ' % (i,j,i*j),end='')
		j += 1
	print()
	i += 1
'''

'''
# 定义一个函数
def func():
	print('只是一个函数')
# 调用函数
func()
'''

'''
def cheng_fa_biao_99():
	for i in range(1,10):
		for j in range(1,i+1):
			#print('%d*%d=%-2d ' % (i,j,i*j),end='')
			print('{:d}*{:d}={:2d}'.format(i,j,i*j),end='')
		print()

for i in range(1,11):
	cheng_fa_biao_99()
'''

# ### 参数(函数运行时需要的值)
'''
参数:两大类(形参,实参)
形参: 形式参数(普通形参,默认形参,普通收集参数,命名关键字形参,关键字收集参数)

实参: 实际参数(普通实参,关键字实参)

形参 和 实参 要一一对应

形参在函数的定义处
实参在函数的调用处

普通形参 别名也加 位置形参
'''

'''
print('<======>')
for i in range(10):
	for j in range(10):
		print('*',end='')
	print()
'''

# 函数的定义处
'''hang , lie是两个普通形参'''
def xiao_xing_xing(hang,lie):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print('*',end='')
			j += 1
		print()
		i += 1

# 函数的调用处
"""10 和 10在函数的调用处是实参"""
xiao_xing_xing(10,10)

# 2 默认形参
# 函数的定义处
'''hang=10 , lie=10 是两个默认形参'''
#如果给与实际参数,那么使用实际参数;如果没有给与实际参数,那么使用默认参数
def xiao_xing_xing(hang=10,lie=10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print('*',end='')
			j += 1
		print()
		i += 1

# 函数的调用处
xiao_xing_xing()

# 3 普通形参 + 默认参数 (默认形参必须在普通形参的后面)

# 4 关键字实参 [在函数的调用处]
'''
1 关键字实参的顺序可以任意调整
2 如果定义是普通形参,调用时使用的是关键字形参,那么当前形参后面的所有参数都需要使用关键字
'''
def xiao_xing_xing(hang,lie=10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print('*',end='')
			j += 1
		print()
		i += 1
#xiao_xing_xing(hang=2,lie=5)
#xiao_xing_xing(lie=5,hang=2)
#xiao_xing_xing(3,a=55,156,2,35)
