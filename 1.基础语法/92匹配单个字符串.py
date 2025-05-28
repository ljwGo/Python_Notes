# ### 正则表达式
import re
'''
lst = re.findall(正则表达式,字符串)
'''
# 1 预定义字符集
# \d 匹配数字
strvar = 'awfhwagw,;46146''你好神秘男孩02561651'
lst = re.findall('\d',strvar)
print(lst)

# \D 匹配非数字
strvar = 'awfhwagw,;46146''你好神秘男孩02561651'
lst = re.findall('\D',strvar)
print(lst)

# \w 匹配字母或数字或下划线 (正则函数中,支持中文的匹配)
strvar = 'awfhwagw,;46146''你好神秘男孩02561651'
lst = re.findall('\w',strvar)

# \W 匹配非字母或数字或下划线
strvar = 'awfhwagw,;46146''你好神秘男孩02561651'
lst = re.findall('W',strvar)
print(lst)

# \s 匹配任意的空白符 \n \t \r ' '
strvar = '  awfhwagw	,;46146''你好神秘男孩02561651'
lst = re.findall('\s',strvar)
print(lst)

# \S 匹配任意非空白符
strvar = '  awfhwagw	,;46146''你好神秘男孩02561651'
lst = re.findall('\S',strvar)
print(lst)

# \n 匹配一个换行符 [最好在正则表达式的前面加上r,让转义字符失效,原型化匹配]
strvar = '''
王文你真帅啊,我 受不了了

'''
lst = re.findall(r'\n',strvar)

# \t 匹配一个制表符
lst = re.findall(r'\t',strvar)
print(lst)

# 2 字符组 从小组中默认选一个
re.findall('[123]','451627')
print(lst)

print(re.findall('a[abc]b','aab abb acb adb'))
# 优化 [o - 9];[a - z] -是特殊字符 ^在字符组中,代表除了

# 匹配特殊符号 利用斜杠转义符,转移来实现匹配
re.findall(r'a[\^]','a^b')

# 匹配斜杠
print(re.findall(r'a\\b',r'a\b'))




