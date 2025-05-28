# ### 字符串的相关符号
# 1字符串的拼接
var1 = '亲爱的'
var2 = '男孩'
res = var1 + var2
print(res)

# 2字符串的重复 *
var = '重要的事情说三遍'
res = var * 3
print(res)

# 3 字符串跨行拼接 \
strvar = 'awawefwatwerasvatwafssssssssssssssssssssssssssss'\
'23333333332244444444444411111'

# \ 避免字符串过长,进行上下行拼接

# 4 字符串的suoyin
#		  0  1  2 3 4
strvar = '天 气 转 冷了'
#		  -5-4-3 -2-1
res = strvar[3]
res = strvar[-2]
print(res)

# 5字符串的切片

strvar = '为中华之崛起而读书,我们还年轻,毕竟18岁'
# 1 [开始索引:] 从开始索引截取到字符串的最后
res = strvar[3:]
print(res)

# 2[:结束索引] 从开头截取到结束索引之前(结束索引-1)
res = strvar[:7]
print(res)

# 3[开始索引:结束索引] 从开始索引截取到结束索引之前(结束索引-1)
res = strvar[11:14]
print(res)

# 4[开始索引:结束索引:间隔值] 从开始索引截取到结束索引之前按照指定的间隔截取字符
res = strvar[::2] 正向
res = strvar[::-1] 逆向
print(res)

# 5  [:] [::] 截取所有字符串

#开始索引 和 结束索引 不写 默认为开始 和 结束

#切片的意义,对容器类型进行单独的备份
