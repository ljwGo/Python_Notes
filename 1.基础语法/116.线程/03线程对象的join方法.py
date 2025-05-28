from threading import Thread
import time

def task():
    print('hello')
    time.sleep(1)
    print('world')

if __name__ == '__main__':
    t = Thread(target=task,)
    t.start()
    t.join()
    print('主')
