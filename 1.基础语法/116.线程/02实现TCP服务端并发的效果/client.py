import socket
client = socket.socket()
client.connect(('127.0.0.1',8080))
while 1:
    client.send(b'hello world')
    data = client.recv(1024)
    print(data.decode('utf-8'))