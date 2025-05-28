# 一：time
import time
import datetime

# 时间分为三种格式：
# 1、时间戳：从1970年到现在经过的秒数
#   作用：用于计算时间间隔
print(time.time())

# 2、按照某种格式显示的时间：2020-11-22 11:11:11
#   作用：用于展示时间
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
print(time.strftime('%Y-%m-%d %X'))

# 3、结构化的时间
#   作用：用于单独获取时间的某一部分
res = time.localtime()
print(res)
print(res.tm_mday)

# 二：datetime

print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=3))

# 时间模块需要掌握的操作
# 1、时间格式的转换
s_time = time.localtime()
print(time.mktime(s_time))

# 时间戳->struct_time
tp_time = time.time()
time.localtime(tp_time)
time.gmtime(tp_time)

time_str = '2011-11-22 22:11:11'
print(time.strptime(time_str, '%Y-%m-%d %M:%H:%S'))

# 真正需要掌握的是：format string <----> timestamp
struct_time = time.strptime('1988-03-03 11:11:11', '%Y-%m-%d %M:%H:%S')
timestamp = time.mktime(struct_time) + 7 * 86400

res = time.strftime('%Y-%m-%d %M:%H:%S', time.localtime(timestamp))
print(res)

# 了解知识
print(time.asctime())
print(datetime.datetime.fromtimestamp(2222222222))
