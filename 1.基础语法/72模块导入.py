# ### 模块和包的导入
'''
# 文件就是一个模块,文件夹就是一个包
# 文件夹里面可以有很多文件,就相当于包中有好多的模块
'''
# import
'''导入一次,终身受益,重复导入也只是导入一次'''
'''
import mymodule
import mymodule
print(mymodule.xboy)

# part1
# 模块.变量
print(mymodule.xboy)
# 模块.函数
mymodule.cat()
# 模块.类
print(mymodule.School().name)
'''
# part2 模块的改名
import mymodule as md
# 模块.变量
print(md.xboy)
# 模块.函数
md.cat()
# 模块.类
print(md.School().name)

# part3 导入任意路径下的模块
# sys.path 返回系统环境变量路径
import sys
print(sys.path)
'''
[windows]
['D:\\systemios\\showtogether',
'C:\\Users\\Administrator\\Desktop',
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32', 
'C:\\Users\\Administrator\\Desktop\\venv', 
'C:\\Users\\Administrator\\Desktop\\venv\\lib\\site-packages']
'''

#sys.path.append(r'D:\shoutogether')
#import ceshi
#print(ceshi.a)

# part4
# from ... import ... 从哪里导入什么什么东西
# 导入一个
from functools import reduce
from mymodule import xboy
print(xboy)
# 导入所有 *
from mymodule import *
print(xboy)
# 精准导入并改名
from mymodule import xboy as b , xgirl as g
print(g)

# part5 返回模块名字的魔术属性 __name__
'''__doc__
__next__() 方法
__file__ 属性'''
'''
如果文件是直接执行的,就是主文件(主进程),返回__main__
如果当前文件是间接执行的,就是子文件(子进程),返回当前文件名(模块名)
'''
print(__name__)

