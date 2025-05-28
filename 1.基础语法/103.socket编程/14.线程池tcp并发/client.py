import socket
from concurrent.futures import ThreadPoolExecutor

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

def talk(conn):
    while True:
        conn.send(b'hello')
        print(conn.recv(1024))
    conn.close()

if __name__ == '__main__':
    tp = ThreadPoolExecutor(60)
    while True:
        conn, addr = sk.accept()
        tp.submit(talk,conn)
    tp.shutdown()
    sk.close()