### 变量:可以改变的量就是变量,实际在内存是一块空间.
'''
linshi_205 = "赖建威"
print("lingshi")输出lingshi
print(lingshi)输出赖建威
'''

#变量的声明
a = 1
b = 2
print(a)
print(b)

#a,b在一行打印
a,b = 3,4
print(a,b)

a = b = 6
#变量从右到左读

#变量的命名
'''
字母数字下划线,首字不能为数字
严格区分大小写,不能使用关键字
变量命名有意义,不能使用中文字
'''


# import 导入 keyword 模块 [模块中有一个属性叫做 kwlist]
# 查看关键字
import keyword
res = keyword.kwlist
print(res)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''


"""
Python 支持中文命名变量,但是严禁使用 容易因为编码集出现乱码
utf-8 国际标准编码集(可变长的unicode编码集)如果是英文字母,字符.用一个字节存储,如果是一个中文,占用3个字节:
unicode 所有字符都占用4个字节,导致存储和存储影响速度和空间,所以出现了utf-8
gbk  国标编码  一个英文字母,符号占用一个字节,一个中文占用2个字节:
"""

中文 = 90
print(中文)

# 变量的交换
a = 100
b = 200
# Python特有的写法
'''
a,b= b,a
print(a,b)
'''
# 也可以通过临时变量存储
tmp = a
a = b
b = tmp
print(a,b)

#常量就是不可改变的量,python当中没有明确定义常量的关键字,所以约定俗成把变量名大写就是常量,表示不可改变
