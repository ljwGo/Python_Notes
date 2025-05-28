# ### socket 服务器
import socket
# 1 创建一个socket对象
sk = socket.socket()

# 2 绑定ip和端口[在网络上注册该主机] localhost => '127.0.0.1'
sk.bind(('172.18.214.63',9000))

# 3 开启监听
sk.listen()

# 4 建立三次握手
conn,addr = sk.accept()
#<socket.socket fd=544, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.18.214.63', 9000), raddr=('172.18.214.63', 53550)>
print(conn)
#('172.18.214.63', 53550)对方的ip对方的端口
print(addr)

# 5 收发数据的逻辑
msg = conn.recv(1024)
print(msg.decode('utf-8'))
# 发送数据
conn.send('好的，多穿衣服'.encode('utf-8'))

# 6 四次挥手
conn.close()

# 7 退还端口
sk.close()
