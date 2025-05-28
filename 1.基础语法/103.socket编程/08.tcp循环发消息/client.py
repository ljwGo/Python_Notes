import socket
sk = socket.socket()
sk.connect(('172.18.214.63',9000))
while True:
    strvar = input('请输入您要发送的消息：')
    sk.send(strvar.encode('utf-8'))
    res = sk.recv(1024)
    if res == b'q':
        break
    print(res.decode())
sk.close()