import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('handle方法被触发') # 相当于conn(是三次握手成功之后的连接对象)
        print(self.request) # 相当于addr 对方的ip和端口号


server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
server.serve_forever()