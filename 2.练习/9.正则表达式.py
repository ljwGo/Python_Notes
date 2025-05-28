# 1
import re
strvar = 'fctcvhv'
re.findall('[+-]?\d+(\.\d+)?',strvar)
re.findall('[1-9]\d{3}-0[0-9]|1[0-2]-0[1-9]|[12]\d|3[01]',strvar)
re.findall('[1-9]\d{4,11}',strvar)
re.findall('1[3-9]\d{9}',strvar)
re.findall('\w{8-10}',strvar)
re.findall('[/da-zA-Z]{4}',strvar)
re.findall('[\w\._-]+@',strvar)















