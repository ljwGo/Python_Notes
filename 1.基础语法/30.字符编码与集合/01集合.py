# 1、作用
# 1.1 关系运算
# friends1 = ['laijianwei','heen','liujiancheng','zhaoxujian']
# friends2 = ['zhangshan','lisi','laijianwei']
# l = []
# for x in friends1:
#     if x in friends2:
#         l.append(x)

# 2、定义：在{}内用逗号分隔开多个元素，多个元素满足以下三个条件
#   1.集合内元素必须为不可变类型
#   2.集合内元素无序
#   3.集合不重复

# 定义空集合
# setvar = set()

# 3、类型转换
res = set('hellollll')
print(res) # 去重

# 4、内置方法
friends1 = {'laijianwei','heen','liujiancheng','zhaoxujian'}
friends2 = {'zhangshan','lisi','laijianwei','heen'}

# 4.1 取交集：两者共同的好友
res = friends1 & friends2
# friends1.intersection(friends2)
print(res)

# 4.2 取并集：两者所有的好友
res2 = friends1 | friends2
# friends1.union(friends2)
print(res2)

# 4.3 取friends1独有的好友
res3 = friends1 - friends2
# friends1.difference(friends2)
print(res3)

# 4.4 取对称差集：求两个用户独有的好友们（即去掉共有的好友）
# friends1.symmetric_difference(friends2)
res4 = friends1 ^ friends2

# 4.5 父子集：包含的关系
s1 = {1,2,3}
s2 = {1,2,4}
# 不存在包含关系，下面比较均为False
print(s1 > s2)
s1.issuperset(s2)
print(s1 < s2)
s1.issubset(s2)

# 去重
# 1、只能针对不可变类型去重

# 2、无法保证原来的顺序

# 其他内置方法
# 需要掌握的操作是update、discard、add、pop
s = {1,2,3}
s.discard(1) # 删除元素不存在时不会报错

s.remove(2) # 删除元素不存在时，报错

s.update({2,3,4,5})

s.pop() # 随机删除

s.add(5) # 添加元素

# s.isdisjoint() 两个集合完全独立，没有公共部分，返回True
