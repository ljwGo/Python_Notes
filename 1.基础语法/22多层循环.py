# ### 双层循环练习

#十行十列小星星

i = 0
while i < 100:
	print("*",end = '')
	if i % 10 == 9:
		print()
	i += 1

i = 0
strvar = ''
while i < 100:
	strvar += '*'
	if i % 10 == 9:
		strvar += "\n"
	i += 1
print(strvar)

print("<=======>")
j = 0
while j <10:

	#逻辑代码写在下面
	#打印一行是个小星星
	i = 0
	while i < 10:
		print('*',end = '')
		i += 1
	#打印换行
	print()

	j += 1

print("<======>")
j = 0
while j < 10:
	i = 0
	while i < 10:
		if i % 2 == 0:
			print("*",end = '')
		else:
			print("+",end = '')
		i += 1
	print()
	j += 1

print('<======>')
j = 0
while j<10:
	i = 0
	if j%2 == 0:
		while i<10:
			print("*",end = '')
			i+=1
	else:
		while i<10:
			print("+",end = '')
			i+=1
	print()
	j+=1

j = 0
while j < 10:
	i = 0
	while i < 10:
		if j % 2 == 0:
			print("*",end = '')
		else:
			print("+",end = '')
		i += 1
	print()
	j += 1

# 99乘法表
j = 1
while j <10:
	i = 1
	while i<=j:
		print('%d*%d=%-2d ' % (j,i,i*j),end = '')
		i+=1
	print()
	j+=1

print('<======>')
i = 9
while i>0:
	j = 1
	while j<=i:
		print('%d*%d=%-2d ' % (i,j,i*j),end = '')
		j+=1
	print()
	i-=1

print("<======>")
j = 1
while j <10:

	# 打印空格
	k = 9 - j
	while k > 0:
		print("       ",end = '')
		k-=1
	# 打印星星

	i = 1
	while i<=j:
		print('%d*%d=%-2d ' % (j,i,i*j),end = '')
		i+=1
	print()
	j+=1

print('<======>')
i = 9
while i > 0:
	k = 9 - i
	while k > 0:
		print('       ',end = '')
		k -= 1
	j = 1
	while j <= i:
		print('%d*%d=%-2d ' % (i,j,i*j),end = '')
		j += 1
	print()
	i -= 1


#求吉利数字100 ~ 999 123 321 111 222 333 ... 666 888 567 765
"""
765

个位: 765 % 10 => 5
十位: 765 // 10 % 10 => 6
百位: 765 // 100 => 7

地板除可以获取数据高位,取余可以获得数据低位

"""
i = 100
while i <= 999:
	# 个位
	gewei = i % 10
	# 十位
	shiwei = i // 10 % 10
	# 百位
	baiwei = i // 100
	print(baiwei,shiwei,gewei)

	#555 666 777
	if shiwei == gewei and shiwei == baiwei:
		print(i)

	i += 1

#方法二
i = 100
while i <= 999:
	num = str(i)
	geiwei = int(num[-1])
	shiwei = int(num[1])
	baiwei = int(num[0])

	i += 1

'''
strvar = '789'
strvar[0]
strvar[1]
strvar[-1]

只有字符串时才可以利用下标(索引)简单列出个位,十位,百位;而只有整形才可以利用运算符号+ -

'''

#百钱买百鸡,公鸡1块钱一只,母鸡3块钱一只,小鸡0.5元一只,有多少种买法?

i = 0
x = 0
while x <= 100:
	y = 0
	while y <= 33:
		z = 100 - x - y
		if x + 3*y + 0.5*z == 100:
			i += 1
		y += 1
	x += 1
print(i)

'''
穷举法:一个一个试
a = [1,2]
b = [3,4]
c = [5,6]
a + b + c = 10?
1 + 3 + 5 = 9
1 + 3 + 6 = 10
1 + 4 + 5 = 10
1 + 4 + 6 = 11
2 + 3 + 5 = 10
2 + 3 + 6 = 10
2 + 4 + 5 = 11
2 + 4 + 6 = 12
'''

x = 0
while x <= 100:

	y = 0
	while y <= 33:

		z = 0
		while z <= 100:

			if (x + y + z == 100) and (x + 3*y + 0.5*z == 100):
				print(x,y,z)
			z += 1

		y += 1

	x += 1






