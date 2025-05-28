# class Mymeta_upper(type):
#     def __new__(cls,name,bases,attrs):
#         dic = {}
#         for k,v in attrs.items():
#             if not callable(v) and not k.endswith('__'):
#                 dic[k.upper()] = v
#             else:
#                 dic[k] = v
#         return type.__new__(cls,name,bases,dic)
#
#         # print(cls.__dict__)
#         # print(dir(cls))
#         # print(*args)
#
# # Student = Mymeta_upper(类名，类的基类，类的名称空间)
# class Student(metaclass=Mymeta_upper):
#     school = 'oldboy'
#
#     def __init__(self,name):
#         self.name = name
#
#     def show(self):
#         print('学生名字是{}'.format(self.name))
#
# print(Student.__dict__)


# class Mymeta_upper(type):
#     def __call__(cls,*args,**kwargs):
#         if args:
#             return TypeError('must be keyword argument')
#         obj = object.__new__(cls)
#         print(cls)
#         for k,v in kwargs.items():
#             obj.__dict__[k.upper()] = v
#         print(obj.__dict__)
#         return obj
#
# Student = Mymeta_upper(类名，类的基类，类的名称空间)
# obj = Student(name) # 调用Studnet类会触发器元类的__call__()方法
# class Student(metaclass=Mymeta_upper):
#     school = 'oldboy'
#     def show(self):
#         print('学生名字是{}'.format(self.NAME))
#
# obj = Student(name='nani')
# obj.show()


# class Mymeta_upper(type):
#     def __call__(cls,*args,**kwargs):
#         obj = cls.__new__(cls,*args,**kwargs)
#         obj.__init__(*args,**kwargs)
#         dic = {}
#         for k,v in obj.__dict__.items():
#             k = '_{}__{}'.format(cls.__name__,k)
#             dic[k] = v
#         obj.__dict__ = dic
#         return obj
#
# class Student(metaclass=Mymeta_upper):
#     school = 'oldboy'
#
#     def __init__(self,name):
#         self.name = name
#
#     def show(self):
#         print('学生名字是{}'.format(self.name))
#
# obj = Student('egon')
# print(obj._Student__name)