# 1 {'x':'A'.'y':'B','z':'C'} 把字典写成x=A,y=B,z=C的列表的推导式
dic = {'x':'A','y':'B','z':'C'}
lst = [i + '=' + dic[i] for i in dic]
print(lst)

# 2 把列表中所有字符变成小写 ['ADDD','ddDD','DDaa','sss']
lst = ['ADDD','ddDD','DDaa','sss']
lst = [i.lower() for i in lst]
print(lst)

# 3 x 是0-5之间的偶数,y 是0-5之间的奇数,把x,y组成一起变成元组,放到列表中
# 方法一
for i in range(6):
	for j in range(6):
		if i % 2 == 0 and i % 2 == 1:
			res = (i,j)
			lst.append(res)
lst = [(i,j) for i in range(6) for j in range(6) if i % 2 == 0 and j % 2 == 1]
print(lst)

# 方法二
for i in range(6):
	if i % 2 == 0:
		for j in range(6):
			if j % 2 == 1:
				lst.append((i,j))
print(lst)

# 改写成推导式
lst = [(i,j) for i in range(6) if i % 2 == 0 for j in range(6) if j % 2 == 1]
print(lst)

# 4 使用列表推导式 制作所有99乘法表中的运算
i = 1
while i <10:
	j = 1
	while j <= i:
		print('%d*%d=%-2d ' % (i,j,i*j),end = '')
		j += 1
	print()
	i += 1

# 改写成推导式
lst = ['%d*%d=%-2d ' % (i,j,i*j) for i in rang(1,10) for j in rang(1,i+1)]
print(lst)

# 实现矩阵运算
'''
lst = [M[i][j]*N[i][j] for i in range(3) for j in range(3)]
lst = [[M[i][j]*N[i][j] for j in range(3)] for i in range(3)]
'''




