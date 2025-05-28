from multiprocessing import Queue

# 创建一个队列
q = Queue(5)  # 括号内可以加参数，参数表示的是数据存储的最大数量，默认值为0

# 往队列中存数据
q.put(1111)
q.put(1111)
q.put(1111)
q.put(1111)
q.put(1111)
# q.put(1111) # 当队列数据满了之后，如果还有数据要放，程序会发生阻塞，知道有位置让出来

'''存取数据 存是为了更好地取，千方百计地存，简单方便地取'''
# 队列中取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get()) # 队列中如果已经没有数据的话，get方法会原地阻塞
print(q.get(timeout=3)) # 队列中如果没有数据，会等待3秒，三秒之后仍然没拿到数据将会报错
print(q.get_nowait()) # 没有数据将会报错，但是不会阻塞

q.full() # 判断当前队列是否满了
q.empty() # 判断当前队列是否空了

'''q.full() q.empty() q.get_nowait() 再多进程的情况下是不精确的'''
