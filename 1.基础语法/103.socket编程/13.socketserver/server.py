# ### 服务器
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #写收发数据的逻辑
        print('handle成员中的代码被执行了')

# 实例化对象 ThreadingTcpServer((ip,端口号),自定义的类)
# 利用ThreadingTcpServer 实现tcp链接的并发操作
server = socketserver.ThreadingTCPServer(('127.0.0.1',9002),MyServer)
# 建立链接，循环使用
server.serve_forever()