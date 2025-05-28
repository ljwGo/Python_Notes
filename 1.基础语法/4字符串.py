### 字符串:用引号引起来的就是字符串 引号:单引号 双引号 三引号

# str容器类型的一个 1单引号
strvar = '今天是Python自学第五天'
print(strvar)
print(type(strvar))

# 2双引号
strvar = "衣带渐宽终不悔,为伊消得人憔悴."
print(strvar)

'''
转义字符:\ + 字符
    1把有意义的字符变得无意义
    2将无意义的字符变得有意义

以下属于第一
\n,\r\n: 都代表换行的意思
\r:把\r后面所有的字符串拉到当前行首
\t:一个缩进
'''

strvar = "衣带渐宽终不悔,\n为伊消得人憔悴."
strvar = "衣带渐宽终不悔,\r为伊消得人憔悴."
strvar = "衣带渐宽\n终不悔,为伊消\r得人憔悴."
strvar = "衣带渐宽\r终不悔,为伊消\n得人憔悴."
strvar = "衣带渐宽\t终不悔,为伊消得人憔悴."
print(strvar)
print( type(strvar))

# 以下属于第二
# strvar = "衣带"渐"宽终不悔,为伊消得人憔悴."   错误表示
# 两种方法
strvar = "衣带'渐'宽终不悔,为伊消得人憔悴."
strvar = "衣带\"渐\"宽终不悔,为伊消得人憔悴."
print(strvar)

#3 三引号
strvar ='''
云穷千里目,
更上一层楼
'''
strvar ="""
云'穷'千"里"目,
更上一层楼
"""
print(strvar)
print( type(strvar))


# 元字符串:在字符串的开头加上r
'''不进行转义,原型化输出内容'''
strvar = "D:\ph\es\ns"       # 其中的\n有歧义
print(strvar)
strvar = r"D:\ph\es\ns"
print(strvar)


# 5字符串的格式化
"""
语法:
    "字符串" % (值1,值2)

占位符:
    %d 整形占位符
    %f 浮点占位符
    %s 字符串占位符
"""

# %d 整点占位符
strvar = "我今天很帅,因为我昨天买了%d个apple"%(2)
print(strvar)
# %2d 占用两位,原字符居右
strvar = "我今天很帅,因为我昨天买了%2d个apple"%(3)
print(strvar)
# %-2d
strvar = "我今天很帅,因为我昨天买了%-2d个apple"%(3)
print(strvar)

# %f 浮点型占位符 默认小数保留6位
strvar = "我昨天领工资了,一共领了%f元" % (4.5e4)
print(strvar)
# %.2f 小数点保留两位
strvar = "我昨天领工资了,一共领了%.3f元" % (4.5e4)
print(strvar)

# %s 字符串占位符
strvar = "%s" %("中奖号码为230597")
print(strvar)

# 在不确定类型的情况下,统一用%s,这里会强制转化成字符串类型:
strvar = "小李花了%.1f$买了%s个苹果" % (2.02,2)
print(strvar)
