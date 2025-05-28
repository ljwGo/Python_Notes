# ### 代码块
# 1 以冒号作为开始,用缩进来划分相同的作用域,整体是一个代码块
'''作用域:作用的范围'''
if 5 == 5:
    print(111)
    print(222)

if 5 == 6:
    print(333)
    print(444)
print(555)

# 注意点:具有相同的作用域 (之一缩进相同)

if 5 == 5:
    print(666)
    print(777)


# ### 流程控制
"""
流程:代码执行的过程
流程控制的三大结构:
    1顺序结构 : 默认代码从上到下依次执行
    2分支结构 : 四种
    3循环结构 : for ... in / while

分支结构:
    1单项分支
    2双向分支
    3多项分支
    4巢状分支
"""

# 单项分支
"""
if 条件表达式:
    code1
    code2
    code3
    ...
如果 条件表达式 成立,返回真 执行其中的代码块
"""

you = "狗"
if you == "狗":
    print("你好狗")

# 双向分支
"""
if 条件表达式:
    code1
    code2
    code3
    ...
else:
    code1
    code2
    code3
    ...

如果条件成立 执行if代码块
如果条件不成立 执行else代码块

if代码块 => 真区间
else代码块 => 假区间
"""

zhongzanlin = "屌丝"
if zhongzanlin == "高富帅":
    print("他将拥有跑车")
    print("他将拥有豪宅")
else:
    print("吃窝窝头")
    print("喝凉水")
    print("睡墙角")

# input 提示用户输入字符串
'''注意,一定是字符串'''
#res = input("请输入你的姓名")  #若用户不输入则程序阻滞
#print(res)
"""




"""

res1,res2 = input("请输入你的用户名:"),input("请输入你的密码:")
if res1 == "admin" and res2 == "000":
    print("恭喜登录成功")
else:
    print("用户名或者密码错误")