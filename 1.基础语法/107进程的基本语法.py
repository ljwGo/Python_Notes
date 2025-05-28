from multiprocessing import Process
import os
"""
# 1 进程的基本语法
'''
获取当前进程号 os.getpid()
获取父进程的id号 os.getppid()
linux 中杀死进程号 kill -9 进程号
'''
def func():
    print('1.子进程id>>>%s，2.父进程id>>>%s' % (os.getpid(),os.getppid()))
# fork linux支持 但是 windows不支持

if __name__ == '__main__':
    print('3.子进程id>>>%s,4.父进程id>>>%s' % (os.getpid(),os.getppid()))
    # 创建一个子进程,单独执行func这个任务，返回p进程对象
    '''target = 函数 让当前子进程执行的任务'''
    p = Process(target=func)
    # 调用子进程
    p.start()
    '''子进程和主进程同时执行'''

# 2 带有参数的函数任务
'''
Process 创建进程对象，参数要依靠args进行传递
args必须制定一个元素，参数和参数之间要用逗号进行分割
'''
def func(n):
    for i in range(1,n+1):
        print('1.子进程id>>>%s,2.父进程id>>>%s' % (os.getpid(),os.getppid()))

if __name__ == '__main__':
    n = 5
    # 创建一个子进程
    p = Process(target=func,args=(n,))
    # 调用子进程
    p.start()

    for i in range(1,n+1):
        print('*' * i)
"""

'''
# 3 进程之间的数据彼此隔离
num = 100
def func():
    global num
    num += 1
    print('我是子进程：',num)
func()

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    print('我是主进程：',num)
'''

# 4 多个进程同时并发，子父进程之间的关系
def func(i):
    print('1.子进程id>>>%s,2.父进程id>>>%s' % (os.getpid(),os.getppid()),i)

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=func,args=(1,))
        p.start()

    print('主进程执行结束')
'''
# 默认程序在并发任务时，因为cpu调度策略，
不一定哪个进程先执行，哪个进程后执行，要参照哪个进程变成就绪态，cpu会优先执行
cpu遇到阻塞，就会立刻切换进程任务

主进程会在执行结束后，等所有紫禁城执行完毕，最后在关闭程序，释放资源
如果不等待子进程，紫禁城就会在后台不停的占用资源，造成僵尸进程
不方便对该进程进行管理，不知都该就能成的来源，会导致维护困难
'''