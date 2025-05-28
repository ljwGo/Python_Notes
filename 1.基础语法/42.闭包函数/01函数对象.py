# 精髓：可以把函数当成变量去用
# func=内存地址
# def func():
#     print('from func')

# 1、可以赋值
# f=func
# print(f,func)
# f()

# 2、可以当作函数的参数传给另外一个函数
# def foo(x):
#     x()
# foo(func) # foo(函数的内存地址)

# 3、可以把函数当作另外一个函数的返回值
# def boo(x):
#     return x
# res = boo(func)
# res()

# 4、可以当作容器类型的一个元素
# l = [func, 111, 222,func()]
# l[0]()

def login():
    print('登录功能')

def transfer():
    print('转账功能')

def check_banlance():
    print('查询功能')

while True:
    print('''
    0 退出
    1 登录
    2 转账
    3 查询余额
    4 提现
    ''', end='')
    choice = input('请输入命令编号:').strip()
    if choice == '0':
        break
    elif choice == '1':
        login()
    elif choice == '2':
        transfer()
    elif choice == '3':
        check_banlance()
    else:
        print('您输入的命令不存在')
    # if choice in func_dic:
    #     func_dic[choice]()
    # else:
    #     print('命令不存在')
# 优化：
func_dic={
    '1':login,
    '2':transfer,
    '3':check_banlance()
}
func_dic[choice]()