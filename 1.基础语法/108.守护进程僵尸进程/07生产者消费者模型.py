from multiprocessing import Process,Queue,JoinableQueue
import time
import random

# 生产者：生产/制造东西的
# 消费者：消费/处理东西的
# 该模型除了上述两个之外还需要一个媒介：消息队列

def producer(name,food,q):
    for i in range(11):
        data = '{}生产了{}'.format(name,food)
        time.sleep(random.randrange(1,4))
        print(data)
        q.put(data)

def consumer(name,q):
    # 消费者胃口很大，关盘行动
    while 1:
        food = q.get()
        # 判断从队列中得到的值是否为结束标识None
        # if food is None:
        #     break
        # time.sleep(random.randrange(1,3))
        print('{}吃了{}'.format(name,food))
        q.task_done()

if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer,args=('egon','包子',q))
    p2 = Process(target=producer,args=('tank','饺子',q))
    p3 = Process(target=consumer,args=('lisi',q))
    p4 = Process(target=consumer,args=('zhangsan',q))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    # 等待生产者生产完毕后，添加一个结束标识None
    # 有多少个消费者就有多少个None
    # q.put(None)
    # q.put(None)
    q.join()

    '''
    JoinableQueue 每当你往该队列中存入数据的时候 内部会有一个计数器+1
    当每次执行你调用task_down方法时 计数器为0
    q.join() 当技术器为0时，代码往下执行
    '''