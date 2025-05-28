import socket,json
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
usr = input('请输入您的账户:')
pwd = input('请输入您的密码:')
dic={'username':usr,'password':pwd,'operate':'login'}
# 返回json格式的字符串
res = json.dumps(dic)
# 在把json字符串转换成字节流并发送
sk.send(res.encode())

msg2 = sk.recv(1024)
dic_code = json.loads(msg2.decode())
if dic_code['code']:
    print('恭喜你登陆成功')
else:
    print('抱歉，登陆失败')

# 关闭链接
sk.close()
