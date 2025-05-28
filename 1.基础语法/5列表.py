# ### 容器类型 list 列表
'''
可获取,可修改,有序
'''


# 定义一个空列表
listvar = []
print(listvar)
print(type(listvar))

#正向索引    0  1    2      3      4
listvar = [89,8.1,False,8 + 8j,"赖建威"] #什么都能塞,int,str,float,bool,complex.
#逆向索引    -5 -4  -3     -2      -1

#获取类表中的值
res = listvar[4]
#你想所应可以迅速得到列表中最后一个元素(python特有)
res = listvar[-1]
print(res)

# 其他语言如何得到列表最后一个元素?
'''
len 可以获得容器类型数据的长度(元素个数)    以下是通用写法
'''
res = len(listvar)
print(res)
#print(listvar[4]) => res = listvar[4]
res2 = listvar[res-1]
print(res2)

#2修改类表中的值
listvar[1] = "a"
print(listvar)

# ### 容器类型数据 tuple 元祖
'''
可获取,不可修改,有序
'''

#定义一个空元组
'''
用逗号,来区分空元组,逗号是元组这个数据类型的标识
如果定义一个空元组,可以直接使用().只能是空元组:
'''
tuplevar = (1,2,3,4,5)
print(tuplevar)
print(type(tuplevar))

tuplevar = (1)                      #括号不足以表示这就是元组
print(tuplevar,type(tuplevar))
#结果为int

#tuplevar = (1,)                    #它是元组
#print(type(tuplevar))

#以下是元组
tuplevar = 1,2,3,4,5
tuplevar = (1,2,3,4,5) #推荐写法
print(tuplevar,type(tuplevar))

#1获取元组中的值
#正向          0      1       2      3
tuplevar = ("王文","隔壁老王","张三","赖建威")
#逆向          -4      -3      -2     -1

res = tuplevar[2]
res = tuplevar[-1]
print(res)

#2元组不能够修改其中的值


# ### 字符串 str
"""
可获取,不可修改,有序
"""
#正向      012345...
strvar = "黑夜给了我黑色的眼睛,我去用它翻白眼"
#逆向                          ...-3-2-1

#1获取字符串当中的元素
res = strvar[5]
res = strvar[-2]
print(res)

#2不可修改字符串中元素的值
























