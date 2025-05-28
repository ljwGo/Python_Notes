# ### pass break continue

# pass 过 (当不能直接在代码块中写上具体代码时,先用pass占位;) 与 None 作用相似
num = 10
if num == 10:
	pass

i = 0
while i < 10:
	pass
	i += 1

# 其它语言,
'''
num = 10
if (num == 10){

}
'''

# break 终止当前循环,只能用在循环中
# 打印 1 ~ 10 ,遇到5就终止循环
# 单循环
i = 1
while i <= 10:
	print(i)
	if i == 5:
		break
	i += 1

# 多循环(终止当前循环)
i = 0
while i < 3 :
	j = 0
	while j < 3:
		if j == 2:
			break
		print(i,j)
		j += 1
	i += 1

# 不能在循环外使用break
"""
if 5 == 5:
	print(111)
	break
"""


# continue 跳过当前循环,从下一次开始
# 打印1 ~ 10 不包括5
i = 1
while i < 11:
	if i != 5:
		print(i)
	i += 1

# continue 极易造成死循环,要注意条件 i += 1

i = 1
while i <= 10:

	if i == 5:
		#手动加1
		i += 1
		continue
	print(i)
	i += 1


# 打印1~100 中所有不含有4的数字:
'''
i = 1
while i <= 100:
	if (i % 10 or i // 10) == 4:
		i += 1
		continue
	print(i)
	i += 1
'''

'''
// 地板除可以取一个数的高位
% 取余 可以取一个数的低位

任意数 // n 会产生 n 个相同的数字
任意数 % n 取值范围是0 到 n - 1
'''

#方法一
i = 1
while i <= 100:
	if i % 10 == 4 or i // 10 == 4:
		#手动加一,防止死循环
		i += 1
		continue
	print(i)
	i += 1

# 方法二 in dict 键
i = 1
while i <= 100:
	strvar = str(i)
	# print(strvar,type(strvar))
	if "4" in strvar:
		i += 1
		continue
	print(i)
	i += 1