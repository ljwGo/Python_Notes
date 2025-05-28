from gevent import monkey; monkey.patch_all()
import socket
import gevent
import time
from threading import currentThread as cthread

def talk(conn):
    pass

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9000))
    sk.listen()
    