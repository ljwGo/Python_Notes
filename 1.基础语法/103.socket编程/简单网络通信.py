import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8001))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    with open(r'D:\download\pythonProjects\djangoProCmd03\templates\temp.html', 'rb') as f:
        conn.send(f.read())
    print(conn.recv(1024))
    conn.close()

