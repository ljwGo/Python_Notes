# ### 进程队列 [让进程之间共享资源]
from multiprocessing import Process,Queue,Semaphore
import queue
'''
后进先出，先进后出，是栈队列的特点
queue，先进先出，后进后出
'''
# 1 基本语法
#q = Queue()
# 用put方法往队列中存值
#q.put(111)
# 用get方法从队列中取值
#res = q.get()
#print(res)
# 当队列中没有值了，在调用get就会发生阻塞
# res = q.get()
# print(res)
# get_nowait() 存在兼容性问题（不推荐使用，报错是线程队列中的空，在取值时存在bug）
#q.put(222)
#res = q.get_nowait()
#print(res)

# 2 可以使用queue 指定队列长度
#q1 = Queue(3)
#q1.put(111)
#q1.put(222)
#q1.put(333)
# 注意：如果超出了队列的长度，直接阻塞
#q1.put(44)
# 注意：如果超出了队列的长度，直接报错（不推荐）
#q1.put_nowait(44)

# 3 多进程之间共享数据
def func(q1):
    res = q1.get()
    print(res)
    q1.put(222)

if __name__ == '__main__':
    q1 = Queue()
    p = Process(target=func,args=(q1,))
    p.start()
    q1.put(111)
    p.join()
    res2 = q1.get()
    print(res2)