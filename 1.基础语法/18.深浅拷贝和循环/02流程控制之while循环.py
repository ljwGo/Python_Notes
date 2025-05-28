# 1、循环的语法与基本使用
'''
print(1)
while 条件:
    代码1
    代码2
    代码3
print(3)
'''

# 2、死循环与效率问题
# count = 0
# while count < 5:
#     print(count)
#     # count+=1
# while True:
#     name = input('请输入您的姓名:')
# 纯计算无io的死循环还会导致致命的效率问题
# while True:
#     1+1

# 3、循环的应用
# username = 'egon'
# password = '123'
# sign = True
# while sign:
#     inp_account = input('请输入您的账号:')
#     inp_password = input('请输入您的密码:')
#     if inp_account == username and inp_password == password:
#         print('登陆成功')
#         sign = False # 之后的代码还会运行，下次循环判断条件时才生效
#     else:
#         print('账号或者密码错误')
#     print('====end====')

# while 1:
#     inp_account = input('请输入您的账号:')
#     inp_password = input('请输入您的密码:')
#     if inp_account == username and inp_password == password:
#         print('登陆成功')
#         break # 在循环中，只要在运行到break就会立刻终止本层循环
#     else:
#         print('账号或者密码错误')
#     print('====end====')
# 4、退出循环的两种方式
# 方式一: 讲条件改为False
# 方式二: while加break

# 5、循环嵌套
'''
sign = True
while sign:
    while sign:
        while sign:
            sign = True # 最后一层关闭所有循环
            break
        break
    break
'''
# while 1:
#     inp_account = input('请输入您的账号:')
#     inp_password = input('请输入您的密码:')
#     if inp_account == username and inp_password == password:
#         print('登陆成功')
#         while True:
#             l = ['取款', '查询余额', '转账']
#             iter_l = enumerate(l)
#             while True:
#                 try:
#                     tup = next(iter_l)
#                     print('{tup[0]},{tup[1]}'.format(tup=tup))
#                 except StopIteration:
#                     break
#             cmd = input('请输入要执行的命令:')
#             if cmd.lower() == 'q':
#                 break
#             else:
#                 print('命令{x}正在执行'.format(x=cmd))
#         break  # 在循环中，只要在运行到break就会立刻终止本层循环
#     else:
#         print('账号或者密码错误')
#     print('====end====')

# 8、while + continue:结束本次循环，直接进入下一次
# continue 的存在是为了结束循环中某个阶段，不需要使其执行
# count = 0
# while count < 6:
#     if count == 4:
#         count+=1
#         continue
#     print(count)
#     count+=1

# while + else （针对break）

# while True:
#    ...
# else:
#    print('else的代码会在while循环结束后，并且while循环是在没有break打断的情况下正常结束才会执行‘）

# username_dict = {'egon':123,'zhangshan':456,'lisi':789}
# count = 3
# while count > 0:
#     inp_account = input('请输入您的账号:')
#     if inp_account in username_dict:
#         inp_password = input('请输入您的密码:')
#         if inp_password == username_dict[inp_account]:
#             print('恭喜您登陆成功')
#             while True:
#                 cmd = input('请输入您的操作命令')
#                 if cmd.lower() == 'q':
#                     break
#                 print('操作{x}正在执行'.format(x=cmd))
#             break
#         else:
#             print('您输入的密码不正确')
#             count -= 1
#     else:
#         print('您输入的账号不存在')
# else:
#     print('您输错密码次数过多')

list1 = ['egon', 'lxx', 'alex']
list2 = ['egon', 'lxx', 'alex']
list1[0] = 'zhangshan'
print(list1,id(list1))
print(list2,id(list2))