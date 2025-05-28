from gevent import monkey
monkey.patch_all()
import socket
# 添加阻塞识别，只有有了这段代码，gevent才能自动识别代码阻塞，并跳转到其他代码
import gevent
import time

# 计算密集型程序下的切换
# 利用yield生成器函数实现阻塞切换
# def foo():
#     while 1:
#         1 * 1000
#         yield
#
# def func():
#     it = foo()
#     start_time = time.time()
#     for i in range(100000):
#         1 * 1000
#         next(it)
#     end_time = time.time()
#     print(end_time-start_time)  # 0.008974790573120117

# func()
#
# def func2():
#     start_time = time.time()
#     for i in range(200000):
#         1 * 1000
#     end_time = time.time()
#     print(end_time-start_time)  # 0.003989219665527344
#
#
# func2()
# 结论：纯计算密集型切换反而耗时

def talk(conn):
    while 1:
        try:
            print('这里运行了3')
            data = conn.recv(1024)
            if len(data):
                break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            conn.close()
            break

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    while 1:
        print('这里运行了2')
        conn, addr = server.accept()
        print('这里运行了1')
        gevent.spawn(talk,conn)

'''协程本身不存在，只是程序员创造出来的，利用携程就可以实现单线程下模拟并发效果'''
# 利用协程实现单线程下的并发效果

if __name__ == '__main__':
    g1 = gevent.spawn(run)
    g1.join()