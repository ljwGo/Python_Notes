# ### json
'''
所有编程语言都能识别的数据格式叫做json,是字符串

json:将数据类型序列化成字符串
pickle:将数据类型序列化成字节流

json能够转换的数据类型:
	int float bool str list tuple dict None
'''
# ### 1 json基本语法
import json
'''dumps 和 loads 是一对,用来序列化和反序列化数据的
ensure_ascii = False: 显示中文
sort_keys = True: 对字典的键进行排序
'''
# dumps 把任意对象序列化成一个字符串
dic = {'name':'长远','age':20,'sex':'男性','family':['爸爸','妈妈','妹妹']}
res = json.dumps(dic)
print(res)

# loads	把任意字符串反序列化为原来的数据
dic = json.loads(res)
print(dic,type(dic))

'''dump 和 load 是一对,根据文件进行操作存储'''
with open('ceshi1.json',mode='w',encoding='utf-8') as fp:
	json.dump(dic,fp)

with open('ceshi1.json',mode='r',encoding='utf-8') as fp:
	dic = json.load(fp)

# ### json 与 pickle 之间的区别
# json
'''
json可以连续dump,但是不能连续load
'''
dic1 = [1,2,3,4,5,6]
dic2 = ['qfq','fqfq','fafga']
with open('ceshi2.txt',mode='w',encoding='utf-8') as fp:
	json.dump(dic1,fp)
	fp.write('\n')
	json.dump(dic2,fp)

'''
# 不能够把两个字典都识别出来
with open('ceshi2.txt',mode='r',encoding='utf-8') as fp:
	res = json.load(fp)
	print(res)
'''

# loads 方法来识别出每一个字典
from collections.abc import Iterator
res = isinstance(fp,Iterator)
print(res)

with open('ceshi2.txt',mode='r+',encoding='utf-8') as fp:
	for i in fp:
		# print(i,type(i))
		dic = json.loads(i)
		print(dic,type(dic))

# pickle
'''
可以连续dump,也可以连续load
pickle在插入数据时,在数据末尾写了结束的标志符,所以可以识别各个数据

'''
import pickle
with open('ceshi3.txt',mode='wb') as fp:
	pickle.dump(dic1,fp)
	pickle.dump(dic2,fp)

# 可以连续load
print('<======>')
with open('ceshi3.txt',mode='rb') as fp:
	res = pickle.load(fp)
	print(res,type(res))
	try:
		while True:
			dic = pickle.load(fp)
			print(dic)
	except:
		pass
'''
try ... except ...
try:
	把有问题的代码写到try代码块中
except:
	如果发生了报错,直接执行except这个代码块
'''



