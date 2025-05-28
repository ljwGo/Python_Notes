# 1
'''
with open('a1.txt',mode='w',encoding='utf-8') as fp:
	lst = ['老男孩是最好的学校\n','全心全意为学生服务\n','只为学生未来,不为牟利\n','我说的都是真的']
	fp.writelines(lst)
'''

'''
fp = open('a1.txt',mode='r',encoding='utf-8')
res = fp.read()
print(res)
fp.close()
'''

'''
fp = open('a1.txt',mode='a+',encoding='utf-8')
fp.write('\n信不信由你,反正我是信了')
fp.close()
'''

'''
with open('a1.txt',mode='r+',encoding='utf-8') as fp:
	res = fp.read()
	print(res)
	fp.write('\n信不信由你,反正我是信了')
'''

"""
strvar = '''
每天坚持一点,
每天努力一点,
每天多思考一点,
慢慢你会发现,
你的进步越来越大
'''
with open('a1.txt',mode='w+',encoding='utf-8') as fp:
	fp.write(strvar)
"""

'''
with open('a1.txt',mode='r+',encoding='utf-8') as fp:
	res = fp.read()
	print(res)
	fp.seek(0)
	lst = fp.readlines()
	print(lst)
	lst.insert(3,'你信就好\n')

with open('a2.txt',mode='w+',encoding='utf-8') as fp:
	fp.writelines(lst)

# 简写
with open('a1.txt',mode='r+',encoding='utf-8') as fp1,open('a2.txt',mode='w+',encoding='utf-8') as fp2:
	lst = fp1.readlines()
	lst.insert(3,'你信就好\n')
	fp2.writelines(lst)
'''

'''
with open('t1.txt',mode='w+',encoding='utf-8') as fp:
	lst = ['葫芦娃,葫芦娃\n','一个藤上七朵花\n','风吹雨打都不怕\n','啦啦啦啦啦\n','我可以算命,\n']
	fp.writelines(lst)
'''

# 第二题
'''
with open('t1.txt',mode='r+',encoding='utf)-8') as fp:
	res1 = fp.readable()
	res2 = fp.writable()
	print(res1,res2)

with open('t1.txt',mode='r',encoding='utf)-8') as fp:
	for i in fp:
		print(i) #一行一行读取

with open('t1.txt',mode='r',encoding='utf)-8') as fp:
	res = fp.readlines()
	print(res)
	for i in res:
		print(i)

with open('t1.txt',mode='r+',encoding='utf)-8') as fp
	res = fp.read(4)
	print(res)

with open('t1.txt',mode='r',encoding='utf)-8') as fp:
	res = fp.readline()
	print(res)
	res_new = res.strip()
	print(res_new)

with open('t1.txt',mode='r',encoding='utf-8') as fp:
	lst = fp.readlines()
	total = ''
	for i in lst[2:]:
		total += i
print(total)

with open('t1.txt',mode='a+',encoding='utf-8') as fp:
	fp.write('老男孩教育')
	fp.seek()
	res = fp.read()
	print(res)

with open('t1.txt',mode='r+',encoding='utf-8') as fp:
	fp.turncate(24)
'''

#第三题

lst2 = []
total = 0
with open('a.txt',mode='r+',encoding='utf_8') as fp:
	lst = fp.readlines()
	#print(lst)
	for i in lst:
		# 重置新字典
		dic = {}
		# print(i.strip())
		# 先去掉两边的空白符,再按照空格进行分割,形成一个列表,
		# 里面的元素是字符串
		n,p,s  = i.strip().split()
		# 把数据塞进新字典中
		dic['name'] = n
		dic['price'] = p
		dic['sum'] = s
		lst2.append(dic)
		total += int(p) * int(s)
print(lst2)
print(total)
		#print('name:' + n,'price:' + p,'sum:' + s)


strvar = 'k:1/k1:2/k2:3/k3:4'
dic = {}
lst = strvar.split('/')
for i in lst:
	k,v = i.split(':')
	dic[k] = v
print(dic)

print('<======>')
li = [11,22,33,44,55,66,77,88,99,90]
lst1 = []
lst2 = []
dic = {}
for i in li:
	if i < 66:
		lst1.append(i)
	elif i > 66:
		lst2.append(i)
dic['k1'] = lst1
dic['k2'] = lst2
print(dic)

li = [11,22,33,44,55,66,77,88,99,90]
dic = {'k1':[],'k2':[]}
for i in li:
	if i > 66:
		dic['k1'].append(i)
	elif i < 66:
		dic['k2'].append(i)
print(dic)
