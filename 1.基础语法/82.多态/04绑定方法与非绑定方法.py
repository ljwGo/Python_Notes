# 一：绑定方法：特殊之处在于将调用者本身当作第一个参数自动传入
#   1、绑定给对象的方法
#   2、绑定给类的方法（类来调用，并且自动传入类作为第一个参数）

import setting
class Mysql:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    def func(self):
        print('{}:{}'.format(self.ip,self.port))

    @classmethod # 将下面的函数装饰成绑定给类的方法
    def from_conf(cls):
        return cls(setting.IP,setting.PORT)

obj1 = Mysql('1.1.1.1',3306)
# 应用场景：提供一种全新的初始化类（使用配置文件中设置的数据初始化类）的方法

# 二：非绑定方法
# 给类中的不需要使用对象和类的方法使用
import uuid
class Student:
    def __init__(self):
        self.id = self.create_id()

    @staticmethod
    def create_id():
        return uuid.uuid4()
