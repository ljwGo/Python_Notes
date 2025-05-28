# ### 主动抛出异常 raise
'''
所有异常类的父亲 BaseException
所有普通异常类的父亲 Exception

raise + 异常类/异常类的对象
'''
# 1 基本语法
try:
	raise BaseException
except BaseException:
	pass

# 简写
'''raise 后面如果什么也不写,默认抛出的是BaseException'''
try:
	raise
except:
	pass

# 2 自定义异常类(必须继承BaseException类)
class MyException(BaseException):
	def __init__(self,num,msg,file,fileline):
		self.num = num
		self.msg = msg
		self.file = file
		self.fileline = fileline

# get_info 通过抛出异常触发return_errorinfo函数,从而获取异常的行号和文件
def get_info(n):
	try:
		raise
	except:
		return return_errorinfo(n)

sex = '中性'
try:
	if sex == '中性':
		raise MyException(122,'人类没有中性的',get_info(2),get_info(1))
except MyException as e:
	print(e)
	print('错误的号码是{}'.format(e.num))
	print('错误的原因是{}'.format(e.msg))
	print('错误的文件是{}'.format(e.file))
	print('错误的行号是{}'.format(e.fileline))





