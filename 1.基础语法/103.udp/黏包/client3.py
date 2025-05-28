# ### 客户端
import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',9002))
n = sk.recv(4)
tup = struct.unpack('i',n)
res = sk.recv(tup[0])
print(res.decode('utf-8'))
res2 = socket.recv(1024)
sk.close()