# ### 如何计算一个文件夹中的所有文件大小
import os
#pathvar = '/mnt/hgfs/showtogether/ceshi3000.txt'
pathvar = '/mnt/hgfs/showtogether'
# 获取文件夹中所有的文件名称
lst = os.listdir(pathvar)
print(lst)
'''
拼接路径,计算文件大小
res = os.path.join(pathvar,'1.txt')
print(res)
res2 = os.path.getsize(res)
print(res2)
'''

# 我的方法
def dir_size(pathvar,total = 0):
	lst = os.listdir(pathvar)
	for i in lst:
		pathnew = os.path.join(pathvar,i)
		# 判断是否是文件
		if os.path.isfile(pathnew):
			print(i + '是文件')
			tatol += os.path.getsize(pathnew)
		# 判断是文件夹
		elif os.path.isdir(pathnew):
			print(i + '是文件夹')
			return dir_size(pathnew)
	return total

# 3 使用递归计算文件夹中所有文件的大小
# 老师的方法
def getallsize(pathvar):
	size = 0
	lst = os.listdir(pathvar)
	for i in lst:
		# 路径 + 文件名 => 绝对路径
		pathnew = os.path.join(pathvar,i)
		if os.path.isfile(pathnew):
			# 计算文件大小
			size += os.path.getsize(pathnew)
		elif os.path.isdir(pathnew):
			size += getallsize(pathnew)
	return size








