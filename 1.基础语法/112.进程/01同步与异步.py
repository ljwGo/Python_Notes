import time
def func():
    time.sleep(3)
    print('hello world')

# 这是同步调用
if __name__ == '__main__':
    func()
    print('hahaha')