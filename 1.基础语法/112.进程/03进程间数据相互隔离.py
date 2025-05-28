from multiprocessing import Process

money = 1000 # 创建子进程时，为子进程开辟的内存空间中不仅有target中的函数体代码
# 还有其它来自主进程中的变量和方法，开启进程类似模块的导入

def task():
    print(money)
    # global money
    # money = 666
    print('子', money)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print(money)