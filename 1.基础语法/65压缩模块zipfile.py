# ### zipfile 压缩模块 (zip)
import zipfile
# 1 压缩文件
# 打开文件
zf = zipfile,ZipFile('ceshi.zip','w',zipfile.ZIP_DEFLATED)
# 写入内容 write(路径,别名)
zf.write('/bin/bzmore','bzmore')
zf.write('/bin/cat','cat')
# 创建一个临时文件 叫tmp,在tmp文件夹中放入chac1文件
zf.write('/bin/chac1','tmp/chac1')
# 关闭文件
zf.close()

# 2 解压文件
# 打开文件
zf = zipfile.ZipFile('ceshi1.zip','r')
# 解压单个文件 extract(文件名,路径)
zf.extract('bzmore','ceshi1')
# 解压缩有文件
zf.extractall('ceshi2')
# 关闭文件
zf.close()

# 3 追加文件 [支持with语法]
with zipfile.ZipFile('ceshi1.zip','a',zipfile.ZIP_DEFLATED) as zf:
	zf.write('/bin/chmod','chmod')

# 4 查看压缩包中的内容
with zipfile.ZipFile('ceshi1.zip','r') as zf:
	lst = zf.namelist()
	print(lst)





