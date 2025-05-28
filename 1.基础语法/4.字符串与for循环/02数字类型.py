# 一：int类型
# 1、作用：
# 2、定义：
age = 10 # age = int(10)

# 名字（参数）
print('hello', 'world')

# 2、类型转换
# 2、1把纯数字得字符串转换成int
res = int('100111')
print(res, type(res))

# 2、2（了解）
# 10进制 -> 二进制
# 11 -> 1011
print(bin(11)) # 0b1011

# 10进制 -> 八进制
print(oct(11)) # 0o13

# 10进制 -> 十六进制
print(hex(11)) # 0xb

# 2.2.2 其他进制转成十进制
# 二进制 -> 10进制
print(int('0b1011', 2))

# 八进制 -> 十进制
print(int('0o13', 8))

# 十六进制 -> 十进制
print(int('0xb', 16))

# 3、使用

# 二：float类型
# 1、作用
# 2、定义
salary = 3.1  # salary=float(3.1)
# 3、类型转换
res = float('3.1')
print(res, type(res))

# 4、使用
# int与float没有需要掌握的内置方法