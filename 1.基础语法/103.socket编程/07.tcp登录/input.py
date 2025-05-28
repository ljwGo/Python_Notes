import hashlib
with open('userinfo.txt',mode='w+',encoding=('utf-8')) as fp:
    usr = input('请输入您的账号：')
    pwd = input('请输入您的密码：')
    hs = hashlib.md5(usr.encode())
    hs.update(pwd.encode())
    usr += ':' + hs.hexdigest()
    fp.write(usr)