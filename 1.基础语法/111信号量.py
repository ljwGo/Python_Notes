# ### 信号量 Semaphore 本质上就是锁,同一时间可以上多把锁
"""
# 语法：
    sem = Semaphore(3)
    sem.acquire()
    sem.release()
"""
'''
import time
import random
from multiprocessing import Process,Semaphore
def ktv(person,sem):
    sem.acquire()
    print('%s在唱歌' % (person))
    time.sleep(random.randrange(3,6))
    print('%s离开了' % (person))
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(3)
    for i in range(10):
        p = Process(target=ktv,args=('person%s' % (i),sem))
        p.start()
'''
'''
lock 多个进程之间，一次只能上一把锁
Semaphore 多个进程之间，可以自定义上锁的数量，不限于一个
'''

# ### 事件(event)
from multiprocessing import Event
'''
# 阻塞事件：
    e = Event()生成事件对象





'''
# 1 基本语法
'''
e = Event()
print(e.is_set())
e.wait()
print('123456')

# 2
e = Event()
e.set()
e.wait()
print('33334444')

# 3 # 代表最大等待事件是2秒，过了2秒之后从阻塞改为放行
e = Event()
e.wait(2)
print(77778888)

# 4
e.clear() # 把is_set()从True改为False
e.wait()
print(55556666)
'''

# 3 模拟红绿灯效果
import time
def traffic_light(e):
    while True:
        if e.is_set():
            time.sleep(3)
            print('红灯亮')
            e.clear()
        else:
            # 让红灯亮一秒
            time.sleep(1)
            # 切换成绿灯
            print('绿灯亮')
            # 把默认值从False 改成True
            e.set()

e = Event()
traffic_light(e)


