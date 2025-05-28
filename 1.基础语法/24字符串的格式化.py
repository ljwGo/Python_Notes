# ### 字符串的格式化.format (%d %f %s也是字符串的格式化)

#1顺序传参
strvar = "{}向{}开了一枪,银弹而亡".format("我","你")
print(strvar)
#2索引传参
strvar = '{1}给{0}一个大大的拥抱'.format('我','你')
print(strvar)
#3关键字传参
strvar = '{who1}给{who2}一个大大的拥抱'.format(who2 = '我',who1 ='你')
print(strvar)
#4容器类型数据(列表或元组)传参
#1
strvar = '{0[1]}给{1[2]}一个大大的拥抱'.format(['a','b','c'],('d','e','f'))
print(strvar)
#2
strvar = '{group1[1]}给{group2[2]}一个大大的拥抱'.format(group1=['a','b','c'],group2=('d','e','f'))
print(strvar)
#3 如果是字典,在获取值的时候,键的两边不要套引号 => 针对于format格式化字符串情景下
strvar = '{1[e]}给{0[a]}一个大大的拥抱'.format({'a':1,'b':2,'c':3},{'d':4,'e':5,'f':6})
print(strvar)

# 5 format的填充符号的使用( ^ < >)
'''
^ 原字符串居中
> 原字符串居右
< 元字符串居左

{who:*^10}
who : 要填充的字符
*   : 要填充的符号
^   : 要填充的方向
10	: 要填充的总长度  符号个数 + 原字符串个数 = 11
'''

strvar = "{who:*^11}在{where:><4}做{what:>5}".format(who= '我',where= '学校',what= '作业')
print(strvar)

# 6 进制转换等特殊符号的使用( :d :f :s :,)
#:d 整型占位符
strvar = '吴荣泽有{:d}女友'.format(7)
print(strvar)

# :2d 占用两位
strvar = '{:d}*{:d}={:3d}'.format(5,6,4*1)
print(strvar)

# :^3d 让元字符串居中,相对于%d多了此功能
strvar = '{:d}*{:d}={:^3d}'.format(5,6,4*1)
print(strvar)

# :f 浮点型占位符(默认为2位,  .2f调整为小数2位)
strvar = '张三犯下了{:f}次罪'.format(2222.2)
print(strvar)

# :s 字符串占位符
strvar = "{:s}"
print(strvar.format('我来了'))

#:, 金钱占位符
strvar = '{:,}'.format(1234567)
print(strvar)

# 综合案例
strvar = '{:s}开了{:.2f}元工资,买了{:d}个布加迪威龙'.format("郭少东",9.9,10)