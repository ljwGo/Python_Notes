# x = yield 返回值

def dog(name):
    print('狗哥{}准备出东西了'.format(name))
    while True:
        # x拿到的是yield接收到的值
        x = yield 'hooooo'
        print('狗哥{}吃了{}'.format(name,x))

# yield 的功能有两个：一个是返回值，并挂起；第二是接受send给的值，并将它赋值给变量名
g = dog('alex')
g.send(None) # 等同于next(g)
g.send('一根骨头')
# next(g)
# next(g)
g.close() # 可以关闭迭代器
# g.send(1,2)不能传两个值，但可以传列表等容器类型

# 二：
def my_g():
    ...