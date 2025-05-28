# ### os模块 -系统进行操作
# system() 在python中执行系统命令
import os
os.system('touch ceshi1028.txt')
os.system('rm -rf ceshi1028.txt')
'''
os.system('ipconfig')

#popen() 执行系统命令返回对象,通过read方法读出字符串
"""优点:在输入字符串时,可以优先转化成utf-8编码集"""
obj = os.popen('ipconfig')
print(obj)
res = obj.read()
print(res)
'''

# listdir() 获取指定文件中所有内容的名称列表
lst = os.listdir('.')
print(lst)

#getcwd() 获取当前文件所在的默认路径 /mnt/hgfs/showtogether
res = os.getcwd()
print(res)

# __file__  路径 + 文件名 /mnt/hgfs/showtogether/66os模块.py
print(__file__)


# chdir()  修改当前文件工作的默认路径
os.chdir('/home/laijianwei/mywork')
os.system('touch ceshi200.txt')

# environ 获取或修改环境变量
print(os.environ)
print(os.environ['Path'])
os.environ['Path'] += ':/homelaijianwei/mywork'
os.system('abc.sh')
'''
[linux] 通过python操作linux里面的脚本,要把脚本的路径添加到环境变量path路径中
	1 在/home/laijianwei/mywork 创建文件abc.sh
	2 在 abc.sh里 写入ifconfig这个命令
	3 修改abc.sh权限,改写777
	4 os.environ['Path'] += ':/homelaijianwei/mywork' 把脚本对应的路径添加到环境变量中
	5 python system这个命令执行 abc.sh 这个脚本

[windows] cmd中通过命令窗口调出qq窗口
	1 找到该文件的路径,右键属性找路径
	2 右键我的电脑 -> 高级系统设置 -> 系统变量Fath -> 新建把刚才的路径黏贴上去
	3 cmd -> 执行目标文件
'''

# os 属性模块
# name 获取系统标识 linux,mac -> posix      windows -> nt
print(os.name)

# sep 获取路径分割符号 linux,mac -> /      windows -> \
print(os.sep)

# linesep 获取系统的换行符号 linux,mac -> \n      windows -> \r\n 或 \n
print(os.linesep)