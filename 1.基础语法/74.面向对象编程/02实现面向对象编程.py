# 先定义类（类是对象相似数据与功能的集合体）
# 注意：类体代码是在类定义阶段就会立即执行的，会产生类的名称空间（局部空间）

# 命名方式
# class 加驼峰体:

# 1、变量的定义(数据属性)
# print(Student.stu_school) => Student.__dict__['stu_school']
# 2、功能的定义(函数属性)

# 再调用类产生对象
# obj = 类名()

# print(obj.__dict__)

class Student:
    name = 'egon'
    age = 18
    gender = 'male'

    def check_info(self):
        pass


print(Student.__dict__)
# Student.__dict__['gander'] = 'male'
# Student.__dict__.update({'gander':'male'})
print(Student.__dict__)

obj = Student()
print(obj.__dict__)
obj.__dict__['hobby'] = 'ball'
print(obj.__dict__)


# 方法一
def init(obj, x, y, z):
    obj.name = x
    obj.age = y
    obj.gender = z


stu_obj = Student()
init(stu_obj, 'laijianwei', 20, 'male')
print(stu_obj.__dict__)

# 调用类的过程又称之为实例化，发生了三件事
# 1、先产生一个空对象
# 2、python会自动调用类中__init__方法将空对象和类括号参数传给__init__方法
# 3、返回初始化的对象

# 总结__init__方法
# 1、会在调用类时自动触发执行，用来为对象初始化自己独有的数据
# 2、__init__内应该存放时为对象初始化属性的功能，但是可以存放任意其它代码，
#   想要在类调用时就立刻执行的代码都可以放到该方法内
# 3、__init__方法必须返回None
