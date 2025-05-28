import os
strvar = '/home/laijianwei/mywork/ceshi1.py'
# basename() 返回文件名
res = os.path.basename(strvar)
print(res)

# dirname() 返回路径部分
res = os.path.dirname()
print(res)

# split() 将路径拆分成单独的文件部分和路径部分 组合成一个元组
res = os.path.split(strvar)
print(res)

# join() 将多个路径文件组成新的路径 可以自动通过不同的系统添加不同的斜杠 linux/ windows\
path1 = 'home'
path2 = 'laijianwei'
path3 = 'mywork'

pathvar = path1 + os.sep + path2 + os.sep + path3
print(pathvar)

pathvar = os.path.join(path1,path2,path3)
print(pathvar)

# splitext() 将路径分割为后缀和其他部分
strvar = '/home/laijianwei/mywork/ceshi1.py'
res = os.path.splitext(strvar)
print(res)

# 用字符串中的split也可以分割出后缀部分
a,b = strvar.split('.')
print(a,b)

# getsize() 获取文件的大小
res = os.path.getsize('1,py')
print(res)

# isdir() 检测路径是否是一个文件夹
res = os.path.isdir('ceshi100')
print(res)

# isfile() 检测是否是一个文件
# islink() 检测路径是否是一个链接

# stat 获取linux文件的相关信息
# getctime() [windows]文件的创建时间,[linux]权限的改动时间(返回时间戳]
# getmtime() 获取文件最后一次修改的时间(返回时间戳)
# getatime() 获取文件最后一次访问的时间(返回时间戳)

# exists() 检测指定的路径是否存在
pathvar = '/home/laijianwei/mywork/2222.txt'
res = os.path.exists(pathvar)
print(res)

# isabs() 检测一个路径是否是绝对路径

# abspath() 将相对路径转化为绝对路径

# 结合使用
if not os.path.isabs(pathvar):
	pathnew = os.path.abspath(pathvar)
	print(pathnew)

# 如何计算一个文件夹中所有文件的大小
