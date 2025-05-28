# ### 循环结构 while
"""
while 条件表达式:
	code1
	code2
当条件表达式成立True,就执行while循环体中的代码内容
"""

# 打印1~100所有的数据
# 初始化变量

# 1初始化变量i
i = 1
# 2循环的条件
while i <= 100:

	#4写上要执行的逻辑
	print(i)

	#3自增自减的值
	i += 1


"""
# 代码解析:
i = 1 i<=100 真的,条件成立,执行循环里面的代码块print(1) i+=1 i=>2
i = 2 i<=100 真的,条件成立,执行循环里面的代码块print(2) i+=1 i=>3
...
...
i = 101 i<=100 ,假的,条件不成立,循环终止
"""

# 注意:死循环
'''
while True:
	print(1)
'''


# 计算1~100的累加和

#方法一
total = 0
i = 1
while i <= 100:
	total += i
	i += 1
print(total)

#方法二
sign = True
i = 1
total = 0
while sign:
	total += i
	i += 1
	if i == 101:
		sign = False
print(total)

# 打印 一行十个小星星
"""help,查看帮助文档"""
help(print)