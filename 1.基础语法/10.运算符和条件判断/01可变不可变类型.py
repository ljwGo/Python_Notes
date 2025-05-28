# 可变不可变类型

# 可变类型：值改变，id不变，证明改的是原值，证明原值是可以被改变的

# 不可变类型：值改变，id也改变了，证明是产生新的值，压根没有改变原值，证明原值是不可以被修改的

# 2、验证
# 2.1 int是不可变类型
x = 10
print(id(x))
x = 11
print(id(x))
# float,str,bool也是不可变类型

# list,dict是可变类型
# l = ['aaa','bbb','ccc']
# print(id(l))
# l[0] = 'AAA'
# print(id(l))

# 关于字典补充：
# 定义：{}内用逗号分隔开的多key：value
#       其中value可以是任意类型
#       但是key必须是不可变类型
