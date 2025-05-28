import socket
def auth():
    msg = sk.recv(32)

sk = socket.socket()
sk.connect('127.0.0.1',9000)
socret_key = 'ig牛逼'
auth()
sk.close()















