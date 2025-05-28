# ### 单循环练习

#打印,一行十个小星星
'''help 查看帮助文档'''
help(print)
print(111),print(222)
print("*",end="")   #代码中表示间隔不能用空格,而是 ,

i = 0
while i < 10:
	print("*",end="")
	i += 1

# 2 用一个变量打印出一行十个小星星
strvar = "**********"
print(strvar)

'''
# 拼接字符串:+
var1 = "我爱你"
var2 = "亲爱的菇凉"
res = var1 + var2
print(res)

var1 = "我爱你"
var1 += "亲爱的祖国"
'''

i = 0
var = ""
while i < 10:
	var += "*"
	i += 1
print(var)

# 3 打印一行十个小星星,奇数个打印* 偶数个打印+
i = 1
while i <= 10:
	if i % 2 == 1:
		print("*",end='')
	else:
		print("+",end='')
	i += 1

print('')
i = 0
strvar = ''
while i < 10:
	if i % 2 == 0:
		strvar += '*'
	else:
		strvar += '+'
	i += 1
print(strvar)

# 4 一个循环,打印十行十列小星星
i = 0
while i < 100:
	if i % 10 == 9:
		print('*')
	else:
		print('*',end='')
	i += 1

i = 0
while i < 100:
	print('*',end='')
	if i % 10 == 9:
		print()
	i += 1

'''
0 % 2 == 0
1 % 2 == 1
2 % 2 == 0
3 % 2 == 1

0 % 3 == 0
1 % 3 == 1
2 % 3 == 2
3 % 3 == 0

任意数和n进行取余,余数的范围都是0 ~ n-1

'''

#5 一个循环,打印十行十列隔列变色的小星星
'''i 可以视为循环进行次数限制;可以利用i的不同值做分支条件的处理'''
i = 0
strvar = ''
while i < 100:
	if i % 2 == 0:
		strvar += '*'
	else:
		strvar += '+'
	if i % 10 == 9:
		strvar += "\n"
	i += 1
print(strvar)

#符号(站位,换位)只能作用在字符串中

i = 0
while i < 100:
	if i % 2 == 0:
		print("*",end='')
	else:
		print("+",end='')
	if i % 10 == 9:
		print()
	i += 1

# 6 一个循环,打印十行十列隔行变色的小星星
print('<===========>')
i = 0
while i < 100:
	if i % 20 <= 9:
		print('*',end='')
	else:
		print('+',end='')
	if i % 10 == 9:
		print()
	i += 1

'''
任意数和n进行地板除,会出现n个相同的数字
0//3 0
1//3 0
2//3 0
3//3 1
...
'''

i = 0
strvar = ''
while i < 100:
	if i // 10 % 2 == 0:
		strvar += "*"
	else:
		strvar += "+"
	if i % 10 == 9:
		strvar += "\n"
	i += 1
print('<===========>')
print(strvar)

'''一定要注意格式中的i += 1,避免死循环'''
#格式
'''
i = 0
while 条件表达式:
	执行的代码
	
	i += 1
'''
