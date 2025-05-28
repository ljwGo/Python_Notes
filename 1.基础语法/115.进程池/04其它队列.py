# 堆栈队列
import queue

# 堆栈队列：后进先出
q = queue.LifoQueue(4)

q.put(11)
q.put(22)
q.put(33)
q.put(44)
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# 优先级队列
q = queue.PriorityQueue(4)

q.put((22,'wwww'))
q.put((-2,'eeee'))
q.put((222,'qqqq'))
print(q.get())
print(q.get())
print(q.get())
''' 优先级队列put方法要传入一个元组，该元组第一个值表示数据提取的优先级，可以为负数，且数字越小，优先级越高'''