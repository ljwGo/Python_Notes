# ### 回调函数
'''
回调函数:
    把函数当成参数传递给另外一个函数
    在当前函数执行完毕之后，调用一下传递进来的函数，该函数是回调函数
'''
from concurrent.futures import ThreadPoolExecutor
from threading import currentThread as cthread
import time,os

from multiprocessing import pool
# 1 线程池，它的回调函数由子线程执行
'''
add_done_callback 在获取当前线程的返回值是，可以异步并发
由执行任务的当前子线程，调用回调函数
'''
def func(i):
    time.sleep(0.5)
    print('thread',i,cthread().ident)
    print('thread %s end' % (i))
    return '*' * i

# 回调函数
def call_back(obj):
    print('call_back',cthread().ident)
    print(obj)
    print(obj.result())

tp = ThreadPoolExecutor(5)
lst = []
for i in range(1,11):
    obj = tp.submit(func,i)
    obj.add_done_callback(call_back)
    #lst.append(obj)

for i in lst:
    print(i.result())

print('主线程执行结束...end',cthread().ident)

# 代码解析：
class MyClass():
    def add_done_callback(self,func):
        func(self)

def call_back(args):
    print('call_back:',cthread().ident)
    print(args)
    print(args.result())

obj = MyClass()
obj.add_done_callback(call_back)

# 2 进程池，它的回调函数
'''
1 add_done_callback 在获取当前线程的返回值的时候，可以异步并发，加快速度
2 回调函数由谁执行，都是有主进程来完成
'''
from concurrent.futures import ProcessPoolExecutor
def func(i):
    print('Process',i,os.getpid)
    time.sleep(0.1)
    print('Process %s end' % (i))
    return '*' * i

def call_back(obj):
    print('call_back:',os.getpid())
    print(obj.result())

if __name__ == '__main__':
    po = ProcessPoolExecutor(6)
    for i in range(20):
        obj = po.submit(func,i)
        obj.add_done_callback(call_back)

    print('主进程执行结束 ...',os.getpid())