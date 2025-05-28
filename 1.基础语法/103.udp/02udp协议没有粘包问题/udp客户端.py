import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.sendto(b'hello',('127.0.0.1',6666))
sk.sendto(b'world',('127.0.0.1',6666))
sk.close()