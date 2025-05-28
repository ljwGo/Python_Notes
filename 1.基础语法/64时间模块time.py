# ### 时间模块 time
# 时间戳是指从1970年1月1日0时0分0秒到指定时间之间的秒数
import time
# time() 获取本地时间戳
res = time.time()
print(res)

# mktime() 通过[时间元祖]获取[时间戳] (参数是时间元组)
ttp = (2020,10,6,11,23,30,0,0,0)
res = time.mktime(ttp)
print(res)

# localtine() 通过[时间戳[获取[时间元组] (默认当前时间)
res = time.localtime()
print(res)

res = time.localtime(1572233310)
print(res)

# ctime() 通过[时间戳]获取[时间字符串] (默认当前时间)
res  = time.ctime()
print(res)

# asctime() 通过[时间元组]获取[时间字符串] (参数是时间元组)
ttp = (2019,11,24,11,22,1,0,0,0)
res = time.asctime(ttp)
print(res)

# 优化版
ttp = (2019,11,24,11,22,1,0,0,0)
res = time.mktime(ttp)
time_str = time.ctime(res)
print(time_str)

# strftime() 通过[时间元组]格式化[时间字符串] (格式化字符串,[可选时间元组参数])
# 格式化时间字符串:
# 格式 含义
'''
  %d








'''
"""
ttp = (2019,11,24,11,22,1,0,0,0)
# strftime 在linux系统中支持中文,windows不支持
res = time.strftime('%Y-%m-%d %H:%M:%S 比尔盖茨生日') # 默认以当前时间进行转换
print(res)

res = time.strftime('%Y-%m-%d %H:%M:%S 比尔盖茨生日',ttp)
print(res)
"""

# strptime() 通过[时间字符串]提取出[时间元组] (时间字符串,格式化字符串)
strvar = '1955-10-28 11:39:10 比尔盖茨生日'
strvar2 = '%Y-%m-%d %H:%M:%S 比尔盖茨生日'
res = time.strptime(strvar,strvar2)
print(res)

'''
# sleep() 程序睡眠等待
time.sleep(200)
print('睡醒了')
'''

# perf_counter() 用于计算程序运行的时间
print('<======>')
startime = time.perf_counter()
for i in range(44):
	pass
endtime = time.perf_counter()
res = endtime - startime
print(res)



