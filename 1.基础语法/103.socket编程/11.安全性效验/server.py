import socket,hashlib,os
def auth():
    # 随机的32位二进制字节流
    res = os.urandom(32)
    # 把res发送给对象的服务器
    conn.send(res)

sk = socket.socket()
sk.bind('127.0.0.1',9000)
sk.listen()
conn,addr = sk.accept()
conn.close()
sk.close()















