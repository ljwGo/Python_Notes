# ### 服务端
import socket
import struct
sk = socket.socket()
sk.bind(('127.0.0.1',9002))
sk.listen()
conn,addr = sk.accept()
# 处理收发数据的逻辑
strvar = input('请输入信息:')
# 变成字节流
msg = strvar.encode('utf-8')
length = len(msg)
# 第一次把长度优先发送过去
res = struct.pack('i',length)
conn.send(res)
# 第二次发送真实的数据
conn.send(strvar.encode('utf-8'))
conn.close()
sk.close()