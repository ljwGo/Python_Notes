# ### lock 线程锁，用来保证线程数据安全
from threading import Thread,Lock
n = 0
def func1(lock):
    global n
    for i in range(100000):
        lock.acquire()
        n -= 1
        lock.release()

def func2(lock):
    global n
    for i in range(100000):
        with lock:
            n += 1

if __name__ == '__main__':
    lst = []
    lock = Lock()
    for i in range(10):
        t1 = Thread(target=func1,args=(lock,))
        t2 = Thread(target=func2,args=(lock,))
        t1.start()
        t2.start()
        lst.append(t1)
        lst.append(t2)

    for i in lst:
        i.join()

    print('主线程执行结束')
    print(n)