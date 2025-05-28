# import 导入模块在使用时候的优缺点
# 优点：肯定不会与当前名称空间中的名字冲突
# 缺点：必须加前缀=》模块名.

# from ... import ...导入也发生了三件事
# 1、产生一个模块的名称空间
# 2、运行m.py将运行过程中产生的名字都丢到模块的名称空间取
# 3、在当前名称空间拿到一个名字，该名字与模块名称空间中的某一个
from m import x
from m import get
from m import chance

x = 3333
get()
chance()
get()

# from ... import ...导入模块在使用时不用加前缀
# 优点：代码更精简
# 缺点：容易与当前名称空间混淆