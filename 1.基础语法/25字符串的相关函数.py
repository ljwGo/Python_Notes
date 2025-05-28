# ### 字符串的相关函数

# * capitalize 字符串首字母大写
strvar = 'happy new year'
res = strvar.capitalize()
print(res)
'''capitalize capitalize capitalize'''

# * title 每个单词的首字母大写(非字母隔开)

# * upper 将所有字母变成大写

# * lower 将所有字母变成小写

# * swapcase 大小写互换

# * len 计算字符串的长度
strvar = 'abcd123'
print(len(strvar))

# * count 统计字符串中某个元素的数量
strvar = '我爱你亲爱的老爸'
res = strvar.count('爱')
print(res)

# * find 查找某个字符串第一次出现的索引位置(查找的是字符串的首个字母)
'''find('要查找的字符串',开始位置,结束位置)'''
strvar = "oh Father this is my favorite toy"
res = strvar.find('or')
res = strvar.find('t',6,15)
# 如果返回的是-1,代表没找到
res = strvar.find("my",0,4)
print(res)

#index 与 find 功能相同 find找不到返回-1,index找不到数据直接报错

# startswith,endswith("字符串",开始索引,结束索引)
# * startswith 判断是否以某个字符或字符串为开头
strvar = "oh Father this is my favorite toy"
res = strvar.startswith('oh')
res = strvar.startswith('Father',3)
res = strvar.startswith('ther',5,16)
print(res)

# * endswith   判断是否一某个字符或字符串结尾
res = strvar.endswith('boy')
res = strvar.endswith('rite',-12,-4)	#明白结束索引最大值不能取,同时开始索引<结束索引
print(res)

# * isupper 判断字符串中的字母是否都是大写字母
strvar = 'XBOYWW'
res = strvar.isupper()
print(res)

# * islower 判断字符串中的字母是否都是小写字母
strvar = 'xboyww'
res = strvar.islower()
print(res)

# * isalpha 判断字符串是否由字母和文字组成
strvar = 'asdfg你好'
res = strvar.isalpha()
print(res)

# * isdigit 检测字符串数是数字组成 接受二进制字节流
strvar = '123456'
res = strvar.isdigit()
print(res)

'''
二进制字节流 : 用来把数据进行传输和存储
表达方式:b"字符串"(b => bytes)
里面的字符串 必须是ascii编码集
bytes bit
'''

res = b'123'
print(res,type(res))
res2 = res.isdigit()
print(res2)

# * isdecimal 检测字符串是否以数字组成 必须是纯数字
res = "2214"
res2 = res.isdecimal()
print(res2)


#重点记住
# split 按某字符串将字符串分割成  列表  (默认字符是空格)
strvar = 'you can you up no can no bb'
res = strvar.split()
strvar = 'you,can,you,up,no,can,no,bb'
#按照逗号进行分割
res = strvar.split(',')
print(res)
res = strvar.split(',',2)	#按,为标志,将字符串strvar分割两次
print(res)
res = strvar.rsplit(',',2)	#r => right(从右向左分割)
print(res)

# join 按某字符将列表拼接成字符串(任何容器类型都可)
listvar = ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
res = ' '.join(listvar)
print(res)

# * center 填充字符串,原字符串居中(默认填充空格)
strvar = '刘德华'
strnew = strvar.center(10) # 10 是字符串的总长度 = 原字符串长度 + 填充字符串长度
strnew = strvar.center(10,'@')
print(strnew)

# * strip 默认去掉首尾两边的空白符(\r \n \t 空格)
strvar = '             神秘男孩      '
res = strvar.strip()
print(res)
strvar = '@@@1223@@@@'
res = strvar.strip('@')
print(res)

# * replace()
'''
功能 : 把字符串的旧字符换成新字符
格式 : 字符串,replace('旧字符','新字符'[,限制替换的次数] # 可选项)
返回值 : 替换之后的字符串
'''

strvar = '可爱的小狗喜欢吃肉,是不是,是不是,是还是不是'
res = strvar.replace('是不是','真不是')
print(res)
#可以选择替换的次数
res = strvar.replace('是不是','真不是',1)
print(res)



