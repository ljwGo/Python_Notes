# ### 命名分组
import re
strvar = '<div>今天天气真不戳</div>'

# 正常匹配
lst = re.findall('<.*?>(.*?)</.*?>',strvar)
print(lst)

# 反向引用 \1 代表的是把第一个括号匹配到的值,拿过来再引用一次
lst = re.findall('<(.*?)>(.*?)<(/\1)>',strvar)

# 2 命名分组
# (?P<组名>正则表达式) 给这个组起一个名字
# (?P=组名) 引用之前的组的名字,把改组名匹配到的内容放到当前位置
lst = re.findall('<(.*?)>(.*?)<(/\1)>',strvar)

# 方法一
strvar = 'a1b2cakjhk'
re.search(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(.*?)(?P=tag1)(?P=tag2)',strvar)

re.search(r'(?P<tag1>.*?)\d(?P<tag2>.*?)\d(.*?)(\1)(\2)',strvar)









