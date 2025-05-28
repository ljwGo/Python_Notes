import socket
import struct
# 1、买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2、拨通号码
phone.connect(('127.0.0.1',6666))
# 3、收发数据
while 1:
    strvar = input('请输入您要发送的命令：').strip()
    # 当发空时,数据会被发送到对方，但会导致对方无法从缓存中拿到数据，因此对方会程序会阻塞在recv中
    if not len(strvar):
        continue
    phone.send(strvar.encode('utf-8'))
    total_num = phone.recv(4)
    total_num = struct.unpack('i',total_num)[0]
    recv_size = 0
    while recv_size < total_num:
        data = phone.recv(1024)
        recv_size += len(data)
        print(data.decode('gbk'))
        print(data.decode('gbk'))
    else:
        print('')
# 4、关闭连接(必选的)
phone.close()