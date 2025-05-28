from threading import Thread,Semaphore
import time
import random

sm = Semaphore(5)

def work(i):
    sm.acquire()
    print('伞兵{}号准备就绪'.format(i))
    time.sleep(random.randrange(2,5))
    print('伞兵{}号落地成盒'.format(i))
    sm.release()

if __name__ == '__main__':
    for i in range(1,21):
        t = Thread(target=work,args=(i,))
        t.start()