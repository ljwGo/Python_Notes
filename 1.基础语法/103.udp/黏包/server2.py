import socket
import time
sk = socket.socket()
sk.bind(('127.0.0.1',8500))
sk.listen()
conn,addr = sk.accept()
# 在真正第一次发送数据之前，把真实的数据长度先发送过去
msg = '00000010'
conn.send(msg.encode('utf-8'))
conn.send('i love you'.encode('utf-8'))
# time.sleep(0.1)(不合适)
conn.send('really'.encode('utf-8'))
conn.close()
sk.close()
