# 1、什么是异常
# 异常是程序发生错误的信号，程序一旦出错就会抛出异常，程序的运行随即终止
# 异常处理的三个特征：
#   异常的追踪信息
#   异常的类型
#   异常的内容

# 2、为何处理异常
# 为了增强程序的健壮性，即便是程序运行过程中出错了，也不要终止程序
# 而是捕捉并且处理：将出错信息记录到日志内

# 3、如何处理异常？
# 3.1 语法上的错误 SyntaxError。

# 3.2 逻辑上的错误
#   错误发生的条件是可以预知的
while 1:
    age = input('请输入您的姓名：').strip()
    if age.isdigit():
        age = int(age)
        if age > 18:
            print('猜大了')
        elif age < 18:
            print('猜小了')
        else:
            print('猜中了')
            break
    print('必须输入纯数字')

#   错误发生的条件是无法预知的
# try:
#     # code... 子代码块
#     pass
# except 异常类型1 as e:
#     pass
# except 异常类型2 as e:
#     pass
# ...
# else:
#     如果被检测的子代码快没有异常，就会发生
# finilly:
#     无论被检测的子代码快是否有异常，都会发生（应该把被检测代码中用于回收系统资源的代码放到这里）

# print('start..........')
#
# try:
#     print('11111111111111')
#     l = [11,22]
#     l[2]
#     print('22222222222222')
#     xxx
#     print('33333333333333')
#     dic = {'a':1}
#     dic['a']
# except IndexError as e: # 捕捉到相关异常后，代码块中其它代码不会继续执行
#     print('异常的信息：',e)
#
#
#
# print('end............')

# print('start..........')
#
# try:
#     print('11111111111111')
#     l = [11,22]
#     l[2]
#     print('22222222222222')
#     xxx
#     print('33333333333333')
#     dic = {'a':1}
#     dic['a']
# except (IndexError,NameError) as e: # 捕捉到相关异常后，代码块中其它代码不会继续执行
#     print('异常的信息：',e)
# except Exception as e: # 万能异常
#     pass
#
# print('end............')

# print('start..........')
#
# try:
#     print('11111111111111')
#     l = [11,22]
#     l[2]
#     print('22222222222222')
#     xxx
#     print('33333333333333')
#     dic = {'a':1}
#     dic['a']
# else: # else不能单独与try使用
#     pass
#
# print('end............')