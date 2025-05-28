# ### sorted
'''
sorted(iterable,key=函数,reverse=False)
功能:排序
参数:
	iterable(容器类型数据,range对象,迭代器)
	key = 函数 自定义 或者 内置函数
	reverse = False 从小到大排序 reverse = True 从大到小排序
返回值:
	排序后的结果
'''

# 默认从小到大排序
tup = (1,23,424,-24)
lst = sorted(tup)
print(lst)

# 从大到小排序
tup = (1,23,424,-24)
lst = sorted(tup,reverse = True)
print(lst)

# 使用绝对值进行排序
tup = (1,23,424,-24)
lst = sorted(tup,key=abs)
print(lst)

# 4 使用自定义的函数进行排序(按照余数大小排序)
tup = (1,23,424,-24,55)
def func(n):
	return n % 10
lst = sorted(tup,key=func)
print(lst)

# 字符串排序
strvar = 'zfacd'
lst = sorted(strvar)
print(lst)

# 集合排序
setvar = {'z','f','a','c','d'}
lst = sorted(setvar)
print(lst)

'''
总结:
	sort 只能针对列表进行排序,直接修改原有列表
	sorted 容器类型数据都可以排序,产生一个新的副本,数据类型是列表


'''






