import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request) # 如果是tcp协议，self.request => conn
        print(self.client_address)

s = socketserver.ThreadingTCPServer(('123.0.0.1',6666),MyServer)
s.serve_forever()
# 等同于
# while True:
#   conn,client_addr=server.accept()
#   启动一个线程(conn,client_addr)

# 第二件事：拿到链接对象，与其进行通信循环
