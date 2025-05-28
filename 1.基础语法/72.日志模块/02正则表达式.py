import re
# findall指从左到右依次检索
re.findall('\w', 'aaneah3_*()7') # 匹配数字字母下划线
re.findall('\W', 'aaneah3_*()7\t\n\r\f') # 匹配非数字字母下划线
re.findall('\s', 'aaneah3_*()7\t\n\r\f') # 匹配空白字符
re.findall('\S', 'aaneah3_*()7\t\n\r\f') # 匹配非空白字符
re.findall('\d', 'aaneah3_*()788\t\n\r\f') # 匹配数字
re.findall('\D', 'aaneah3_*()788\t\n\r\f') # 匹配非数字
# 了解 re.findall('\Aaaa', 'aaneah3_*()788\t\n\r\f') # 从头开始匹配
re.findall('^aaa', 'aaneah3_*()788\t\n\r\f') # 从头开始匹配
# 了解 re.findall('aaa\Z', 'aaneah3_*()788\t\n\r\f') # 只匹配结尾
re.findall('aaa$', 'aaneah3_*()788\t\n\r\f') # 只匹配结尾
str = '''
sb
eee
aaa
'''
re.findall('aaa\Z', str) # 只匹配结尾
re.findall('aaa$', str) # 只匹配结尾

print(re.findall('^alex$','al   ex'))

# 重复匹配：. * ? {n,m}
# .：匹配除了\n之外任意一个字符   re.DOTALL可以指定.匹配所有的字符

# *：左侧字符重复0次货无穷次，性格贪婪
