from threading import Thread
import socket

def task(conn):
    while 1:
        try:
            data = conn.recv(1024)
            if data is None: break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            conn.close()
            break

server = socket.socket()
server.bind(('127.0.0.1', 6666))
server.listen(5)
while 1:
    conn, addr = server.accept()
    print('卡在这里了')
    t = Thread(target=task,args=(conn,))
    t.start()