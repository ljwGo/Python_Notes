# 1、打开文件
# windows路径分隔符问题
# open('D:\a\nb\c\d.txt')
# 解决方案一：推荐
# open(r'D:\a\nb\c\d.txt')
# 解决方案二：
# open('D:/a/nb/c/d.txt')

# 绝对路径
# open('/Users/linux')
# 相对路径

# f=open(r'aaa/aaa.txt',  mode='rt') # f的值是一种变量，占用的是应用空间和操作系统的空间
# print(f)

# 2、操作文件：读/写文件，应用程序对文件的读写请求都是在向操作系统发送系统调用，然后由操作系统控制硬盘输入读入内存、或者写入到硬盘
# res = f.read()
# print(res)

# 3、关闭文件
# f.close() # 回收操作系统资源
# f.read() # 变量f存在，但是不能再读了
# del f # 回收应用程序资源