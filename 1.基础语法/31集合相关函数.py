# ### 集合的相关函数
setvar = {'王文','乔碧萝'}
# 增
# add 向集合中添加数据
setvar.add('周润发')
print(strvar)

#update() 迭代着增加
lst = ['a','b','c']
setvar.update(lst)
print(setvar)

# 删
#clear() 清空集合
setvar.clear()
print(setvar)

setvar = {'王文','王源','黄渤'}
#remove() 删除集合中指定的值(不存在则报错)
setvar.remove('黄渤')
#setvar.remove('黄柏') 不存在时报错
print(setvar)

#discard() 删除集合中指定的值(不存在的不删除 推荐使用)
res = setvar.discard('黄柏')
print(res,setvar) # 不报错,不会导致下面的代码终止

#pop() 随机删除集合中的一个数据
res = setvar.pop()
print(res,setvar)

# 改查 (无法实现)


# 冰冻集合
# frozenset 可强转容器类型数据变为冰冻集合
# 冰冻集合一旦创建,不能在进行任何修改,只能做交叉并补

# 定义一个冰冻集合
fz = frozenset()
print(fz,type(fz))

lst1 = ['a','b','c','d']
lst2 = ['a','b','f','z']

fz1 = frozenset(lst1)
fz2 = frozenset(lst2)

# 交集
res = fz1 & fz2
print(res)
res = fz1.intersection(fz2)
print(res)

# 差集
res = fz1 - fz2
print(res)
res = fz1.difference(fz2)
print(res)

# 不能在冰冻集合中 做添加或者删除操作
