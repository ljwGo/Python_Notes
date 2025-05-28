# ### 默认形参 和 关键字实参
def wangzhe  (top='长远',middle='周永林',bottom='主进程',jungle='林明辉',support='李诗韵'):
	print('上路选手:{who}'.format(who=top))
	print('中路选手:{who}'.format(who=middle))
	print('下路选手:{who}'.format(who=jungle))

# 调用函数
# wangzhe()
'关键字实参在函数的调用处'
wangzhe(middle='张三',top='李四')

# ### 收集参数
'''
收集参数:
	1 普通收集参数(专门用来收集那些多余的,没人要的普通实参)
	# 语法:
	def func(*args):
		code1...
	args => arguments


'''

'''
def func(a,b,c,*args):
	print(a,b,c)
	print(args)

func(1,2,3,4,5,6,7)
'''

# 计算人一个数的累加和
def func(*args):
	#print(args)
	total = 0
	for i in args:
		total += i
	print(total)

func(1,2,3,4,5,6,7)

'''
2 关键字收集参数
	# 语法:
	def func(**kwargs):
		code1...
	
	**keargs 是关键字收集参数 专门用来收集那些多余的,没人要的关键字实参
	kwargs => keyword arguments
'''

# 基本语法
def func(a,b,c,**kwargs):
	print(a,b,c)
	print(kwargs)

func(a=1,b=2,c=3,d=4,e=5)

# 任意字符串的拼接
'''
班长:黄乐喜
班花:李诗韵
吃瓜群众:李明辉,李德亮
'''

'''
def func(**kwargs):
	dic = {'monitor':'班长','classflower':'班花'}
	print(kwargs)
	for i in kwargs:
		if i in dic:
			print(dic[i] + ':' + kwargs[i])
		else:
			print(kwargs[i])
'''

def func(**kwargs):
	dic = {'monitor':'班长','classflower':'班花'}
	for k,v in kwargs.items():
		strvar = ''
		if k in dic:
			strvar += dic[k] + ':' + v
			print(strvar)
		else:
			print(v)

func(monitor='欢乐喜',classflower='李诗韵',eatmelon1='李敏慧',eatmelon2='李德亮')



