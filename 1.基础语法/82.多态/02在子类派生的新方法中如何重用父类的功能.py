# 方式1：指名道姓调用某一个类下的函数=》不依赖于继承关系
class OldboyPeople:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def f1(self):
        print('{} say hello'.format(self.name))

# class Teacher(OldboyPeople):
#     def __init__(self,name,age,sex,salary,level):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.salary = salary
#         self.level = level

# 方式2
# 调用super()会得到一个特殊的对象，该对象会参照发起属性查找类的mro，去当前类的父类中找属性和方法
class Teacher(OldboyPeople):
    def __init__(self,name,age,sex,salary,level):
        super().__init__(name,age,sex) # 调用的是方法，自动传入对象
        self.salary = salary
        self.level = level

# super案例
class A:
    def test(self):
        super().test()

class B:
    def test(self):
        print("from B")

class C(A,B):
    pass

c = C()
c.test()