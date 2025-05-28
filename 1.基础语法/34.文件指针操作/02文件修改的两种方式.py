# 方式一：文本编辑采用的就是这种方式
with open('a', mode='r', encoding='utf-8') as fp:
    res = fp.read()
    data = res.replace('alex', 'egon')

with open('a', mode='w', encoding='utf-8') as fp:
    fp.write(data)

# 方式二:
import os
with open('a',mode='r',encoding='utf-8') as fp2,\
    open('.a.swap', mode='wt', encoding='utf-8') as fp3:
    for line in fp2:
        res = line.replace('alex', 'egon')
        fp3.write(res)
os.remove('a')
os.rename('.a.swap', 'a')