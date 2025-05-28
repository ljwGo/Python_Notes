from threading import Thread
import time

def task(name):
    print('{} is running'.format(name))
    time.sleep(2)
    print('{} is over'.format(name))

if __name__ == '__main__':
    t = Thread(target=task,args=('egon',))
    t.daemon = 1
    t.start()
    print('主')

# 主线程运行结束之后不会立刻结束，会等待所有其他非守护进程结束才会结束
