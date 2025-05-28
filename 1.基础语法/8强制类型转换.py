# ### 强制类型转换 Number int float bool complex

var1 = 33
var2 = 23.11
var3 = True
var4 = 3+3j
var5 = "111"


'''
int 可由 int float bool str(仅数字) 转换
float
complex
bool     (容器类型数据/Number数据类型都可以)
'''
# int 强制转换成整型  (无需四舍五入)
res = int(var2)
res = int(var3)
# res = int(var4) errpr
print(res,type(res))

# float 强制转化成浮点型
res = float(var1)
res = float(var3)
res = float(var5)
print(res,type(res))

#complex 强制转化成复数
res = complex(var1)
print(res,type(res))
complex(3,-4)

#重要 bool 强制转换成布尔型  True 真的 False 假的
res = bool(var1)
print(res)

#布尔类型为假的情况
#0 0.0 0j的布尔值为False; ''(空字符串)[]()set(){}None的布尔型为False
#" "(含空格的字符串)
# Nome 是python中的关键字,代表空的,什么也没有,一般用于变量的初始操作
var = None

''''
括号里面不加任何值,可以转换出一个当前数据类型的值
'''
var = bool()
print(var)
#对应转化为数字0的有关值    0,0.0,False,0j




# ### 强制类型转换 容器类型数据(str list tuple set dict)
var1 = "你好世界"
var2 = ['赖建威','张三','李四','王五']
var3 = ('赖建威','张三','李四','王五')
var4 = {'赖建威','张三','李四','王五'}
var5 = 5488
var6 = {"a":1,"b":2}
print(var3,type(var3))

# str 强制转换成字符串
"""就是单纯的在原有数据的两边套上引号"""
res = str(var2)
print(res,type(res))

# repr 不转义字符,原型化输出,可以显示引号
print(repr(res))

# list 强制转换成列表
"""如果是字符串:把每一个字符都变成一个新元素组合在一起,形成新列表
如果是字典:只保留字典的键
如果是其他的容器:仅仅单纯的在原数据两边套上中括号即可"""
res = list(var1)
res = list(var3)
res = list(var4)  #(对于集合转换成列表,无无序性,按原本集合排序形成列表)
res = list(var6)
print(res,type(res))

#tuple 强制转换成元组
res = tuple(var1)
res = tuple(var2)
#res = tuple(var5)
res = tuple(var6)
print(res)

#set 强制转换成集合(具有无序性)
res = set(var1)
res = set(var2)
res = set(var6)
print(res)

#转化成对应的空字符串,空列表,集合,元组,字典
var = list()
print(var)





listvar = [1,2,1,1]
res=set(listvar)
print(res)

print(listvar[0] is listvar[-1])

