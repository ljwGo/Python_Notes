# 接受用户的输入
# 在Python3: input会将用户输入的所有内容都存成字符串类型
username = input("请输入您的账号:")
print(username, type(username))
age = input('请输入您的年龄:')
age = int(age)
print(age > 16)

# 在python2中:
# raw_input():用户与python3的input一模一样
# input():要求用户必须输入一个明确的数据类型，输入的是什么类型，就存成什么类型

# 2、格式化输出
# 字符串类型
# 值按照位置与%s一一对应，少一个不行，多一个也不行
print("my name is %s my age is %s" % ('egon', '18'))
res = "我的名字是 %(name)s 我的年龄是 %(age)s" % {'name': 'egon','age': '18'}
# %s能接受所有类型，%d只能接受int类型

# 2.2 str.format:兼容性好(效率其次)
res = '我的名字是{}我的年龄是{}'.format('egon',18)
res = '我的名字是{0}{0}{0}我的年龄是{1}'.format('egon',18)
res2 = "开始执行:{x:=<15}".format(x='你好')
print(res2)
# 四舍五入
'{salary:.3f}'.format(salary=1231.161616) # 精确到小数后三位
res = '我的名字是{name}我的年龄是{age}'.format(name='egon',age=18)
print(res)

# 3.5 f python3.5以后才推出(效率最快)
x = input("your name:")
y = input("your age:")
res = f'my name is {x},my age is{y}'
