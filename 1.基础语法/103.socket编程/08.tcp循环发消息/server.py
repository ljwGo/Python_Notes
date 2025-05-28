# ### tcp 循环发消息
import socket
# 创建一个对象
sk = socket.socket()
# 绑定ip，端口号，在网络上注册该主机
sk.bind(('172.18.214.63', 9000))
# 开启监听
sk.listen()
while True:
    # 三次握手
    conn,addr = sk.accept()
    while True:
        # 收发数据
        res = conn.recv(1024)
        print(res.decode('utf-8'))
        # 发送消息
        strvar = input('请输入您要发送的消息：')
        conn.send(strvar.encode())
        # 退出
        if strvar == 'q':
            break
# 四次挥手
conn.close()
# 退还端口
sk.close()