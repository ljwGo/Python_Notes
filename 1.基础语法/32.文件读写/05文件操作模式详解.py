# 以t模式为基础进行内存操作

# 1、r（默认的操作模式）：只读模式，当文件不存在时报错，文件存在时，文件指针跳到开始模式
# with open('笔记',mode='rt',encoding='utf-8') as fp:
#     print(r'{x:*>15}'.format(x='第一次读'))
#     res = fp.read() # 把所有内容从硬盘读入内存
#     print(res)

# r模式案例
inp_username = input('your username>>>:')
inp_password = input('your password>>>:')
with open('user_info', mode='rt', encoding='utf-8') as f2:
    for line in f2:
        username, password = line.strip().split(':')
        if inp_password == password and inp_username == username:
            print('login success')
            break
    else:
        print('your password or account is error')

# 2、w：只写模式，当文件不存在时,当文件存在时会清空文件，指针位于开始位置
with open('d.txt', mode='wt', encoding='utf-8') as fp2:
    # fp2.read() 不可读
    fp2.write('哈哈哈我擦勒\n')

# 强调1：
# 在以w模式打开文件没有关闭的情况下，连续的写入，新的内容总是跟在旧的内容之后
# 案例，文本文件的copy
with open('a.txt', mode='rt', encoding='utf-8') as fp1,\
    open('b.txt', mode='wt', encoding='utf-8') as fp2:
    res = fp1.read()
    fp2.write(res)


# 3、a：只追加写，在文件不存在时会创建空文档，在文件存在时会直接存在内容末尾
# 实例注册功能
# inp_username = input('your username>>>:')
# inp_password = input('your password>>>:')
# with open('db 数据文件.txt', mode='wt', encoding='utf-8') as fp3:
#     fp3.write('{}:{}\n'.format(inp_username,inp_password))

# 了解：+不能单独使用，必须配合r、w、a使用
