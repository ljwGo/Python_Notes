import os

# 获取某一个文件夹下所有的子文件以及文件夹的名字
res = os.listdir('.')
print(res)

# 获取文件夹大小
res2 = os.path.getsize('.')
print(res2)

# os.remove() # 删除文件夹
# os.rename() # 重命名文件夹

os.system(r'dir C:')

# 规定：key与value必须都是字符串
print(os.environ)

os.path.dirname(r'/a/b/c/d.txt')  # 处理字符串获取文件夹名
os.path.basename(r'/a/b/c/d.txt')  # 处理字符串获取文件名

os.path.isfile(r'/a/b/c/d.txt')  # 判断文件是否存在
os.path.isdir(r'/a/b/c/d.txt')  # 判断文件夹是否存在

print(os.path.join('/', 'a', 'b', ))

# 在python3.5之后，推出了一个新的模块pathlib
from pathlib import Path
root = Path(__file__)
res = root.parent.parent
print(res)

res = Path('/a/b/c') / 'd/e.txt'
print(res)