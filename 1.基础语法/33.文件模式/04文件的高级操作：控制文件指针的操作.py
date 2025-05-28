# 指针移动的单位都是以bytes/字节为单位
# 只有一种情况特殊：
#       t模式下的read(n),n代表的是字符个数

# with open('a',mode='rt',encoding='utf-8') as fp:
#     res = fp.read(4)
#     print(res)

# f.seek(n,模式):n指的是移动的字节个数
# 模式：
# 0：参照物是文件开头的位置
# fp.seek(9,0)
# fp.seek(3,0)
# 1：参照物是当前指针所在位置
# fp.seek(9,1)
# fp.seek(3,1)
# 2：参照物是文件末尾位置，应该倒着移动
# fp.seek(-9,2)
# fp.seek(-3,2)

# 强调：只有0模式可以在t下使用，1、2必须在b模式下使用

# fp.tell() # 获取文件指针当前位置
# 示范
with open('a', mode='rb') as fp:
    fp.seek(6)
    res = fp.read()
    print(res.decode('utf-8'))
