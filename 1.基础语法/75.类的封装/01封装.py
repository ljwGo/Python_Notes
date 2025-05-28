# 一：封装时面向对象三大特征最核心的一个特性
# 封装<->整合

# 二：将封装的属性进行隐藏
# 1、如何隐藏：在属性名前面加__前缀,就实现一个对外隐藏属性效果
# python实现隐藏的方式是通过改名策略，将__变量名改为_类名__变量名
# 2、这种隐藏对外不对内,因为__开头的属性名会在检查类体代码语法时统一发生变形
# 3、这种变形操作只能在检查类体代码的时候发生一次，之后定义的__开头的属性不会发生变形

class Foo:
    __x = 1

    def __test(self):
        print('from test')

    def f2(self):
        print(self.__x)

print(Foo.__dict__)
# print(Foo.x)
# print(Foo._Foo__x)

# 三：为何要隐藏？
# 隐藏数据属性
class People:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        print(self.__name)

    def set_name(self,values):
        if values.isalnum():
            self.__name = values
        print('小垃圾，必须传字符串类型')

# 隐藏函数属性