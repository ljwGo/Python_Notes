# ### 正则表达式 => 多个字符串匹配
# 量词
import re
# ? 匹配0个或者一个a
re.findall('a?b','abbzab abb aab') # ab b ab ab ab

# + 匹配1个或者多个a
re.findall('a+b','b ab abbbbb')

# * 匹配0个或者多个a
re.findall('a*b','b ab aab ')

# {m,n} 匹配m个至n个a
'''1<=x<=3'''
re.findall('a{1,3}','aaab ab aab')
# {m,} 至少m次
re.findall('a{2,}','abb,awagfgqaf')
# {m} 必须m次
re.findall('a{2}b','aaaabfwafagahzc')

# 2 贪婪模式与非贪婪模式
'''
贪婪模式: 默认向更多次匹配
非贪婪模式: 默认向更少次匹配

贪婪模式在底层使用的是回溯算法:
回溯算法: 默认从左向右进行匹配,一直到最后,直到最后再也匹配不到了,回头,找最后一个能够匹配到的数据

非贪婪模式: 在量词的后面加?,这个语法就是非贪婪,默认向更少次匹配
.?? .+? .*? .{1,23}?
'''
# 贪婪模式
strvar = '刘能和刘德华和刘铁锤子777子888'
print('<=======>')
lst = re.findall('刘.',strvar)
print(lst)
lst = re.findall('刘.?',strvar)
print(lst)
lst = re.findall('刘.+',strvar)
print(lst)
lst = re.findall('刘.*',strvar)
print(lst)
lst = re.findall('刘.{1.25}',strvar)
print(lst)
lst = re.findall('刘.{1.25}子',strvar)
print(lst)

# 非贪婪模式
strvar = '刘能和刘德华和刘铁锤子777子888'
lst = re.findall('刘.??',strvar)
print(lst)

lst = re.findall('刘.+?',strvar)
print(lst)

lst = re.findall('刘.*?',strvar)
print(lst)

lst = re.findall('刘.{1.25}?',strvar)
print(lst)

lst = re.findall('刘.{1.25}?子',strvar)
print(lst)

# 3 边界符 \b backspace 退格
'''
转义字符: \b backspace 退格
边界符也用的是\b,要注意转移
例如: word 卡住边界
	1 卡住左边界 \bw
	2 卡住右边界 d\b
	
'''
strvar = 'pwd word szf'
re.findall(r'\bw.*',strvar)
re.findall(r'\bw.*?',strvar)
re.findall(r'\bw.*? ',strvar)
re.findall(r'\bw\S*',strvar)
# print(lst)
re.findall(r'.*d\b',strvar)
re.findall(r'.*?d\b',strvar)

# 4 ^ $
'''
^ 以...开头
$ 以...结尾
如果正则表达式里面出现了^ $,代表把这个字符串看成一个整体,再去匹配

'''
strvar = '大哥大嫂大爷'
print(re.findall('大.',strvar))
print(re.findall('^大.',strvar))
print(re.findall('大.$',strvar))
print(re.findall('^大.$',strvar))
print(re.findall('^大.*?$',strvar))
print(re.findall('^大.*?大$',strvar))
print(re.findall('^大.*?爷$',strvar))







