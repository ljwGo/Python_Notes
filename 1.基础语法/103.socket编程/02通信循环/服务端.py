import socket
# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 流式协议=> tcp协议 SOCK_DGRAM 包式协议
# 2、绑定手机卡
phone.bind(('127.0.0.1',6666)) # 127.0.0.1 特殊的ip地址，只能被自己访问到
# 3、开机
phone.listen(5) # 5指的是半连接池的大小
# 4、等待电话链接请求
conn, addr = phone.accept()
print(conn, addr)

# 5、通信：收\发信息
while 1:
    data = conn.recv(1024) # 最大接受的数据两位1024Bytes，收到的是bytes类型
    print(data.decode('utf-8'))
    conn.send(data.upper())

# 6、关闭电话链接conn(必选的)
conn.close()

# 7、关机(可选操作)
phone.close()