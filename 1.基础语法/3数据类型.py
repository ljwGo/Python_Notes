### 数据类型分类:
# Number 数据类型(int float bool complex)
# int 整形(正整形 0  副整形)


intvar = 89
# int 整形 var 变量
print(intvar)

# tpye 函数 可以获取一个变量的类型
res = type(intvar)
print(res)

# id 可以获得一个变量对应值的地址(不是真正的地址)
res = id(intvar)
print(res)

# 十六进制整形
intvar = 0xff
print(intvar)
# 获取类型
print( type(intvar))
# 获取地址
print( id(intvar))

# 八进制整形
intvar = 0o124

# 二进制整形
intvar = 0b101
print(intvar)
print( type(intvar))
print( id(intvar))



# float 浮点型 小数
# 表达方式一
floatvar = 5.73
print(floatvar)
print( type(floatvar))
print( id(floatvar))

# 表达方式二
floatvar = 5.78e4
# e是乘以10的意思,e后面的4指的是10的幂
print(floatvar)
# 输出的是57800
print( type(floatvar))
print( id(floatvar))


# bool 布尔型 Ture 真的 False 假的(首字母必须是大写)
boolvar = True
print(type(boolvar))
print(id(boolvar))

# complex 复数类型
'''实数 +  虚数 组成的
3 + 4j
3  =>实数
4  =>虚数
j:如过一个数的平方等于-1,那么这个数就叫做虚数单位
'''

# 表达方式一
complexvar = 3 +4j
print(complexvar)
print(type(complexvar))
print( id(complexvar))

# 表达方式二
'''
complex(实数,虚数)
'''
complexvar = complex(3,4)
print(complexvar)


'''
str 字符串类型
list 列表类型
tuple 元组类型
set 集合类型
dict 字典类型
'''