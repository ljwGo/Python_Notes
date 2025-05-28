# ### 正则表达式 => 分组
import re
print(re.findall('.*?_good','wusir_good alex_good secret男_good'))
# 把想要匹配的内容,用小园括号包起来,表达分组
print(re.findall('(.*?)_good','wusir_good alex_good secret男_good')
# ?:是取消括号优先显示的功能
print(re.findall('(?:.*?)_good','wusir_good alex_good secret男_good'))

# l(竖杆) 代表或 , alb 匹配字符a 或者 匹配字符b . 把字符串长的写在前面,字符串短的写在后面
# abc 或者 abcd
strvar = 'abcpahgwajgioahnaabcd484'
lst = re.findall('abcdlabc',strvar)
print(lst)

# 匹配小数
'''
\ 可以把有意义的字符变得无意义,还可以把无意义的字符变得有意义
\n : 换行
\. : 单纯的匹配一个点
'''
strvar = '3.56 89.44 .418 15. 8,67 '
re.findall('\d+\.\d+')

# 匹配小数和整数
re.findall('\d+\.\d+l\d+',strvar)

# 使用分组合并正则
#\d+\.\d+
#\d+
#\d+(\.\d+)?
re.findall('\d+(?:\.\d+)?',strvar)

# 匹配135或171的手机号
re.findall('(?:135l171)\d{8}','13566668888 171123456785')

# 匹配www.baidu.com 或者 www.oldboy.com
re.findall(r'www\.(?:baidu|oldboy)\.com')

# search
'''
findall 匹配所有内容,缺陷:不能把匹配到的内容和分组里面的内容同时显示出来,返回的是列表
search 匹配到一个内容就直接返回,优点:可以把分组的内容,和实际匹配到的内容分开,同时显示,返回的是对象obj
obj.group() 获取匹配到的内容
obj.groups() 获取分组里面的内容
res = obj.group(3) 参数:获取分组里面第三个元素
'''

