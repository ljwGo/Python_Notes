from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
import os
import time

def roll_back(name):
    print(name.result()*2)

def task(i):
    print('你好{}{}'.format(current_thread().name,i))
    print(os.getpid())
    time.sleep(2)
    return '世界'

if __name__ == '__main__':
    # pool = ThreadPoolExecutor(5)  # 开启固定数量的线程，如果不指定，默认数量为cpu数 * 5 的个数
    pool = ProcessPoolExecutor(5)  # 开启固定数量的进程，如果不指定，默认数量为cpu数
    l = []
    for i in range(20):
        res = pool.submit(task,i)  # 提交任务
        print(res)  # 这里的res返回一个执行对象
        # print(res.result)  # 调用对象下的result方法可以得到提交的任务的执行结果
        l.append(res)
        '''
        线程池执行的任务都是异步并发的，但想要得到方法的返回结果，必然得等到任务执行结束之后。
        这就会导致一个问题，那就是原本并发的程序会变成串行。于是和线程利用列表和join方法，保证
        所有线程都启用后，才逐一调用方法
        '''
    for res in l:
        print(res.result())
        '''
        但这也不是最优解，它任然有导致串行的可能
        这里用到异步回调机制.add_done_callback()方法，当执行的任务返回结果时，会将返回的结果当作参数
        传给callback中的回调函数作为参数，res最总会拿到回调函数处理的结果
        '''
        res = pool.submit(task,1).add_done_callback(roll_back)
        pool.shutdown()
