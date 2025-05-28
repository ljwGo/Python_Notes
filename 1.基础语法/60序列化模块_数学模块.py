# ### pickle 序列化模块
'''
序列化: 把不能够直接存储到文件的数据变得可存储,这个过程就是序列化
反序列化: 把存储的数据拿出来,恢复成原来的数据类型,这个过程就是序列化

php: (了解)
	serialize 序列化
	unserialize 反序列化

pickle 可以序列化所有数据类型
'''

import pickle
# 文件当中,只能存储字符串 或者 二进制字节流,其他不行
'''
lst = [1,2,3,4,5]
with open('ceshi.txt',mode='r+',encoding='utf-8') as fp:
	fp.write(lst)
'''

lst = [1,2,3,4,5]
# dumps 把任意对象序列化成一个bytes
res = pickle.dumps(lst)
print(res)

#loads 把任意bytes反序列化成原来的数据
lst = pickle.loads(res)
print(lst,type(lst))

def func():
	print('我是函数func')
res = pickle.dumps(func)
print(res)
func = pickle.loads(res)
print(func,type(func))

it = iter(range(6))
# 序列化迭代器
res = pickle.dumps(it)
# 反序列化恢复成原来的数据
it2 = pickle.loads(res)
print(it2)
from collections.abc import Iterable,Iterator
res = isinstance(it2,Iterable)
print(res)

# dump 把对象序列化后写入到file-like Object(即文件对象)
lst = [1,2,3]
with open('ceshi.txt',mode='wb') as fp:
	pickle.dump(lst,fp)

with open('ceshi.txt',mode='rb') as fp:
	lst = pickle.load(fp)
	print(lst)

# ### math 数学模块
import math
# ceil()	向上取整操作 (对比内置round) ceil意思是天花板
res = math.ceil(4.3)
print(res)

# floor()	向下取整操作
res = math.floor(5.6777765)
print(res)

# pow() 计算一个数值的N次方(结果为浮点数) math模块pow方法只有两个参数

# sqrt() 开平方运算(结果浮点数)
res = math.sqrt(9)
print(res)

# fabs() 计算一个数值的绝对值(结果浮点数)
res = math.fabs(-8)
print(res)

# modf() 将一个数值拆分为整数和小数两部分组成元组
res = math.modf(7.81)
print(res)

# copysign() 将参数第二个数值的正负号拷贝给第一个(返回一个小数)
res = math.copysign(-18,10)
print(res)

# fsum() 将一个容器类型数据中的数据进行求和运算 (结果浮点数)
lst = [1,2,3,4,5,6,7]
res = math.fsum(lst)
print(res)

# 圆周率常数 ip







