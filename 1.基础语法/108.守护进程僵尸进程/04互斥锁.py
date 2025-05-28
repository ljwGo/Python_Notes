from multiprocessing import Process, Lock
import json
import random
import time

def search(name):
    # 文件操作读取票数
    with open('data',mode='r',encoding='utf-8') as f:
        dic = json.load(f)
    ticket_num = dic.get('ticket_num')
    print('用户{}查询余票:{}'.format(name,ticket_num))
    return ticket_num,dic

def buy(name,lock):
    lock.acquire()
    ticket_num, dic = search(name)
    time.sleep(random.randrange(1,4))
    if ticket_num > 0:
        ticket_num -= 1
        dic['ticket_num'] = ticket_num
        with open('data', mode='w', encoding='utf-8') as f2:
            json.dump(dic,f2)
        print('{}购票成功'.format(name))
    else:
        print('{}购票失败'.format(name))
    lock.release()

if __name__ == '__main__':
    # 在主进程中生成一把锁
    lock = Lock()
    for i in range(1,11):
        p = Process(target=buy,args=(i,lock))
        p.start()