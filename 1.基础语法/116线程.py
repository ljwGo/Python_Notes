# ### 线程
'''
进程是资源分配的最小单位
线程是程序调度的最小单位
默认一个进程当中，含有一个线程
线程和线程之间共享同一份进程资源
'''
import os,time,random
from threading import Thread
from multiprocessing import Process

# 1 进程中可以包含多个线程
'''
def func(num):
    time.sleep(random.uniform(0.1,1))
    print('子线程',num,os.getpid())

for i in range(10):
    t = Thread(target=func,args=(i,))
    t.start()
'''
# 2 并发多线程 和 多进程，谁的速度快
def func(num):
    print('子进程',num,os.getpid())

if __name__ == '__main__':
    starttime = time.perf_counter()
    lst = []
    for i in range(1000):
        t = Thread(target=func,args=(i,))
        t.start()
        lst.append(t)
    for i in lst:
        print(i)
        i.join()
    endtime = time.perf_counter()
    print('多线程执行的时间:',endtime-starttime)

# 3 多进程的执行时间
    time1 = time.time()
    lst = []
    for i in range(1000):
        p = Process(target=func,args=(i,))
        p.start()
        lst.append(p)
    for i in lst:
        i.join()
    time2 = time.time() - time1
    print('多进程执行的时间：',time2)

# 4 线程相关函数
'''
线程.is_alive() 检测线程是否仍然存在
线程.setName() 设置线程名字
线程.getName() 获取线程名子
1.currentThread().ident 查看线程id号
2.enumerate() 返回目前正在运行的线程列表
3.activeCount() 返回目前正在运行的线程数量
'''
def func():
    time.sleep(0.5)
t = Thread(target=func)
print(t)
t.start()
print(t.is_alive())
print(t.getName())
t.setName('wangwen')
print(t.getName())

from threading import current_thread,enumerate
def func():
    print('子线程:',current_thread().ident)
t = Thread(target=func)
t.start()
print('主线程:',current_thread().ident)
