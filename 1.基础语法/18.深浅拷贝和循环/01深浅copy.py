# list1 = [
#     'egon',
#     'lxx',
#     20
# ]
# # 二者分隔不开，list改数据list2也跟之改，因为指向的就是同一个列表的内存地址
# list2 = list1 # 这不叫拷贝

# 需求
# 1、拷贝一个列表产生新列表
# 2、想让两个两个列表完全独立开，针对的是改操作的独立而不是读操作


# 3、 如何拷贝列表
# 3、1 浅拷贝：是把原列表第一层的内存地址直接复制一份交给另一个新的容器（新的内存地址）
list1 = [
    'egon',
    'lxx',
    [1,2]
]
# list2 = list1.copy()
# print(id(list1), id(list2))
#
# list1[0] = 'Egon'
# list1[1] = 'Lxx'
# list1[2] = '222'
# print(list1,list2)
#
# list1[2][0] = 111
# list1[2][1] = 222
# print(list1,list2)

import copy
list3 = copy.deepcopy(list1)
list2 = list1.copy()
list1[0] = 'EGON'
list1[1] = 'LXX'
list1[2][0] = '111'
print(list1,list2,list3)