from threading import Thread,Lock
import time

money = 100
lock = Lock()

def task():
    global money
    lock.acquire()
    tmp = money
    time.sleep(0.1)
    money = tmp - 1
    lock.release()

if __name__ == '__main__':
    listvar = []
    for i in range(100):
        t = Thread(target=task,)
        t.start()
        listvar.append(t)

    for k in listvar:
        k.join()
    print(money)
