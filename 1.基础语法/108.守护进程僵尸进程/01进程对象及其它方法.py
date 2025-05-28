from multiprocessing import Process,current_process
import time
import os
# 计算机会给每一个进程分配一个独一无二的PID进程号
# 在window系统下使用tasklist命令查看进程号
#   tasklist |findstr PID查看具体的进程

# 在mac系统下，在终端使用ps aux查看进程号
#   ps aux|grep PID查看具体进程
def task():
    print(current_process().pid) # current_process().pid获取当前进程的进程号
    print(os.getpid()) # 可以取代current_process()
    print(os.getppid()) # 获取父进程的pid

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate() # 杀死当前进程
    # 告诉操作系统杀死进程，需要一定时间，而代码的运行速度极快
    time.time(0.1)
    print(p.is_alive()) # 判断当前进程是否存活
    print('主')