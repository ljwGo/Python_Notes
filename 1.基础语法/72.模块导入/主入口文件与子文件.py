print('m is pocessing')
def f1():
    print('from f1')

def f2():
    print('from f2')

print(__name__)
# 1、当m.py被运行时，__name__的值为'__main__'；当被当作模块导入时，__name__的值为当py文件的名字