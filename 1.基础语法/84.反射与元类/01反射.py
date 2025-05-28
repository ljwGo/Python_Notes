# 什么是反射？
# 指的是在程序运行过程中可以"动态"获取对象的属性和方法

# 为何要用反射？

# 怎么用反射？
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def see(self):
        print('{}的年龄是{}'.format(self.name,self.age))

obj = People('egon',18)

# 1、查看某一个对象下可以通过.的方式得到的属性名来
print(obj.__dict__)
print(dir(obj))

# 2、可以通过字符串反射到真正的属性上，得到属性值
# obj.'name'
print(obj.__dict__[dir(obj)[-2]])

# 四个内置函数的使用
# hasattr()
print(hasattr(obj,'name'))
print(hasattr(obj,'x'))

# getattr() # (obj,属性名，默认属性)
# 默认属性：当getattr得不到obj下的属性值，则获取默认属性
print(getattr(obj,'name'))

# setattr()
setattr(obj,'name','Egon') # obj.name = Egon

# delattr()
delattr(obj,'name') # del obj.name

obj2 = 10
print(getattr(obj2,'x',1111)) # print(obj2.x = 1111)
print(getattr(obj2,'x')) # print(obj2.x)
