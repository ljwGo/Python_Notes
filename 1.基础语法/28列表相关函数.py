# ### 列表相关函数
listvar = ['宗荣玲','李守銮','黄乐喜','卓冰洁']
# 增
#append()   1默认在列表最后加入新元素
listvar.append('长远')
print(listvar)

#insert(索引,值)   2在指定索引之前插入元素
listvar.insert(0,"郭少东")
print(listvar)

#extend 迭代追加所有元素
'''可迭代型数据:(容器类型数据 range(对象) 迭代器)'''
#lst = ['a','b','c']
#listvar.extend(lst)
strvar = 'abc'
listvar.extend(strvar)
print(listvar)

# 删
#pop 通过指定的索引删除元素,若没有索引则移除最后一个
listvar = ['宗荣玲','李守銮','黄乐喜','卓冰洁']
res = listvar.pop(2)
print(listvar)
print(res)

# remove 通过给与的值来删除,如果多个相同元素,默认删除第一个(与replace替换所有指定的值不同)
listvar = ['宗荣玲','李守銮','黄乐喜','卓冰洁']
res = listvar.remove('李守銮')
print(listvar)
print(res)

# clear 请空列表
listvar = ['宗荣玲','李守銮','黄乐喜','卓冰洁']
res = listvar.clear()
print(listvar)
print(res)

# 改
# 查

# 列表的其他操作
# index 获取某个值在列表中的索引,找不到会报错
# 格式,index(值[,start],[,end] # 中括号内 表达参数可选项

listvar = ['宗荣玲','李守銮','黄乐喜','卓冰洁']
res = listvar.index('黄乐喜')
res = listvar.index('黄乐喜',0,3)
print(res)

# count 计算某个元素出现的次数
# 格式:列表.count(值) 返回值:次数

# sort 列表排列(默认从小到大)
listvar = [1,2,44,-100,-3]
listvar.sort()
print(listvar)

# 从大到小排列
listvar.sort(reverse=True)
print(listvar)

# 对字母进行排列
listvar = ['james','kobe','caixukun','yao','kuli','daivs']
listvar.sort()
print(listvar)

# 中文可以排列,无规律可循
listvar = ['蔡徐坤','杀马特','葬爱家族','黄子稻']
listvar.sort()
print(listvar)

#reverse() 列表反转操作
listvar =  [1,2,False,77,'蔡徐坤']
listvar.reverse()
print(listvar)