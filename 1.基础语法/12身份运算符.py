# ### 身份运算符 is 和 is not(检测两个数据在内存当中是否是同一个值)

var1 = -2.2
var2 = -2.2
print(var1 is var2)

# ### 逻辑运算符

#and 逻辑与
'''一假则假,全真则真'''
res = True and True  # 返回真
res = True and False # 返回假
res = False and False# 返回假
res = False and True # 返回假
print(res)

#or 逻辑或
'''一真则真,全假则假'''
res = True or True  # 真
res = True or False # 真
res = False or True # 真
res = False or False# 假

#not 逻辑非
res = not True
res = not False
print(res)


#逻辑短路:后面的代码不执行(不能改变最终的结果)
"""
True or 表达式
False and 表达式
"""

True or print(111) # print 不会执行
print(111) or True # print 会执行

False and print(111) #不会打印111
print(111) and False #会打印111

res = 8 or 1  #返回8
res = 8 and 1 #返回1
res = not 8   #返回False
res = not 0   #返回True
print(res)


#逻辑的优先级
# () > not > and > or
print((4+5)*2)

res = 5 or 6 and 7 #5 or 7
res = (5 or 6) and 7 # 5 and 7
res = not (5 or 6) and 7 # not 5 and 7
res = 1>2 or 3<4 and 5>6 # False or True and False
res = 1<2 and 3>5 or 7<6 and 90>100 or 100<2000 # True and False or False and False or True
print(res)

# 注意点:
True or False and True or False # 这种情况直接短路
False and True or True and True # False and 一堆表达式,不能直接判定结果
#出现这种情况的原因:优先级and>or

# isinstance 判断类型的
"""
int float bool complex str tuple list set dict
isinstance(要判断的值,要判断的类型) 返回True真 或者 False假

isinstance(要判断的值,(把所有可能的类型塞到元组当中))
"""

#用法一
strvar = "我好帅"
res = isinstance(strvar,str)
print(res)

#用法二
listvar = [1,2,3]
res = isinstance(listvar,(list,tuple,set,dict,str))
print(res)




