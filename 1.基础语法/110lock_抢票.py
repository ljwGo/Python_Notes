# ### lock(互斥锁)
'''
# 应用在多进程当中
# 互斥锁lock：互斥锁是进程间的相互排斥
进程之间，谁先抢占到资源，谁就先上锁，等到解锁之后，下一个进程再继续使用

# 语法：
    上锁 锁.acquire()
    解锁 锁.release()
'''
from multiprocessing import Process,Lock
import time

'''
lock = Lock()
# 上锁
lock.acquire()
print(1)
# 上锁和解锁是一对，如果只上锁不解锁，就会死锁
lock.release()
print(2)
'''

import json
# 2 模拟抢票
# 读取票数，更新票数
def wr_info(sign,dic=None):
    if sign == 'r':
        with open('ticket.txt',mode='r',encoding='utf-8') as fp:
            dic = json.load(fp)
        return dic

    elif sign == 'w':
        with open('ticket.txt',mode='w',encoding='utf-8') as fp:
            json.dump(dic,fp)

#wr_info('w',{'count':3})

# 抢票的方法
def get_ticket(person):
    # 读取数据库当中的实际票数
    dic = wr_info('r')

    time.sleep(0.1)# 防止数据错乱，造成报错，如果加锁了，会发生死锁
    if dic['count'] > 0:
        print('%s抢票成功' % (person))
        dic['count'] -= 1
        # 更新数据库
        wr_info('w',dic)
    else:
        print('%s抢票失败' % (person))

# 用ticket来进行函数的统一调用
def ticket(person,lock):
    # 查询票数
    dic = wr_info('r')
    print('%s 查询票数： %s' % (person,dic['count']))
    lock.acquire()
    get_ticket(person)
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=ticket,args=('张%s' % (i),lock))
        p.start()
'''
在创建进程时，是异步并发，在执行进程任务时，是同步上锁
哪个进程先抢到资源就先上锁，知道锁释放掉之后，下一个进程再上锁
'''