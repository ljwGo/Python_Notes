from threading import Thread,Lock,RLock
import time

# metuxA = Lock()
# metuxB = Lock()
metuxA = metuxB = RLock()
# 递归锁的特点：
'''
递归锁可以被连续acquire和release，当每次acquire时，锁内部的计数器自动加一；
当每次release时，锁内部的计数器自动减一。当计数为0时，锁才能真正被释放，其它线程才能枪锁
'''

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        metuxA.acquire()
        print('{}抢到了锁A'.format(self.name))
        metuxB.acquire()
        print('{}抢到了锁B'.format(self.name))
        metuxA.release()
        metuxB.release()

    def func2(self):
        metuxB.acquire()
        print('{}抢到了锁B'.format(self.name))
        time.sleep(2)
        metuxA.acquire()
        print('{}抢到了锁A'.format(self.name))
        metuxA.release()
        metuxB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
