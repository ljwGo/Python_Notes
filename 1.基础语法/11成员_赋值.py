# ### 赋值运算符 = += -= *= /= //= %= **=

# =
a = 4

# += -= *= /=(float型) //= %= **=
var1 = 3
var2 = 4

var1 += var2
print(var1)
# var1 = var1 + var2 的简写
# var1 = var1 - var2 的简写
#             *
#             /
#            //
#             %
#            **

var = 5
var **= 2
print(var)


#i++ i-- ++i --i (自动加一)

# 4成员运算符: in 和 not in (针对于容器型数据)
"""必须是连续的片段"""
strvar = "如果遇到你是一种错,那我宁愿一错再错"
res = "你" in strvar
res = "一种错" in strvar
res = "你我" in strvar
print(res)

# list tuple set
listvar = ["罗总要","主进程","杨马志","肖波","张晓东","是华清"]
res = "主进程" in listvar
print(res)

tuplevar = ("罗总要","主进程","杨马志","肖波","张晓东","是华清")
res = "杨马志" not in tuplevar
print(res)

setvar = {"罗总要","主进程","杨马志","肖波","张晓东","是华清"}
res = "肖波111" not in setvar
print(res)

# dict
'''在字典中,in,not in 判断的是字典的键,不是值'''
dictvar = {"罗总要":"应该减肥","主进程":"小心被卖掉","杨马志":"王者"}
res =  "应该减肥" in dictvar
res = "罗总要" in dictvar
print(res)

