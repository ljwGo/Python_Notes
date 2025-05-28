#1 有变量 name = 'aleX leNb' 完成如下操作
name = 'aleX leNb'
print(name)
res = name.strip()
print(res)

#(1)
name = 'aleX leNb'
# del name[:2] 字符串不能使用del
res = name[2:]
print(res)

res = name.lstrip('al')
print(res)

#(2)
res = name[:7]
print(res)

res = name.rstrip('Nb')
print(res)

#(3)
res = name[1:-1]
print(res)

res = name.lstrip('a').rstrip('b')
print(res)

res = name.strip('ab') #并不需要完全对应,有就删除
print(res)

#(4)
res = name.startswith('al')
print(res)

#(5)
res = name.endswith('Nb')
print(res)

#(6)
res = name.replace('l','p')
print(res,name)

#(7)
res = name.replace('l','p',1)
print(res)

#(8)
res = name.split('l')
print(res)

#(9)
res = name.split('l',1)
print(res)

#(10)
res = name.upper()
print(res,name)

#(11)
res = name.lower()
print(res)

#(12)
res = name.capitalize()
print(res)

#(13)
res = name.count('l')
print(res)

#(14)
res = name.count('l',0,4)
print(res)

#(15)
res = name.index('N')
print(res)

#(16)
res = name.find('N')
print(res)

#(17)
res = name.find('X le')
print(res)

#(18)
res = name[1]
print(res)

#(19)
res = name[:3]
print(res)

#(20)
res = name[-2:]
print(res)

#(21)
res = name.find('e')
print(res)

#利用循环把所有e的索引打印出来
'''
#错误写法,原因索引开始为0
res = 0
tem = 0
i = 0
while i < name.count('e'):
	tem = name[tem + 1:].find('e')
	res += tem
	print(res)
	i += 1
'''

print('<======>')
res = 0
x = -1
i = 0
while i < name.count('e'):
	x = name.find('e',x+1)
	print(x)
	i += 1
print('<======>')

#老师的方法
name = 'aleX leNb'
i = 0
while i<len(name):
	if name[i] == 'e':
		print(i)
	i+=1

x = 0
for i in name:
	if i == 'e':
		print(x)
	x += 1

name = 'aleX leNb'
for i in range(len(name)):
	pos = name.find('e',i,i+1)
	if pos != -1:
		print(pos)

'''
name = 'aleX leNb'
for i in name:
	if i == 'e':
		num = name.index(i)
		num2 = name.index(i,num+1)
		print(num)
		print(num2)
'''

#2
content = input('请输入计算式:')
diedai = content.split('+') # split 把字符串按一定值为间隔分割成列表
sum = 0
for i in diedai:
	sum += int(i)
print(sum)

name = 'aleX leNb'
a,b = content.split('+') # 变量的解包
res = int(a) + int(b)
print(res)

#4
'''非纯数字组成的字符串强转为整型会报错：ValueError: invalid literal for int() with base 10'''
content = input('请输入内容:')
sum = 0
for i in content:
	if i.isdigit():  #isdecimal
	#if type(int(i)) == 'int':
		sum += 1
print(sum)

#5
while True:
	neirong = input('请输入内容:')
	if '小粉粉' in neirong or '大铁锤' in neirong:
		print('存在敏感字符请从新输入')
	else:
		break
'''
lst = ['小粉粉','大铁锤']
while True:
	sign = False
	neirong = input('请输入内容:')
	#判断是否又敏感词汇
	for i in lst:
		if i in neirong:
			#有一个敏感词汇,就直接终止里层循环,让用户重新输入
			sign = True
			print('存在敏感字符请从新输入')
			break

	#根据sign来打印内容
	if sign == True:
		print('有敏感词汇')
	else:
		print('这个词可以使用')
'''

name = input('请输入你的名字:')
address = input('请输入你的地址:')
hobby = input('请输入你的爱好:	')

print('敬爱可亲的{},最喜欢在{}做{}'.format(name,address,hobby))

#6
s1 ='123a4b5c'
res = sl[:3]





