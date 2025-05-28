# ### 函数的返回值 return
'''
return 自定义返回值
1 return 后面除了可以接6大标准数据类型之外,还可以跟上类对象或函数 如果不写return,默认返回None
2 return 执行之后,意味着函数终止,后面的代码不执行

'''
res = print(1234)
print(res) #返回值None

# 1 return 第一个只一点
def func():
	#return 1
	#return 5.74
	#return True
	return [1,2,3]

res = func()
print(res)

# 2 return 第二个注意点
def func():
	print(1)
	print(2)
	return 3
	print(4)
	print(5)
res = func()
print(res)
print(res)

# 注意点:如果遇到了return,意味着函数终止不执行
def func():
	for i in range(10):
		if i == 5:
			return 3
		print(i)
res = func()
print(res)
print(res)

# 3 模拟计算器操作
# + - * /
print('<======>')
def calc(sign,sum1,sum2):
	res = None
	if sign == '+':
		res = sum1 + sum2
	elif sign == '-':
		res = sum1 - sum2
	elif sign == '*':
		res = sum1 * sum2
	elif sign == '/':
		if num2 == 0:
			print('除数不能为零')
		else:
			res = sum1 / sum2
	else:
		print('请输入有效字符')
	return res
res = calc('',2,4)
print(res)

'''
def calc(sign,sum1,sum2):
	if sign == '+':
		res = sum1 + sum2
		print(res)
calc('+',1,4)
res = calc('+',3,4) # res只能存储calc的返回值,而本身定义的函数中print代码也会执行
print(res)
# 这种写法可以直接打印出计算后的结果但是无法用变量将结果存储
'''



