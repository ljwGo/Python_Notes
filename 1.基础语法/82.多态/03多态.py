# 1、什么是多态：同一事物有多种形态
class Animal:
    def say(self):
        print('')

class People(Animal):
    pass

class Dog(Animal):
    pass

class Pig(Animal):
    pass

# 2、为何要有多态=》多态会带来什么样的特性，多态性
#    多态性指的是在可以在不考虑对象具体类型的情况下直接使用对象
print('hello'.__len__()) # 'hello' => str('hello')
print(['1',2,3].__len__())
print({'a':2,'b':4}.__len__())

def my_len(obj):
    return obj.__len__()

# 鸭子类型
# python中不推荐使用父类设置多个类的共有方法
# 而是使用将多个类设定得大致相同，如linux系统的万物皆文件
class Cpu:
    def read(self):
        pass
    def write(self):
        pass

class Mem:
    def read(self):
        pass
    def write(self):
        pass

class Txt:
    def read(self):
        pass
    def write(self):
        pass