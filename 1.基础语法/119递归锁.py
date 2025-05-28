# ### 线程之间的数据隔离
from threading import Thread,local,currentThread

# 创建对象
loc = local()
# 为当前对象赋值
loc.val = 'main thread 目前下载进度为57%'
print(loc,loc.val)

def func2():
    # loc.val,currentThread().name 获取当前线程名
    print('%s 该数据归属于 %s' % (loc.val,currentThread().name))

# 另外一个子线程任务
def func1(speed):
    loc.val = speed
    func2()
t1 = Thread(target=func1,args=('下载进度%9',))
t1.setName('子线程1')
t1.start()

t2 = Thread(target=func1,args=('下载进程%19'))
t2.setName('子线程2')
t2.start()

'''
a = 10
def func():
    print(a)
def func2():
    a = 90
    func()
func2()
'''
