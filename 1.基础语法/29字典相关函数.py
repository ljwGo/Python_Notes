# ### 深拷贝 和 浅拷贝
a = 7
b = a
a = 8
print(b)
#输出结果为7

lst1 = [1,2,3]
lst2 = lst1
lst1.append(4)
print(lst2)
#输出类型为[1,2,3,4]

# 浅拷贝 copy模块中有一个同名方法也叫copy
import copy
# 方法一
lst1 = [1,2,3]
lst2 = copy.copy(lst1)
lst1.append(4)
print(lst2)

# 方法二
# 列表.copy
lst1 = [1,2,3]
lst2 = lst1.copy()
lst1.append(4)
print(lst1)
print(lst2)

# 深拷贝 copy模块中有一个方法叫deepcopy
'''
# 浅拷贝只能复制列表中的一级所有元素,二级或者多级中的元素无法复制,所以引出深拷贝
lst1 = [1,2,3,[4,5,6]]
lst2 = lst1.copy()
lst1[-1].append(7)
print(lst2)
'''

import copy
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.deepcopy(lst1)
lst1[-1].append(7)
print(lst2)

# 深拷贝字典
dic = {'a':1,'b':[1,2,3]}
dic2 = copy.deepcopy(dic)
dic['b'].insert(2,4)
print(dic)
print(dic2)

# 深拷贝 比 浅拷贝 占用空间更大,速度更慢;
# 多级容器用深拷贝,一级容器用浅拷贝


# ### 字典相关函数
dic = {}
#'top':'the shy','middle':'rookie','bottom':'uzi','support':'faker','jungle':'厂长'
# 增
dic['top'] = 'the shy'
dic['middle'] = 'faker'
dic['bottom'] = 'uzi'
dic['support'] = 'mata'
dic['jungle'] = 'kakao'
print(dic)

# fromkeys() 使用一组键和默认值创建字典(为当前键赋值初始值)
lst = ['top','middle','bottom']
dic = {}.fromkeys(lst,None)
print(dic)
dic['middle'] = 'a' #对于同一列表 将会导致所有空列表中都添加了字符串 'a'
print(dic)

#注意点(列表)
lst = ['top','middle','bottom']
dic = {}.fromkeys(lst,[])
print(dic)
dic['top'].append(1)
print(dic)

# 删
dic = {'top':'the shy','middle':'rookie','bottom':'uzi','support':'faker','jungle':'厂长'}
# pop() 通过键去删除键值对 (若没有该键可设置默认值,以防报错)
res = dic.pop('top')
print(res) #res 存储的是键所对应的值
print(dic)

mykey = 'jungle123'
res = dic.pop(mykey,'该键不存在')
print(res,dic) #当找不到对应的键时,会返回设定的默认值('该键不存在')

#popitem() 删除最后一个键值对
res = dic.popitem()
print(res,dic)

#clear() 清空字典

#改
# update() 批量更新(有该键就更新,没该建就添加)
'''
dic = {'top':'the shy','middle':'rookie','bottom':'uzi','support':'faker','jungle':'厂长'}
dicnew = {'hxg':'何仙姑','xboyww':'王文'}
dic.updata(dicnew)
print(dic)
'''

#查
#get() 通过键获取值(若没有该键可以设置默认值,以防报错)
dic = {'top':'the shy','middle':'rookie','bottom':'uzi','support':'faker','jungle':'厂长'}
print(dic['support']) #当使用这种方法时,若没有对应的键,会报错
print(dic.get('support')) #当使用get查找键对应的值是,若值不存在,则返回 None

#key() 将字典的键 组成新的可迭代对象
res = dic.keys()
print(res)

#value() 将字典中的值 组成新的可迭代对象

#items() 将字典中的键值对凑成一个个元组,组成新的可迭代对象
dic = {'top':'the shy','middle':'rookie','bottom':'uzi','support':'faker','jungle':'厂长'}
res = dic.items()
print(res)

