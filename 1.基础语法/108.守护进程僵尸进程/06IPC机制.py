from multiprocessing import Process,Queue
import time

# 研究思路
#   1、主进程跟子进程借助于队列通信
#   2、子进程跟子进程借助于队列通信

def producer(q):
    time.sleep(0.1)
    q.put('我是23号技师，很高兴为您服务')
    print('hello big baby')

def consumer(q):
    print(q.get())

if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=producer,args=(q,))
    p2 = Process(target=consumer,args=(q,))
    p2.start()
    p1.start()
    # print(q.get())