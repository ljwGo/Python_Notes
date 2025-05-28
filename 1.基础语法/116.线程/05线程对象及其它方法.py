from threading import Thread,current_thread,active_count
import os,time

def task():
    print('当前进程名：{} 线程名：{}'.format(os.getpid(),current_thread().name))
    time.sleep(2)

if __name__ == '__main__':
    t = Thread(target=task,)
    t2 = Thread(target=task,)
    t.start()
    t2.start()
    print('当前活跃线程数：{}'.format(active_count()))
    print('主进程号：{} 主前线程名：{}'.format(os.getpid(),current_thread().name))