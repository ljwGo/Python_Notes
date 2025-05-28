'''
t：
    1、读写都是以字符串（unicode）为单位
    2、只针对文本文件
    3、必须指定字符编码
b：binary模式
    硬盘的二进制读入内存-》b模式下，不做任何转换，直接读入内存
    1、读写都是以bytes为单位
    2、可以针对所有文件类型
    3、一定不能指定字符编码
总结：
    b模式更通用

循环读取文件
方式一：
with open('文件名',mode='rb') as fp:
    while True:
        res = fp.read(1024)
        if len(res) == 0: # if not res:
            break
        print(len(res))

方式二：
with open('文件名',mode='rb') as fp:
    for line in fp:
        fp.read(line)
'''
