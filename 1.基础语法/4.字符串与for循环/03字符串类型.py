# 1、作用
# 2、定义
# msg='hello' # msg=str('hello')
# print(msg, type(msg))

# 3、类型转换
# str可以把任意类型转换成字符串
# res = str({1:'www',2:'wfaw'})
# print(res, type(res))

# 4、使用：内置方法
# 4.1优先掌握
# 按索引取值（正向取+反向取）：只能取
# msg = 'hello world'
# 正向取
# print(msg[5])
# 反向取
# print(msg[-1])
# 只能取，不能改
# msg[0] = 'H'

# 4.1.2、切片：索引的拓展应用，从一个大字符串中拷贝出一个子字符串（顾头不顾尾，步长）re
# res = msg[0:6]
# print(res)
# res = msg[0:7:2]
# print(res)

# 反向步长(了解)
# res = msg[5:0:-1]
# res = msg[::] # 把字符串完整拷贝一份
# res = msg[::-1] # 把字符串倒过来拷贝一份
# print(res)

# 4.1.3、 长度len
# msg='hello world'
# print(len(msg))

# 4.1.4、 成员运算符 in、not in

# 4.1.5、移除字符串左右两侧的符号strip
# msg = '   egon    '
# res = msg.strip() # 默认去掉空格
# print(res)

# msg = '*****gw***jag******' # strip只去两边，不去中间
# res = msg.strip('*')
# print(res)

# msg = '**/**-=-=*egon**//**-=-=**'
# res = msg.strip('*-=/')
# print(res)

# 4.1.6、切分split：把一个字符串按照某种分隔符进行切分，返回一个列表
# # 默认分隔符是空格
# info = 'egon 18 male'
# res = info.split()
# print(res)

# 指定分隔次数（了解）
# res = info.split(':', 2)
# print(res)

# 需要掌握
# strip,lstrip,rstrip
# lower,upper
# startswith(''),endswith('')
# format的三种玩法
# split,rsplit（从右往左分隔字符串）
# join：把列表拼接成字符串
# l = ['egon', '18', 'male'] # 拼接的列表必须全为字符串类型
# res = ':'.join(l) # 以:作为拼接的符号将列表的每一项拼接成一个大字符串
# replace
# msg = 'you can you up no can no bb'
# print(msg.replace('you', 'YOU', 2))
# isalnum 判断字符串是否仅由字母和数字组成
# isalpha 判断字符串是否仅由字母组成
# isdigit 判断字符串是否由纯数字组成
# age = input('请输入您的年龄：').strip()
# if age.isdigit():
#     age = int(age)
#     if age > 18:
#         print('猜大了')
#     elif age < 18:
#         print('猜小了')
#     else:
#         print('猜对了')
# else:
#     print('您输入的年龄不全为数字')

# 4.3了解
msg = 'hello egon world'
# 返回要查找的字符串在大字符串中的起始索引值
print(msg.find('egon')) # 找不到时返回-1
print(msg.index('egon')) # 找不到是直接报错

# 4.3.2、center，ljust，rjust，zfill
print('egon'.center(50, '*')) # 居中填充
print('egon'.rjust(50, '*')) # 居右填充
print('egon'.ljust(50, '*')) # 居左填充
print('egon'.zfill(50)) # 使用0进行填充

# 4.3.4、captalize（字符串开头大写），swapcase（大小写反转），title（字符串中每一个单词首字母大写）

# 4.3.5、is数字系列
# islower
# isupper

num1 = b'4' # bytes
num2 = u'4' # unicode，pyhon3中无需加u就是unicode
num3 = '四' # 中文数字
num4 = 'Ⅳ' # 罗马数字
# isdigit只能识别num1、num2
# isnumberic可以识别num2、num3、num4
# isdecimal只能识别num2