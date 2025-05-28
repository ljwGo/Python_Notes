# ### 闭包函数的特点:
'''
内函数使用了外函数的变量,外函数把内函数返回return,奖盖变量与内函数发生绑定,延长生命周期



'''

def outer(varl):
	def inner(num):
		return var1 + num
	return inner
func = outer(10) # func = inner
res = func(5) # var1 + num = 15
print(res)

'''
代码解析:
outer(10) var1 = 10
func = inner
func(5) num = 5
return var + num => return 10 + 5 => 15
print(res) => 15
'''

# ### 闭包的意义
# 模拟记录鼠标点击次数操作
# 方法一: 全局变量的作用范围太大,容易被串改
total = 0
def click():
	global total
	total += 1
click()

# 方法二:
'''闭包可以优先使用外函数中的变量,并对闭包中的值起到了封装保护的作用,外部无法访问'''
def myclick():
	x = 0
	def click():
		nonlocal x
		x += 1
		print(x)
	return click
func = myclick()
print(func)
func()
func()
func()
x = 100
func()







