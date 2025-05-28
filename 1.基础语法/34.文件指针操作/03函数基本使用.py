'''
1、什么是函数
    函数就相当于具备某一功能的工具
    函数的使用必须遵循一个原则：
        先定义
        后调用
2、为何要用函数
    1、组织结构不清晰，可读性差
    2、代码冗余
    3、可维护性差、扩展性差

3、如何用函数
    先定义
        三种定义方式
    后调用
        三种调用方式
    返回值
        三种返回值的形式

# 1、先定义
def 函数名(参数1，参数2，...):
    """函数功能描述"""
    函数体
    return 值

# 形式一：无参函数
def func():
    print('哈哈哈哈')
调用
func()

# 定义函数发生的事情
1、申请内存空间保存函数体代码
2、将上述内存地址绑定给函数名
3、定义函数不会执行函数体代码，但是会检测函数体语法

# 调用函数发生的事情
1、通过函数名找到函数的内存地址
2、然后加括号就是在触发函数体代码的执行
print(func)

# 示范
x = 111
def foo():
    print(x)
    print('from poo')

foo()

# 实例二：
def poo():
    boo()
    print('from poo')
def boo():
    print('from boo')

poo()

# 实例三：
def poo():
    boo()
    print('from poo')
poo()
def boo():
    print('from boo')

# 形式二：有参函数
def func(x,y):
    print(x,y)

func(1,2)

# 形式三：空函数，函数体代码为pass
def func(x,y):
    pass

# 三种定义方式个用在何处
# 1、无参函数的应用场景
# 2、有参函数的应用场景
def func(x,y):
    print(x)
    print(y)
# 3、空函数的应用场景(构思的时候使用)
def func():
    pass

# 2、调用函数
1、语句的形式：只加括号调用函数
2、函数调用可以当做参数
3、表达式输出

# 3、函数返回值
return是函数结束的标志:即函数体代码一旦运行到return会立刻终止函数的运行，并且会将return后的值当作本次运行的结果返回
1、返回None：函数体内没有return、
                    return None、
                    return
2、返回值一个值：return 值

3、返回多个值：用逗号分隔开多个值，会被return返回成元组
def func():
    return 10,'aa',[1,2]
'''