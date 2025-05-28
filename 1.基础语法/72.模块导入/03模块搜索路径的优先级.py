# 无论是import还是from...import在导入模块时都涉及到查找问题
# 优先级：
# 1、内存（内存模块）
# 2、从硬盘找（按照sys.path中存放的文件的顺序依次查找要导入的模块）

import sys
# 值为一个列表，存放了一系列文件夹
# 其中第一个是当前这姓文件所在的文件夹
print(sys.path)

# 了解：sys.modules查看已经加载到内存的模块
# import poo
# del poo无法解除poo与该内存地址的绑定关系

# def func():
#     import poo
# func()
# func()结束调用也无法接触绑定关系

# 利用sys.path把模块位置添加到收索例表中