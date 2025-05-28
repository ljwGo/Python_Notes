# ### os模块 (具有新建和删除功能) 与 shutil模块 (复制和移动)
import os
os.chdir('/home/laijianwei/mywork')
# os.mknod 创建文件
os.mknod('ceshi11.txt')
# os.remove 删除文件
os.remove('ceshi11.txt')
# os.mkdir 创建文件夹
os.mkdir('ceshi222')
# os.rmdir 删除目录
os.rmdir('ceshi222')
# os.makedirs 递归创建文件夹
os.makedirs('a/b/c/d/f')
# os.removedirs 递归删除文件夹 (空文件夹)
os.removedirs('a/b/c/d/f')

# ### shutil
import shutil

# 1 单纯仅仅复制文件内容
# copyfileobj(fsrc,fdst[,length=16*1024]) 复制文件 (length的单位是字符(表达一次读多少字符)
fp1 = open('ceshi.py',mode='r',encoding='utf-8')
fp2 = open('ceshi2.py',mode='w',encoding='utf-8')
shutil.copyfileobj(fp1,fp2)

# copyfile(src,dst) # 单纯的仅复制文件内容,底层调用了copyfileobj
shutil.copyfile('ceshi101.py','ceshi102.py')

# copymode(src,dst) 单纯仅仅复制文件的权限
shutil.copymode('ceshi102.py','ceshi103.py')

# copystat(src,dst) 复制文件的所有信息,包括权限,组,用户,修改时间等,不包括内容
shutil.copystat('ceshi102.py','104.py')

# 3 文件内容 + 文件权限
# copy(src,dst) # 复制文件权限和内容
shutil.copy('ceshi102.py','105.py')

# copy2(src,dst) # 复制文件的权限和内容,还包括权限,时间等
shutil.copy2('ceshi102.py','106.py')

# copytree(src,dst) # 拷贝文件夹里面的所有内容(递归拷贝)
shutil.copytree('ceshi100','ceshi1000')

# rmtree(path) # 删除当前文件夹及其中所有内容(递归删除)
shutil.rmtree('ceshi1000')

# move(path1,path2) # 移动文件或者文件夹
# 移动文件夹
shutil.move('ceshi1000','../ceshi2000')
# 移动文件
shutil.move('104.py','111.py')







