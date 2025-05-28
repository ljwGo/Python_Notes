# 1
# 自己的方法
x = 66
i = 0
while i < 3:
	guess = int(input("请您输入一个数字"))
	if guess > x:
		print("您猜的数字大于该数字")
		i += 1
	elif guess < x:
		print("您猜的数字小于该数字")
		i += 1
	else:
		print('恭喜您猜对了')
		break
if i == 3:
	print('很遗憾,您没能猜出数字,请继续努力')

# 老师的方法
x = 66
i = 0
while i < 3:
	guess = int(input("请您输入一个数字"))
	if guess > x:
		print("您猜的数字大于该数字")
	elif guess < x:
		print("您猜的数字小于该数字")
	else:
		print('恭喜您猜对了')
		break
	if i == 2:
		print('很遗憾,您没能猜出数字,请继续努力')
	i += 1

# 2
# 使用while循环
s = 'asdfgh'
i = 0
while i < len(s):
	print(s[i])
	i += 1

# 使用for in循环
for i in s:
	print(i)

# (1)
for i in s:
	print(s)
# (2)
# 1
for i in s:
	print('%ssb' %  (i))
# 2
for i in s:
	print(i + 'sb')

# 3
#方法一
while True:
	choice = input('请输入你的选择(A,B,C)')
	if choice.upper() == 'A':
		print('你选择了走大路回家')
		choice2 = input('请你进一步选择步行还是公交车')
		if choice2 == '公交车':
			print('预计10分钟到家')
			break
		elif choice2 == '步行':
			print('预计20分钟到家')
			break
		else:
			print('没有该选项')
	elif choice == 'B':
		print('选择走小路回家')
		break
	elif choice == 'C':
		print('选择绕道回家')
		choice3 = input('去游乐厅玩还是网吧')
		if choice3 == '游戏厅':
			print('一个半小时到家,爸爸在家,拿棍等你')
		elif choice3 == '网吧':
			print('两个小时到家,妈妈已做好战斗准备')
		else:
			print('无该选项,请重新输入')
	else:
		print('请输入有效字符')

#方法二
'''sign = True
while sign:'''

# 4
i = 1
sum = 0
while i < 100:
	if i != 88:
		if i % 2 == 1:
			sum += i
		elif i % 2 == 0: #(else:)
			sum -= i
	i += 1
print(sum)

s = 0
for i in range(1,100):
	if i == 88:
		continue
	if i % 2 == 0:
		s -= i
	else:
		s += i
print(s)

#错误的尝试
'''
i = 1
while i <= 12:
	j = 1
	while i // 7 == 0:
		strvar = '*'*j
		print(strvar.center(11))
		j += 2
	j = 11
	while i // 7 == 1:
		strvar = '*' * j
		print(strvar.center(11))
		j -= 2
	i += 1
	print()
'''

#修正后我的方法
i = 1
while i <= 2:
	if i // 2 == 0:
		j = 1
		while j < 12:
			strvar = '*' * j
			print(strvar.center(11))
			j += 2
	else:
		j = 11
		while j > 0:
			strvar = '*' * j
			print(strvar.center(11))
			j -= 2
	i += 1

"""
     *     
    ***    
   *****   
  *******  
 ********* 
***********
***********
 ********* 
  *******  
   *****   
    ***    
     *     

     *     
    ***    
   *****   
  *******  
 ********* 
***********

图形: 空格 + 星星 + 换行 组成的一行元素
11 => 6
9 => 5
7 => 4
5 => 3
3 => 2
对于任意个星星n,一共多少行? hang = n // 2 + 1

1 => 5
2 => 4
3 => 3
4 => 2
5 => 1
对于当前行i,一共有多少个空格 kongge = 6 - i

1 => 1
2 => 3
3 => 5
4 => 7
5 => 9
6 => 11
对于当前的行i,一共有多少个星星 xingxing = i*2 - 1
"""

n = 11
hang = n // 2 + 1
i = 1
while i<=hang:
	#打印空格
	print(' '*(6-i),end='')
	#打印星星
	print('*'*(i*2-1),end='')
	#打印换行
	print()
	i+=1
# 下半部分

i = hang
while i > 0:
	print(' ' * (6 - i), end='')
	print('*' * (i * 2 - 1), end='')
	print()
	i-=1

# 方法二
# 上半部分
n = 11
hang = n // 2 + 1
i = 1
while i <= hang:
	# 打印空格
	# print(' '*(6-i),end='')
	kongge = 6 - i
	while kongge > 0:
		print(' ',end='')
		kongge -= 1
	#打印星星
	xingxing = 2*i - 1
	while xingxing > 0:
		print('*',end='')
		xingxing -= 1
	print()
	i += 1
# 下半部分
n = 11
hangshu = n // 2 +1
i = hangshu
while i > 0:
	kongge = hangshu - i
	while kongge > 0:
		print(' ',end = '')
		kongge -= 1
	xingxing = 2*i -1
	while xingxing > 0:
		print('*',end = '')
		xingxing -= 1
	print()
	i -= 1

