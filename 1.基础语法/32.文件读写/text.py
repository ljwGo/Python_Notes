username = input('your username>>>:')
password = input('your password>>>:')
with open('user_info', mode='a', encoding='utf-8') as fp:
    fp.write('{}:{}\n'.format(username, password))

inp_username = input('账号>>>:')
inp_password = input('密码>>>:')
with open('user_info', mode='r', encoding='utf-8') as fp2:
    for line in fp2:
        username, password = line.strip().split(':')
        if username == inp_username and password == inp_password:
            print('login success')
            break
    else:
        print('account or password is error')

copy_file = input('请输入copy目录:')
new_name = input('请输入new_name:')
with open('{}',mode='r',encoding='utf-8') as fp3,\
    open('{}',mode='w',encoding='utf-8') as fp4:
    for line in fp3:
        fp4.write(line)
# data = fp3.read()
# fp4.write(data)


