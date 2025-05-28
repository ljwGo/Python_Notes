import hashlib,socket,json
def get_md5_code(usr,pwd):
    # 将用户名作为加密的盐key
    hs = hashlib.md5(usr.encode())
    hs.update(pwd.encode())
    res = hs.hexdigest()
    return res

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
conn,addr = sk.accept()
msg = conn.recv(1024)
dic = json.loads(msg.decode())
#print(msg,type(msg))

sign = False
with open('userinfo.txt',mode='r+',encoding='utf-8') as fp:
    for line in fp:
        usr,pwd = line.strip().split(':')
        if usr == dic['username'] and pwd == get_md5_code(dic['username'],dic['password']):
            res = {'code':1}
            res_msg = json.dumps(res)
            conn.send(res_msg.encode())
            sign = True
            break
            # 如果登录成功,默认改成True

if sign == False:
    # 登陆失败，返回状态码为0
    res = {'code':0}
    conn.send(json.dumps(res).encode())

conn.close()
sk.close()





