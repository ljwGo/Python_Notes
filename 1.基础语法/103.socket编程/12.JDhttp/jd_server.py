import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9420))
sk.listen()

while True:
    print('server is waiting')
    conn, addr = sk.accept()
    # data: 符合http请求协议格式的请求信息字符串
    data = conn.recv(1024)
    print('data', data)
    with open('css_use.html', 'rb') as f:
        info = f.read()
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n"+info)
    conn.close()
    #sk.close()
