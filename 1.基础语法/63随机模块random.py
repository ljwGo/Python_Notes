# ### 随机模块 random
import random
# random() 随机获取0~1中的小数(左闭右开)
res = random.random()
print(res)

# randrange() 随机获取指定范围内的整数(包含开始值,不包含结束值,间隔值)
res = random.randrange(1,17,4)
print(res)

# randint() 随机产生指定范围内的随机整数(了解)
res = random.randint(2,6) # 会返回结束值
print(res)

# uniform() 获取指定范围内的随机小数(左闭右开)
# 1 <= x < 3
res = random.uniform(1,3)
print(res)

# 参数可以反着写,但是不推荐
res = random.uniform(1,-2)
print(res)
# return a + (b-a) * self.random()

# choice() 随机获取序列中的值(多选一)
lst = ['李德亮','王文','李明辉','周杰伦','郭福正']
res = random.choice(lst)
print(res)

def func(lstvar):
	lth = len(lstvar)
	res = lstvar[random.randrange(lth)]
	return res
print(func(lst))

# sample() 随机获取序列中的值(多选多) [返回列表]
res = random.sample(lst,2)
print(res)

# shuffle() 随机打乱序列中的值(直接打乱原序列)
lst = [1,2,3,4]
res = random.shuffle(lst)
print(res) # None 返回值没有意义
print(lst)

# 随机验证码
def func():
	strvar = ''
	for i in range(4):
		# a~z
		sm_char = chr(random.randrange(97,123))
		# A~Z
		bg_char = chr(random.randrange(65,91))
		# 0~9
		num = str(random.randrange(10))
		# 把可能的字符元素塞到列表
		lst = [sm_char,bg_char,num]
		# 通过choice抽取其中的元素
		strvar += random.choice(lst)
	return strvar
res = func()
print(res)












