from threading import Thread
import time

# 第一种方法
def task(name):
    print('{} is running'.format(name))
    time.sleep(1)
    print('{} is over'.format(name))

# 开启线程不需要在main下面执行代码，直接书写就可以
# 但是我们还是习惯性的将启动命令写在main下面

t = Thread(target=task,args=('egon',))
t.start()
print('主')

# 第二种方法
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print('{} is running'.format(self.name))

t = MyThread('egon')
t.start()