import socket

# 1、买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2、拨通号码
phone.connect(('127.0.0.1',6666))
# 3、收发数据
while 1:
    phone.send('hello egon 哈哈哈'.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('utf-8'))

# 4、关闭连接(必选的)
phone.close()