# ### 客户端
import socket
# 创建socket对象
sk = socket.socket(type=socket.SOCK_DGRAM)
# 2
msg = input('最新品上市，只要999元:')
sk.sendto(msg.encode('utf-8'),('172.18.214.63', 40000))
res,addr = sk.recvfrom(1024)
print(addr)
print(res.decode('utf-8'))
sk.close()