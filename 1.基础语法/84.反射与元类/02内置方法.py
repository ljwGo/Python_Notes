# 1、什么是内置方法？
# 定义在类内部，以__开头并以__结果的方法
# 特点：会在某种情况下自动触发

# 2、为何要用内置方法？
# 为了定制化我们的类or对象

# 3、如何使用内置方法
# __str__：在打印对象时会自动触发，然后将返回值（必须是字符串）当作本次打印的结果
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        print('运行了')
        return '哈哈哈哈{}'.format(self.name)

obj = People('egon',123)
print(obj) # => obj.__str__() => '哈哈哈哈'.__str__()

# __del__：在删除对象时触发,先执行该方法
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.x = open('a,txt',mode='w')
        # self.x 是占据操作系统的资源，而不是应用程序的资源，程序关闭时不会回收申请的操作系统资源

    def __del__(self):
        print('run....')
        # 发起系统调用，告诉操作系统回收相关的系统资源
        self.x.close()

obj = People('egon',18)
print('==============>')