# 第一种
from multiprocessing import Process
import time

def task(name):
    print('{} is running'.format(name))
    time.sleep(3)
    print('{} is over'.format(name))

if __name__ == '__main__':
    # 1、创建一个对象
    p = Process(target=task,args=('json',))
    # 2、开启进程
    p.start() # 告诉操作系统帮你创建一个进程
    print('主进程')

'''
windows操作系统下 创建进制一定要在main内创建
因为windows下创建进程类似于模块导入的方式
会从上往下依次执行代码

linux中则是直接将代码完成复制一份
'''

# 第二种方式 类的继承
from multiprocessing import Process
import time

class MyProcess(Process):
    def run(self):
        print('hello')

if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('主')

# 总结
'''
创建进程就是在内存中申请一块内存空间将需要运行的代码丢进去
一个进程对应在内存中就是一块独立的内存空间
多个进程对应在内存中就是多块独立的内存空间
进程与进程之间的数据是独立开来的，想要交互必须借助其它软件或者模块
'''