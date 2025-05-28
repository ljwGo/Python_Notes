# ### 购物车
'''
# 复习
# 顺序传参
strvar = '{:s}'.format('张三')
print(strvar)
# 关键字传参
strvar = '{who}'.format(who='周永林')
print(strvar)
# 传进来的who,这个数据类型是字符串
strvar = '{who:s}'.format(who='黄乐喜')
print(strvar)

# 填充字符 * 天重符号 ^ 原字符串居中 10填充的个数 s数据类型是字符串
strvar = '{who:s*^10}'.format(who='朱景城')
print(strvar)

# 可以不强制指定类型,默认什么数据类型都可以
dic2 = {'name':'电脑','price':100}
strvar = '{dic[name]:*^10}'.format(dic=dic2)
print(strvar)

# 可以不强制指定填充符号,默认填充空格
strvar = '{dic[name]:^10}.format(dic=dic2)'
print(strvar)
'''














