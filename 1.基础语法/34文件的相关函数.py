# 刷新缓冲区 flush
	# 当文件关闭的时候自动刷新缓冲区
	# 当整个程序运行结束的时候自动刷新缓冲区
	# 当缓冲区写满了 会自动刷新缓冲区
	# 手动刷新整个缓冲区

'''
fp = open('ceshi7.txt',mode='w',encoding='utf-8')
fp.write('abc')
# 手动将缓冲区的内容刷新到文件
fp.flush()
while True:
	pass
# 文件会创建,但不会有内容
fp.close()
'''

# readline() 功能:读取一行文件内容
"""
with open('ceshi7.txt',mode='r+',encoding='utf-8') as fp:
	#读取一行
	#res = fp.readline()
	#print(res)
	#读取所有
	'''
	res = fp.readline()
	while res:
		print(res)
		# 再读取一行
			res = fp.readline() #操作实行的情况与光标位置有关
	'''

	# readline(字符的个数)
	'''
	参数值 小于当前总个数,按照当前字符进行读取
	参数值 大于当前总个数,按照当前行进行读取(不会跨行读取)
	'''
	res = fp.readline(1) #1指的是字符
	print(res)
"""

#readlines() 功能:将文件中的内容按照换行读取到列表当中
lst_new = []
with open('ceshi7.txt',mode='r+',encoding='utf-8') as fp:
	lst = fp.readlines() # 使用read()换行符\n也会被打印
	print(lst)
	# 利用循环把两边的空白符去掉
	for i in lst:
		# 将处理好的结果放到新列表中
		lst_new.append(i.strip('\n'))
print(lst_new)

# writelines()	功能: 将内容是字符串的可迭代型数据写入文件中 参数:内容为字符串类型的可迭代型数据
'''
1 字符串
2 可迭代型数据: (容器类型数据,迭代器,range对象)
'''

with open('ceshi8.txt',mode='w+',encoding='utf-8') as fp:
	lst = ['参数值\n','小于当前总个数\n','按照当前字符进行读取\n']
	# str = 'asdfghjkl'
	fp.writelines(lst)

#truncate()		功能: 把要截取的字符串提取出来,然后清空内容将提取的字符串重新写入文件中(字节)
with open('ceshi8.txt',mode='r+',encoding='utf-8') as fp:
	fp.truncate(14)

fp = open('ceshi9.txt',mode='w+',encoding='utf-8')
fp.writelines(['注意文件是否使用utf-8进行编译\n',
'是否使用utf-8进行解码'])
fp.seek(0)
#readable() 功能:判断文件对象是否可读
res = fp.readable()
print(res)
#writable() 功能:判断文件对象是否可写
res = fp.writable()
print(res)

# fp 是一个可迭代对象(文件的io对象)是一个可迭代对象
# 默认是一行一行读取
# 使用for 必须要求fp(文件io对象)可读取(r,或者+ 模式)
# for in 本身每遍历一次就有增加\n的功能

for i in fp:
	print(i)
fp.close()

'''
read() readline() 一般情况下都是字符[在字节流模式下,读取的是字节]
seek() truncate() 读取的是字节
'''
