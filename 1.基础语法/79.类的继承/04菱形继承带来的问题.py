# 类的多继承问题
# 菱形继承：由一个子类继承多个父类，多个父类最终汇聚到同一个非object的类的情形下就是菱形问题
class A:
    def text(self):
        print('from A')


class B(A):
    def text(self):
        print('from B')


class C(A):
    def text(self):
        print('from C')


class D(B, C):
    pass


print(D.mro())  # 类以及该类的对象访问属性都是参照该类的mro列表
obj = D()
obj.text()
# 总结：类相关的查找循序依照的是该类的mro列表下的循序
