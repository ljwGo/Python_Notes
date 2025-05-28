# 服务端应该满足两个特点；
# 1、一直对外提供服务
# 2、实现并发，同时为与个客户端交互
import subprocess
import socket
import struct
# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 流式协议=> tcp协议 SOCK_DGRAM 包式协议
# 2、绑定手机卡
phone.bind(('127.0.0.1',6666)) # 127.0.0.1 特殊的ip地址，只能被自己访问到
# 3、开机
phone.listen(5) # 5指的是半连接池的大小
# 4、等待电话链接请求
while 1:
    conn, addr = phone.accept()

# 5、通信：收\发信息
    while 1:
        # 当客户端非正常退出时，不同的操作系统会发生不同的情况：
        #   linux系统下 服务端会进入死循环，循环收空，循环发空
        #   window系统下 服务端会报错
        try:
            cmd = conn.recv(1024) # 最大接受的数据两位1024Bytes，收到的是bytes类型
            if not len(cmd):
                break
            obj = subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE
                             )
            stderr_res = obj.stderr.read()
            stdout_res = obj.stdout.read()
            # res = stderr_res + stdout_res # 得到的结果都是字节流,编码格式依照操作系统
            total_num = len(stderr_res) + len(stdout_res)
            total_num = struct.pack('i',total_num)
            # 1、先发数据包头（固定长度），包含真正数据的描述信息
            conn.send(total_num)

            # 2、再发真实的数据
            conn.send(stdout_res)
            conn.send(stderr_res)
            # print(cmd.decode('utf-8'))
            # conn.send(cmd.upper())
            # conn.send(res)
        except Exception:
            break
    # 6、关闭电话链接conn(必选的)
    conn.close()

# 7、关机(可选操作)
# phone.close()