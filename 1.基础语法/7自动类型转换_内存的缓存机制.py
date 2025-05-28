# ### 自动类型转换 Number (int float bool complex)
'''
自动类型转换:默认项更高级精度转换
默认精度从低到高:
    bool<int<float<complex
'''

#bool + int
res = 5 + True
print(res)

#bool + float
res = False + 4.11
print(res)

#bool + complex
res = True + 2+1j
print(res)

#int + float
res = 3 + 3.33
print(res)

#int + complex
res = 4 + 4+4j
print(res)

#float + complex
res = 4.55 + 1-34j
print(res)


# ### 内存的缓存机制:
'''
Number 部分
1.对于整形而言,-5~正无穷范围内的相同值 id一致
2.对于浮点数而言,非负数范围内的相同值 id一致
3.布尔值而言,值相同情况下,id一致
4.复数在 实数+虚数 这样的结构中永不相同(只有虚数的情况例外)
'''

'python3.7之后,只要值相同,id就相同,无范围限制'


var1 = 22
var2 = 22
var1 = -100
var2 = -100
var1 = 2+3j
var2 = 2+3j
print(id(var1),id(var2))#对于相同的number,str都是唯一的不可改变,因而用相同去重

listvar1 = ["lei","we","wfew"]
listvar2 = ["lei","we","wfew"]
print(id(listvar1),id(listvar2)) #相同值的列表的id不同,因为它们是可变的,要是id相同就会改一变二

tuplevar = ([1,2,3],"wo",{"weee"},{"ser":"ziwe"}) # 元组可以放列表,集合,字典这些不可哈希的数据
tuplevar1 = (1,2,3)
tuplevar2 = (1,2,3)
print(id(tuplevar1),id(tuplevar2))



# 容器类型部分
"""
5字符串和元组相同的情况下,地址相同
6列表,字典,集合无论什么情况下 id标识都不同
"""










