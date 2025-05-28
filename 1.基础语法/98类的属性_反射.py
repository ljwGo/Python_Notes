# ### 于类相关的魔术方法
class Man():
	pass

class Woman():
	pass

class Children(Man,Woman):
	'''啦啦啦'''
	eye = '天蓝色'
	skin = '天蓝色'

	def eat(self):
		print('小孩就会吃奶奶')

	def cry(self,func):
		print('小孩会哭,地动山摇')
		print(func.__name__)

	def __sleep(self):
		print('小孩睡觉的时候,不喜欢别人干扰他')

obj = Children()
# __dict__ 获取类的内部成员结构
# 对象
res = obj.__dict__
print(res)
# 类
res = Children.__dict__
print(res)

# __doc__ 获取对象或者类的内部文档
print(Children.__doc__)

# __name__ 获取类名函数名
def abc():
	pass
	#print('abc')
obj.cry(abc)

# __class__ 获取当前对象所属的类
res = obj.__class__

# __bases__ 获取一个类直接继承的所有父类,返回元祖

# ### 2 反射
# 通过字符串去操作类对象 或者 模块中的属性方法

# 1 类中的反射
# hasattr() 检测对象/类是否有指定的成员
# 对象
res = hasattr(obj,'eye')
print(res)
# 类
res = hasattr(Children,'skin')
print(res)

# getattr() 获取对象/类成员的值
# 对象
res = getattr(obj,'eye')
print(res)
# 通过对象把方法反射出来,是绑定方法
func = getattr(obj,'eat')
func()
# 通过类把方法反射出来,是普通方法
func = getattr(Children,'eat')
func(1)
# 可以为getattr设置默认值,如果找不到该成员,在第三个参数上可以设置相应的返回值
res = getattr(Children,'abc','没有')
print(res)

strvar = input('请输入你要操作的成员:')
if hasattr(obj,strvar):
	func = getattr(obj,strvar)
	func()
else:
	print('对不起,没有该成员')

# 3 setattr() 设置对象/类成员的值
# 对象
setattr(obj,'hair','天蓝色')
print(obj.hair)

# 类
setattr(Children,'age',5)
print(Children,'age',lambda : print('aaaa'))
Children.age()

# 4 delattr() 删除对象/类成员的值
# 对象
delattr(obj,'hair')
# 类
delattr(Children,'age')

# 2 模块的反射
import sys
# sys.modules 返回的是一个系统字典,字典的键是加载的所有模块
print(sys.modules)
mymodule = sys.modules['__main__']
print(mymodule)

def func2():
	print(2)

# 通过字符串来操作模块中的成员
if hasattr(mymodule,func):
	# 反射真实的函数
	func1 = getattr(mymodule,func)
	func1()
else:
	print('这个函数不存在')





