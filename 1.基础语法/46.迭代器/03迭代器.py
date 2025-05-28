'''
1、什么是迭代器
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于
    上一次结果进而继续的，单纯的重复并不是迭代

2、为何要有迭代器
    迭代器是用来迭代取值的工具
    l=['egon','lxx','alex']
    i = 0
    while i < len(l):
        print(l[i])
        i+=1
    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、元组
    为了解决索引迭代取值的局限性
    python必须提供一种能够不依赖于索引的取值方式，这就是迭代器

3、如何用迭代器
'''

# 可迭代对象：但凡有有__iter__方法都称之为可迭代对象
# 调用可迭代对象下的__iter__方法会将其转换成迭代器对象
d = {'a':2,'b':3,'c':'ee'}
d_iterator = d.__iter__()
print(d_iterator)

d_iterator.__next__()
d_iterator.__next__()
d_iterator.__next__()
# d_iterator.__next__() # 抛出异常StopIteration

# 利用while遍历字典
d_iterator = d.__iter__()
while True:
    try:
        print(d_iterator.__next__())
    except StopIteration:
        break

# 3、可迭代对象与迭代器对象详解
# 3.1可迭代对象（"可以转换成迭代器的对象"）：内置有__iter__方法的对象
#       可迭代对象.__iter__():得到迭代器对象

# 3.2迭代器对象：内置有__next__方法并且内置有__iter__方法的对象
#       迭代器对象.__next__():得到迭代器的值
#       迭代器对象.__iter__():得到迭代器对象，说白了跟没调一样，目的是为了统一for循环调用的方式

# for循环的工作原理
# 1、d.__iter__()得到一个迭代器对象
# 2、迭代器对象.__next__()拿到一个返回值并赋值给变量名
# 3、循环往复步骤2，直到抛出异常StopIteration后结束循环

# 迭代器优缺点总结
