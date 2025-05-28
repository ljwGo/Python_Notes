# 1、什么是继承
# 继承是一种创建类的方式，新建的类可以为子类或派生类，父类又可称为基类或超类。字类可以继承父类的属性和功能
# 需要注意的是：python支持多继承
#       在python中，新建的类可以继承一个或多个父类
#       优点：子类可以同时遗传多个父类的属性，最大限度地重用代码
#       缺点：
#           代码设计时会与人的逻辑冲突
#           代码的可读性会变差
#       不推荐使用多继承，拓展性变差，如果无法避免的要用多个父类的属性，应该使用Mixins

class Parent1:
    pass


class Parent2:
    pass


class Sub1(Parent1):  # 单进程
    pass


class Sub2(Parent1, Parent2):  # 多进程
    pass


# 在python2中有经典类与新式类之分
# 新式类：继承了object类的字类，以及该子类的子类子子类
# 经典类：没继承object类的字类，以及该子类的子类子子类

# 在python3中所有没有父类的类，默认以object为父类，所以python3中所有类都是新式类
print(Parent1.__bases__)


# 2、为何要用继承：用来解决类与类之间代码冗余问题

# 如何实现继承
# 代码之间存在冗余的代码
# class Student:
#     school = 'OLDBOY'
#
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def choose_course(self):
#         print('{}正在选课'.format(self.name))
#
# class Teacher():
#     school = 'OLDBOY'
#
#     def __init__(self,name,age,gander,salary,level):
#         self.name = name
#         self.age = age
#         self.gander = gander
#         self.salary = salary
#         self.level = level

# 优化
class OldboyPeople:
    school = 'OLDBOY'

    def __init__(self, name, age, gander):
        self.name = name
        self.age = age
        self.gander = gander


class Student(OldboyPeople):
    def choose_course(self):
        print('{}正在选课'.format(self.name))


class Teacher(OldboyPeople):
    def __init__(self, name, age, gander, salary, level):
        OldboyPeople.__init__(self, name, age, gander)
        self.salary = salary
        self.level = level

    def score(self):
        print('老师{}正在打分'.format(self.name))
