# ### udp 服务器
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
# 绑定ip，端口号
sk.bind(('172.18.214.63', 40000))
# udp协议，如果作为服务器，第一次需要先接受消息，才能得到对方的ip和端口号
msg,cli_addr = sk.recvfrom(1024)
print(msg,cli_addr)
sk.sendto('不要'.encode('utf-8'),cli_addr)
# 4 关闭连接
sk.close()