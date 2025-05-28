# ### tarfile 压缩模块2 后缀为.tar 或 .tar.gz 或 .tar.bz2
# bz2 模式的压缩文件较小 根据电脑的不同会产生不同的结果

# 创建tar压缩包
# 1 创建压缩包
'''.tar的压缩包,只打包不压缩'''
tf = tarfile.open('ceshi0907.tar','w',encoding='utf-8')
# 2 写入文件到压缩包中
tf.add('/bin/ntfscmp','ntfscmp')
tf.add('/bin/openvt','openvt')
# 3 关闭压缩包
tf.close()

# 创建.tar.gz压缩包
tf = tarfile.open('ceshi0908.tar.gz','w:gz',encoding='utf-8')
# 2 写入文件到压缩包中
tf.add('/bin/ntfscmp','ntfscmp')
tf.add('/bin/openvt','openvt')
# 3 关闭压缩包
tf.close()

# 创建.tar.bz2压缩包
tf = tarfile.open('ceshi0909.tar.bz2','w:bz2',encoding='utf-8')
# 2 写入文件到压缩包中
tf.add('/bin/ntfscmp','ntfscmp')
tf.add('/bin/openvt','openvt')
# 3 关闭压缩包
tf.close()

# 解压压缩包
tf = tarfile.open('ceshi0907.tar','r',encoding='utf-8')
# extract(文件,路径)
tf.extract('ntfscmp','ceshi1030')
# extractall(路径)
tf.extractall('ceshi3000')
# 3 关闭压缩包
tf.close()

# 追加模式 支持with语法 只能是对只打包不压缩的包进行追加,其他的模式不可以
with tarfile.open('ceshi0908.tar.gz','a',encoding='utf-8') as tf:
	tf.add('/bin/gzip','gzip')

# 查看压缩包中的内容
with tarfile.open('ceshi0908.tar.gz','r',encoding='utf-8') as tf:
	lst = tf.getnames()
	print(lst)

# ### 如何解决tarfile中存在的缺陷(不能追加文件到已经压缩的包)
'''
1 先解压缩有文件到文件夹
2 把想要追加的内容复制到文件夹中
3 经过过滤筛选,重新打包压缩
'''
import os,tarfile
res = os.getcwd()
print(res)

# 压缩包路径
path1 = os.path.join(res,'ceshi1031.tar.bz2')
# 解压的路径
path2 = ps.path.join(res,'ceshi1031')

# 1 先解压缩有文件到文件夹
tf = tarfile.open(path1,'r',encoding='utf-8')
tf.extractall(path2)
tf.close()

# 2 把想要追加的内容复制到文件夹中
os.system('cp -a /bin/ip ' + path2)
# import shutil
# shutil.copy2('/bin/ip',path2)

# 3 经过过滤筛选,重新打包压缩
lst = os.listdir(path2)
with tarfile.open(path1,'w:bz2',encoding='utf-8') as tf:
	for i in lst:
		if i != 'openvt':
			# 拼接绝对路径
			pathnew = os.path.join(path2,i)
			# add(路径,别名)
			tf.add(pathnew,i)


