# ### 守护线程：等待所有线程全部执行结束之后，再终止，守护所有进程
from threading import Thread
import time
def func1():
    while True:
        time.sleep(1)
        print('我是子线程func1')

def func2():
    print('func2 start...')
    time.sleep(3)
    print('func2 end...')

t1 = Thread(target=func1)
t1.setDaemon(True)
t1.start()

t2 = Thread(target=func2)
t2.start()
print('我是主线程')