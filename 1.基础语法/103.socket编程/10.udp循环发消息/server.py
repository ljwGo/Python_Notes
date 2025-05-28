import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9100))
while True:
    msg,cli_addr = sk.recvfrom(1024)
    print(msg,cli_addr)
    strvar = input('请问你要发送什么：')
    sk.sendto(strvar.encode('utf-8'),cli_addr)
sk.close()