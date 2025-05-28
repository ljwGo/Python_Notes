# 引入：
# 一切都源于一句话：一切皆为对象

# 什么是元类？
# 元类就是用来实例化产生类的类
# 关系：元类--------实例化--------类--------实例化--------对象
# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def see(self):
#         print('{}的年龄是{}'.format(self.name,self.age))

# 如何得到对象
# obj=调用类()
# obj = People('egon',18)
# print(type(obj))

# 如果说类也是对象
# 查看内置的元类
# print(type(People))
# print(type(int))
# 一切自定义以及内置的类都是由type元类实例化得到的

# class产生类的过程
# 类有三大特征：
# 1、类名
# class_name = "People"
# 2、类的基类
# class_bases = (object,)
# 3、执行类体代码拿到类的名称空间
# class_dic={}
# class_body="""
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# def see(self):
#     print('{}的年龄是{}'.format(self.name,self.age))
# """
# exec(class_body,{},class_dic)
# print(class_dic)


#exec：三个参数

#参数一：包含一系列python代码的字符串

#参数二：全局作用域（字典形式），如果不指定，默认为globals()

#参数三：局部作用域（字典形式），如果不指定，默认为locals()

#可以把exec命令的执行当成是一个函数的执行，会将执行期间产生的名字存放于局部名称空间中
# g={
#     'x':1,
#     'y':2
# }
# l={}
#
# exec('''
# global x,z
# x=100
# z=200
#
# m=300
# ''',g,l)
#
# print(g) #{'x': 100, 'y': 2,'z':200,......}
# print(l) #{'m': 300}



# 4、调用元类
# People=type(class_name,class_bases,class_dic)

# 四、如何自定义元类来控制类的产生
# class Mymeta(type): # 只有继承了type类的类才是元类
#     def __init__(cls,class_name,class_bases,class_dic):
#         super().__init__(class_name,class_bases,class_dic)
#         print('run from __init__')
#         print(cls)
#         print(cls.__doc__)
#         if not cls.__doc__:
#             raise NameError('必须写注释')
#         print(class_name)
#         print(class_bases)
#         print(class_dic)
#
#     # __new__发生在__init__之前，用于造一个空对象，返回值必须是对象
#     def __new__(cls, *args, **kwargs):
#         print('run from __new__')
#         print(cls,*args,**kwargs)
#         return super().__new__(cls, *args, **kwargs)

# 调用Mymeta发生了三件事,调用Mymeta即调用Mymeta中的type.__call__
# 1、先造一个空对象=>Student,其实是调用了类内的__new__方法
# 2、调用Mymeta这个类内__init__方法，完成初始化对象的操作
# 3、返回初始化好的对象

# class Student(object,metaclass=Mymeta):
#     '''
#     类的注释
#     '''
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# 五：__call__：调用类或对象时，它的基类中的__call__会被调用
# class Foo:
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print('你好')
#         return 23333
#
# obj = Foo()
# res = obj()
# print(res)

# 六、利用元类为自定义元类的类生成对象的过程展示
# 自定义元类（必须继承type）
class Mymeta(type):
    def __call__(cls,*args,**kwargs):
        obj = cls.__new__(cls,*args,**kwargs)
        obj.__init__(*args,**kwargs)
        return obj

class School(metaclass=Mymeta):
    def __init__(self,name):
        self.name = name

    def show(self):
        print('学校名称是{}'.format(self.name))

# 实例化对象
obj2 = School('oldboy')
print(obj2)
# 第一步：
#       School加括号调用，会先触发（以School为基准，谁调用谁为基准）
#       找它的上一层自动触发__call__类代运行（此处为Mymeta）,
#       并将调用的 类 和 括号内的实参 自动传入
# 第二步：
#       在__call__内部调用__new__()方法产生一个空白对象，
#       参数不会自动传入，
#       第一个参数是调用的 类 ，并将其它实参也传入，得到这个类的空白对象
# 第三步：
#       调用__init__()方法，为空白对象初始化独有的属性值（个性）,
#       参数会自动传入，
#       直到这一步其它实参才能赋值给对象实行，实参传递结束
# 第四步：
#       __call__将得到的 类 的对象返回
