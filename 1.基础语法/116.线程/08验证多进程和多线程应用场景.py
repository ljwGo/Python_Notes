from multiprocessing import Process
from threading import Thread
import time
import os

# 计算密集型
def work():
    num = 0
    for i in range(1,10000000):
        num *= i

if __name__ == '__main__':
    print(os.cpu_count())
    l = []
    start_time = time.time()
    for i in range(12):
        p = Process(target=work,)
        p.start()
        l.append(p)
        t = Thread(target=work,)
        t.start()
        l.append(t)

    for p in l:
        p.join()
    end_time = time.time()
    print(end_time-start_time)

# IO密集型
def work():
    time.sleep(2)

if __name__ == '__main__':
    l = []
    start_time = time.time()
    for i in range(400):
        p = Process(target=work,)
        p.start()
        l.append(p)
        t = Thread(target=work,)
        t.start()
        l.append(t)

    for p in l:
        p.join()
    end_time = time.time()
    print(end_time-start_time)
