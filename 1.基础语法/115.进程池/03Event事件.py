from threading import Thread, Event
import time

event = Event()

def traffic_light():
    print('红灯亮了')
    print(event.is_set())  # 打印_flag当前的值
    time.sleep(8)
    print('绿灯亮了')
    event.set()  # 设置_flag为True
    print(event.is_set())  # 打印_flag当前的值

def car(i):
    print('{}车在等待'.format(i))
    event.wait()  # 执行到这里，判断_flag的值，False时阻塞；True时同行
    print('{}车开了'.format(i))

if __name__ == '__main__':
    t2 = Thread(target=traffic_light)
    t2.start()
    for i in range(1,10):
        t = Thread(target=car,args=(i,))
        t.start()

event.clear()  # 设置_flag为False