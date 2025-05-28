# ### 生产者和消费者模型
'''
# 爬虫例子：
1号进程负责抓取网页当中的内容
2号进程负责匹配网页当中的关键字

1号进程可以理解为生产者
2号进程可以理解为消费者

理想的生产者和消费者模型：彼此运行的速度相当
从程序上来讲：
    生产者就是负责存储数据(put)
    消费者就是负责获取数据(get)
'''
# 1 基本语法
from multiprocessing import Process,Queue,JoinableQueue
'''
put
get
task_done 队列数据减一
join 阻塞

task_done 与 join 通过一个中间变量统计队列中元素个数
每放入一个值，成员中的中间变量值加一
每执行一次task_done,成员中的中间变量值减一
join根据中间变量值来确定是否阻塞
如果中间变量是0，意味这放行
如果中间变量不是0 意味这阻塞
'''
# 消费者
def poducer(jq,name,i):
    for i in range(1,1+i):
        print('%s在生产便便%d' % (name,i))
        jq.put('便便'+str(i))

def customer(jq,name):
    while True:
        good = jq.get()
        print('%s在消费%s' % (name,good))
        jq.task_done()

if __name__ == '__main__':
    jq = JoinableQueue()
    p1 = Process(target=poducer,args=(jq,'张三',5))
    p1.start()

    p2 = Process(target=customer,args=(jq,'李四'))
    p2.daemon = True
    p2.start()

    p1.join()
    jq.join()
    print('主进程结束')