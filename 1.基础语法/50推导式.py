# ### 推导式 : 通过一行循环判断,遍历出一系列数据的方式是推导式
'''
推导式一共三种:
	列表推导式,集合推导式,字典推导式
	[val for val in Iterable]
	{val for val in Iterable}
	{a:b for a,b in Iterable}

'''

# 单循环的推导式
'''[1,2,3,4,5,6,7,8...50]'''
lst = []
for i in range(1,51):
	print(i)
	lst.append(i)
print(lst)

lst = [val for val in range(1,51)]
print(lst)

# 带有判断条件的单循环推导式[判断条件只能是单项分支,其他的不可以]
'''[1,2,3,4,5,6,7,8...50]要所有的偶数'''
lst = []
for i in range(1,51):
	if i % 2 == 0:
		lst.append(i)
print(lst)

# 改写成推导式
lst = [i for i in rangeo(1,51) if i % 2 == 0]
print(lst)

# 多循环推导式 谁爱谁
lst1 = ['长远','林明辉','纸质红']
lst2 = ['李德亮','皮得意','陈佳琪']
lst_new = []
for i in lst:
	for j in lst2:
		strvar = i + '爱' + j
		lst_new.append(strvar)

lst = [i + '爱' + j for i in lst1 for j in lst2]
print(lst)

# 带有判断条件的多循环推导式
lst1 = ['长远','林明辉','纸质红']
lst2 = ['李德亮','皮得意','陈佳琪']
lst_new = []
for i in lst:
	for j in lst2:
		if lst1.index(i) == lst2.index(j):
			strvar = i + '爱' + j
		l	lst_new.append(strvar)
print(lst_new)

# 改写成推导式
lst = [i +'爱'+j for i in lst1 for j in lst2 if lst1.index(i) == lst2.index(j)]





