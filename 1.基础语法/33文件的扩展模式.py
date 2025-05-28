# ### 文件的扩展模式 +
# (utf-8编码格式下 默认一个中文三个字节 一个英文或符号 占用一个字节)
	#read()		功能:读取字符的个数(里面的参数代表字符个数)
	#seek()		功能:调整指针的位置(里面的参数代表字节个数)
		# seek(0)	 把文件指针移动到行首
		# seek(0,2)  把文件指针移动到末尾
	#tell()		功能:当前光标左侧所有的字节数(返回字节数)

# r+ 先读后写
'''
fp = open('ceshi3.txt',mode='r+',encoding='utf-8')
res = fp.read()
print(res)

fp.write('123')
#重新读取
fp.seek(0)
res = fp.read()
print(res)
fp.close()
# 文件指针,操作由光标开始向右实行操作
'''

# r+ 先读后写
fp = open('ceshi3.txt',mode='r+',encoding='utf-8')
fp.seek(0,2)
fp.write('123')
#从新调整光标位置,移动到开头
fp.seek(0)
res = fp.read()
print(res)
fp.close()

# w+ 可写可读
fp = open('ceshi4.txt',mode='w+',encoding='utf-8')
fp.write('色即是空,空即是色,受想行识,亦复如是')
fp.seek(0)
res = fp.read()
print(res)
fp.close()

# a+ 可读可写[a模式下,在追加内容时,会强制把光标移动到末尾进行写入]
'''
fp = open('ceshi5.txt',mode='a+',encoding='utf-8')
fp.write('无眼耳鼻舌身意')
fp.seek(0)
res = fp.read()
print(res)
fp.close()
'''

# read seek tell 三个方法的使用
'''
fp = open('ceshi5.txt',mode='r+',encoding='utf-8')
res = fp.read(3) # 字符数
print(res)
# 当前光标左侧所有的字节数
res = fp.tell()
print(res)
fp.seek(4) # 字节数
res = fp.tell()
print(res)
fp.close()
'''
# 注意点: 如果是中文字符串,移动seek时候,如果移动到一半,读取时会发生报错;
fp = open('ceshi5.txt',mode='r+',encoding='gbk') # 使用utf-8编码集时会报错,原因可能是这些汉字字符没有对应的utf-8二进制数据
res = fp.read(2)
print(res)
res = fp.tell()
print(res)
fp.close()

#一个中文3个字节,但是移动了2个,会出现报错
'''
res = fp.seek(2)
res = fp.read()
print(res)
fp.close()
'''

# with 语法 : 可以自动实现关闭文件操作
'''
语法: with open('ceshi5.txt',mode='r+',encoding='utf-8') as fp:
	逻辑
'''
with open('ceshi5.txt',mode='r+',encoding='gbk') as fp:
	res = fp.read()
	print(res)

# 改写复制图片操作
with open('集合的交并补.png',mode='rb') as fp1 , open('集合3.png',mode='wb') as fp2:
	# 读取内容
	str_bytes = fp1.read()
	# 写入内容
	fp2.write(str_bytes)