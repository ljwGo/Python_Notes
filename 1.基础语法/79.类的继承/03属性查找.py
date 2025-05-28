# 单继承下的属性查找
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')

# obj = Bar()
# obj.f2()
#
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         Foo.f1(self)
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()

# class Foo:
#     def __f1(self): # _Foo__f1
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.__f1() # _Foo__f1
#
# class Bar(Foo):
#     def __f1(self): # _Bar__f1
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()