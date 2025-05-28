# 装饰器是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加新功能
# 新功能的可调用对象
# print(property)

# property是一个装饰器，用来绑定给对象的方法伪装成属性
class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height**2)


obj1 = People('egon', 70, 1.80)
# res = obj1.bmi()
# print(res)

print(obj1.bmi)

# 案例二：
class People:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self,val):
        if type(val) is not str:
            print('必须传入str类型')
        else:
            self.__name = val

    def del_name(self):
        print('不让删除')

    name = property(get_name,set_name,del_name)

obj2 = People('egon')
# print(obj2.get_name())
# print(obj2.set_name('Egon'))
# obj2.del_name()

# 正常人的思维
print(obj2.name)

class People:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        if type(val) is not str:
            print('必须传入str类型')
        else:
            self.__name = val

    @name.deleter
    def name(self):
        print('不让删除')