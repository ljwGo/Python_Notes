# ### join 等待所有子进程执行完毕之后，主进程任务再继续执行，保证子父进程的同步性
import time
import os
# 1 join 基本用法
from multiprocessing import Process
"""
'''
def func():
    print('发送第一封邮件')

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    #必须等待子进程执行完毕之后，再执行下面的代码
    p.join()
    print('发送第二封邮件')
'''

# 2 多个子进程通过join加阻塞，可以同步子进程和主进程
def func(i):
    print('发送%s个邮件'%(i))

if __name__ == '__main__':
    lst = []
    for i in range(10):
        p = Process(target=func,args=(i,))
        p.start()
        # p.join() 从结果上达到目的，但是会严重损坏性能，速度下降
        lst.append(p)
        print(lst)
    for i in lst:
        i.join()

    print('主进程负责发送最后一份邮件')
"""

# ### 2 使用自定义类的方法创建进程
'''
自定义创建进程的要求
    1 必须继承Process这个父类
    2 所有的逻辑要写在run方法里面
'''
# 1 基本语法
"""
class MyClass(Process):
    # 方法名字必须是run
    def run(self):
        print('1.子进程>>%s,2.父进程>>%s' % (os.getpid(),os.getppid()))

if __name__ == '__main__':
    p = MyClass()
    p.start()
    print('3.子进程>>%s,4.父进程>>%s' % (os.getpid(),os.getppid()))
"""

# 2 往自定义的进程中传参
"""
class MyProcess(Process):
    def __init__(self,args):
        # 必须手动调用一下父类的构造方法，进行系统的初始化
        super().__init__()
        # 将传进来的参数，赋值给一个成员属性args
        self.args = args

    def run(self):
        print('1.子进程>>%s,2.父进程>>%s' % (os.getpid(), os.getppid()))
if __name__ == '__main__':
    lst = []
    for i in range(10):
        p = MyProcess(i)
        p.start()
        lst.append(p)

    for i in lst:
        i.join()

    print('主进程结束')
"""

# ### 守护进程
'''
默认情况下，主进程要等待所有子进程执行完毕之后，才会关闭程序，释放资源
守护进程进行在主进程代码执行结束之后，就直接关闭
守护进程守护的是主进程

语法：
    进程.daemon = True 设置当前这个进程是守护进程
    守护主进程，如果主进程执行代码结束了，守护进程立刻终止
    必须要写在start（）调用之前，进行设置
'''

from multiprocessing import Process
# 1 基本语法
'''
def func():
    print('当前子进程start')
    print('当前子进程end')

if __name__ == '__main__':
    p = Process()
    p.daemon = True
    p.start()
    print('主进程执行结束')
'''

# 2 多个子进程场景
"""
def func1():
    count = 1
    while True:
        time.sleep(0.5)
        print('*' * count)
        count += 1
def func2():
    print('func2 start...')
    time.sleep(2)
    print('func2 end...')

if __name__ == '__main__':
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p1.start()
    p2.start()

    print('主进程执行代码结束...')
"""

# 3 守护进程的实际用途：监控报活
def alive():
    while True:
        print('10好服务器运转正常')
        time.sleep(2)

def func():
    time.sleep(4)
    print('10号服务器正在工作')

if __name__ == '__main__':
    p1 = Process(target=alive)
    p1.daemon = True
    p1.start()

    p2 = Process(target=func)
    p2.start()
    p2.join()

    # 如果统计报表的任务挂掉了，立刻终止报活
    print('目前服务器正常运转')