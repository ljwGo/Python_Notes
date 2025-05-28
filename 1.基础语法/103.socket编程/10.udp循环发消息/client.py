import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
strvar = input('请输入您要发送的信息：')
sk.sendto(strvar.encode(utf-8),('127.0.0.1',9100))
msg,cli_addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.close()
