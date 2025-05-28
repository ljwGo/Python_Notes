from multiprocessing import Process
import time
def task(name):
    print('{}总管存活'.format(name))
    time.sleep(3)
    print('{}总管死亡'.format(name))

if __name__ == '__main__':
    p = Process(target=task,args=('egon',))
    p.daemon = 1
    p.start()
    print('皇帝jason驾崩')