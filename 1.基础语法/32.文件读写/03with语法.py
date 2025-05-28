# 文件对象又称之为文件句柄
with open('笔记', mode='rt', encoding='utf-8') as f1,\
        open('b', mode='rt', encoding='utf-8') as f2:
    res = f1.read()
    print(res)
# with语法可以打开多个文件，同时可以使用\将换行符转义