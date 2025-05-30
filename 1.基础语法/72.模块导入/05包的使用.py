'''
1、包就是一个含有__init__.py文件的文件夹

2、为何要有包
    包的本质是模块的一种形式，包是用来当作模块导入的
'''

#1、产生一个名称空间
#2、运行包下的__init__.py文件，将运行过程中产生的名字都丢到1的名称空间中
#3、在当前执行文件的名称空间中拿到一个名字mmm，mmm指向1的名称空间

# 绝对导入，以包的文件夹作为起始来进行导入
# from mmm.m1 import f1
# from mmm.m2 import f2
# from mmm.m3 import f3

# 环境变量是以执行文件为准的，所有被导入的模块下的环境变量都与执行文件一致
# __init__下导入其它子模块时，只能使用from...import...不能使用import

# 强调
# 1、导入时带点点左边边必须都是包
# 2、包A与包B下有同名空间，因为来自不同的名称空间

# 相对导入：仅限于包内使用，不能挎出包（包内模块之间的导入，推荐使用相对导入）
# . ：代表当前文件夹
# .. ：代表上一层文件夹