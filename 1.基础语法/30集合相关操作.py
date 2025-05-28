# 按住ctrl同时点击关键字可以查看其类的方法 如tuple

# ### 集合的相关操作
set1 = {'郭富城','刘德华','张学友','王文'}
set2 = {'王宝强','王源','王文'}
# intersection() 交集
res = set1.intersection(set2)
print(res)
# 简写 &
res = set1 & set2
print(res)

#difference() 差集
res = set1.difference(set2)
print(res)
# 简写
res = set1 - set2
print(res)

# union() 并集
res = set1.union(set2)
print(res)
# 简写 1(按位或)
#res = set1 1 set2
#print(res)

# symmetric_difference() 对称差集
res = set1.symmetric_difference(set2)
print(res)

# 简写 ^
res = set1 ^ set2
print(res)

#issubset() 判断是否是子集
set1 = {'周杰伦','林俊杰','王文'}
set2 = {'王文'}
res = set2.issubset(set1)
print(res)

#简写 < <=
res = set2 < set1
print(res)

#issuperset() 判断是否是父集
res = set1.issuperset(set2)
print(res)

#简写 > >=
res = set1 > set2
print(res)

#isdisjoint() 检测两集合是否不想交 不相交返回 True; 相交返回False
res = set1.isdisjoint(set2)
print(res)
