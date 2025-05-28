# ### for ... in 循环
'''循环,遍历,迭代 都是指把容器中的数据一个一个获取出来'''
lst = [1,2,3,4,5]
i = 0
while i < len(lst):
	print(lst[i])
	i += 1

'''while 有局限性,无法通过while 它的索引下标获取集合中的值'''
setvar = {'a','b','c'}
"""
for in 的语法:
for 变量 in 可迭代对象:
	code...

可迭代对象(通常用到的是:容器类型数据,range对象,迭代器)

"""

# 遍历集合
container = {'a','b','c','d'}
# 遍历列表(相似)
container = ['a','b','c','d']
#遍历字符串
container = "{'a','b','c','d'}"
#遍历字典
container = {'a':1,'b':2,'c':3,'d':4}
for i in container:
	print(i)

#变量的解包[个数要匹配]
a,b = 1,2
a,b = (1,2)
a,b = [3,4]
a,b = "56" # 字符串有局限性,个数是2个,只能用两个变量收:
a,b = {"a","b"} # 由于集合无序性
a,b = {"a":1,"b":2} #赋值的是字典的键
print(a,b)

#遍历登场的二级容器
lst = [("2","王思聪","王钢弹"),["马云","马化腾","马伊琍"],("王宝强","马蓉","宋小宝")]
#方法一
for i in lst:
	print(i)
	for j in i:
		print(j)

#方法二
for a,b,c in lst:
	print(a,b,c)
# a,b,c = ["马云","马化腾","马伊琍"],

#遍历不等长的二级容器
lst = [("2","王思聪","王钢弹"),["马云","马化腾"],("王宝强",)]
for i in lst:
	for j in i:
		print(j)


# range 对象
"""
range(开始值,结束值,步长)
start:开始值
end:结束值
step:步长

最大值end 取不到的,取到end这个数之前的那个值
"""

res = range(10)
print(res)

# range 当中只有一个值
for i in range(10):
	print(i)

# range 当中二个值的情况
for i in range(5,11):
	print(i)

# range 当中三个值的情况
for i in range(1,15,2):
#1,3,5,7,9,11,13
 	print(i)

for i in range (9,0,-1):
	print(i)

#range(一个数),相当于创建了一个元组,从0开始叠加,与列表,元组的正向索引特点有关


# 99乘法表 for 改写
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i,j,i*j),end = '')
		j += 1
	print()
	i += 1

for i in range(1,10):
	for j in range(1,i + 1):
		print("%d*%d=%2d " % (i,j,i*j),end = '')
	print()


'''
#总结:
while 一般用于复杂的逻辑操作

for 一般用于数据的遍历
'''