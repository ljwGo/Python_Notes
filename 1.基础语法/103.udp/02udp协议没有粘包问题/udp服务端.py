import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 6666))
# udp协议中，sendto与recvfrom一一对应，当recvfrom接受的字节数小于sendto发送的数据时
# 会截取部分数据，剩下数据会被丢弃掉
data1,client_addr1 = sk.recvfrom(2)
print(data1)
data2,client_addr2 = sk.recvfrom(1024)
print(data2)

sk.close()
