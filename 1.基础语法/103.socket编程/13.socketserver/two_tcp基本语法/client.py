# ### 客户端
'''
一发一收是一对send，recv必须个数上保持一致
否则收发次数不匹配，会出现异常
'''
import socket
# 1 创建一个socket对象
sk = socket.socket()

# 2 与服务器创建连接
sk.connect(('172.18.214.63',9000))

# 3 收发数据的逻辑
#  发送数据
sk.send('天气有点凉'.encode('utf-8'))

#  接收数据
msg = sk.recv(1024)
print(msg.decode('utf-8'))

# 4 关闭连接
sk.close()