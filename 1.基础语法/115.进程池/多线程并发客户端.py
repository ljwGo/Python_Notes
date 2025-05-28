import socket
from threading import Thread

def client_s():
    client = socket.socket()
    client.connect(('127.0.0.1',8080))
    while 1:
        client.send(b'hello world')
        info = client.recv(1024)
        print(info.decode('utf-8'))

if __name__ == '__main__':
    for i in range(100):
        t = Thread(target=client_s,)
        t.start()