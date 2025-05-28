# ### 二级容器:外面是一个容器类型的数据,里面的元素还是一个容器类型的元素

#二级列表
listvar = [1,2,3,4,5,[6,7,8]]
#二级元组
tuplevar = (1,2,3,4,5,(11,22,33),90)
#二级集合
setvar = {1,2,3,"a","b","c",(4,5,6)}
#二级字典
dictvar = {"a":1,"b":2,"c":{"d":1,"e":2}}

#四级容器
container = [1,2,3,4,5,(6,7,8,["a","b","c",{"aa":1,"bb":"王文"}])]
res = container[-1]
print(res)
res2 = res[-1]
print(res2)
res3 = res2[-1]
print(res3)
res4 = res3['bb']
print(res4)

# 简写
res = container[-1][-1][-1]["bb"]
print(res)

#等长的二级容器
container = [(1,2,3,4),{"a","b","c","d"}]
container = [(1,2),[3,4]]


# ### dict 强制转化成字典
'''必须是等长的二级容器,并且里面的元素个数是2个'''

#外面是列表(里面是元组或者列表(推荐))
listvar = [("a",1),("b",1),("c",3),["d",4]]
dictvar = dict(listvar)
print(dictvar)

#语法上可以,但是不推荐,因为集合无序;同时不推荐字符串,对于字符串,仅限2个元素才可以
listvar = [("a",1),["b",2],{"c",3},"c3"]
dictvar = dict(listvar)
print(dictvar)

#2外面是元组
tuplevar = (("a",1),["b",2])
dictvar = dict(tuplevar)
print(dictvar)

#3外面是集合,里面只能放元组
setvar = {("a",1),("b",2)}
dictvar = dict(setvar)
print(dictvar)


# 去掉类表中的所有重复数据
listvar = [1,2,3,3,4,4,5,6,7,"a","a","b","b","c","c"]
#由于算法的原因,数字在集合中按小大顺序排列,而其他字符串,元组则会打乱顺序
res = set(listvar)
listvar2 =list(res)
print(listvar2)

tuplevar = (1,2,3,4,5,6,["a","b","c"])   #可以修改元组中箱套的元素(列表,字典)中的元素
tuplevar[-1][-1] = "b"
print(tuplevar)


