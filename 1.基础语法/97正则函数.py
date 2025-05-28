# ### 正则函数
import re
# search 通过正则匹配出第一个对象返回,通过group取出对象中的值
strvar = '5*7 9*8'
obj = re.search('(\d+)[*/]\d+',strvar)
print(obj)
# group 获取匹配的内容
res = obj.group()
print(res)
res = obj.groups()
print(res)

# match 验证用户输入内容
'''search在正则表达式的前面加上^ 就与math函数一摸一样'''
strvar = 'y17164684846'
obj = re.search('^\d+',strvar)
obj2 = re.match('\d+',strvar)
print(obj,obj2)

# split 切割
strvar = 'wangwen|alex|xboy-fwfw'
lst = strvar.replace('-','|').split('|')
print(lst)

strvar = 'wangwen|alex&xboy-fwfw'
res = re.split('[-&|]',strvar)
print(res)

strvar = 'wangwen156156alex14654xboy6464fwfw'
res = re.split('\d+',strvar)
print(res)

# split(正则表达式,字符串,[选择分割的次数,可选])
res = re.split('\d+',strvar,1)
print(res)

# sub 替换 返回的结果是一个字符串
strvar = 'wangwen|alex&xboy-fwfw'
re.sub('[|&-]','%',strvar)
print(res)

# sub(正则表达式,要替换的字符串,原字符串,[选择替换的次数,可选])
re.sub('[|&-]','%',strvar,1)
print(res)

# subn 替换 用法上与sub一样,但是返回的结果是元组,(替换后的结果,替换的次数)
re.subn('[|&-]','%',strvar,1)
print(res)

# finditer 匹配字符串中相应的内容,返回迭代器
from collections.abc import Iterator
strvar = 'wangwen|alex&xboy-fwfw'
res = re.finditer('\w+',strvar)
print(res)
# 判断是否是迭代器
print(isinstance(res,Iterator))

for i in res:
	print(i)

# compile 制定一个统一的匹配规则
'''
正常情况下,需要先编译好正则表达式,再去执行匹配
如果频繁的使用,浪费时间和空间

所以使用compile 用来编译一次,不用对同一个正则反复编译
'''
strvar = 'wangwen|alex&xboy-fwfw'
pattern = re.compile('\d')
print(pattern)
res = pattern.findall(strvar)
print(res)

# 正则表达式修饰符
# re.I 是匹配对大小写不敏感
strvar = '<h1>这是一个大标题</H1>'
pattern = re.compile('<.*?>(.*?)<.*?>',flags=re.I)
obj = pattern.search(strvar)
print(obj)

# re.M 使每一行都能够单独匹配(多行匹配),影响^和$
strvar  = '''
<a>fwaagaga</a>
<p>fwag65156</p>
<div>225*^*</div>
'''

pattern = re.compile('^<.*?>(.*?)<.*?>$',flags=re.M)
lst = pattern.findall(strvar)
print(lst)

# re.S 使 . 匹配包括换行在内的所有字符
strvar = '''
give
122mefive
'''
pattern = re.compile('.*?mefive',flags=re.S)
obj = pattern.search(strvar)
print(obj)
