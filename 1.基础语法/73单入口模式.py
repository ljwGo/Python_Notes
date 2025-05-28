# ### 包的导入
'''
文件 -> 模块
文件夹 -> 包
在文件夹中有一个脚本__init__.py 作用:用来初始化包的脚本

import os # os是文件夹
os.listdir()
os.path.getsize()
'''
# 1
import package1
package1.mylistdir()

# 2 默认: 通过 文件夹.文件.函数()
import package1.mypath
package1.mypath.mypath()

# 3 借助在初始化脚本文件__init__中引入对应的mypath模块,间接导入mypath
import package1
package1.mypath.mypath()

# from .. import 导入包
# 导入单个
from package.mypath import m1
print(m1)
# 导入多个
from package1.mypath import m1 as a,m2 as b
# 导入所有
from package1.mypath import *

# ### 相对路径导入
import package2.path1.a1 as pp1
'''
所有的模块都通过main2.py这个单入口进行调用
分模块不会被单独执行,只能通过导入的方式
这种情况下用相对路径
如果文件中包含了相对路径,直接执行会报错
. 当前路径
..上一级路径
...上一级的上一级路径
以此类推
'''
# 单入口模式
'''
分模块不能单独进行调用,同益友文件main进行调用
模块之间的互相嵌套导入,使用相对路径实现
单入口文件必须和包在同一层级,包里面可以含有各种包和模块
'''

