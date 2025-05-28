# import os
import time
# print('[%-50s]' % '#') # - 是指字符左对齐；50 是指共有50个字符
# def progress():
#     res = ''
#     for i in range(20):
#         res += '#'
#         print('\r[{: <20}]'.format(res),end='')
#         # time.sleep(0.5)

recv_size = 0
total_size = 333333
while recv_size <= total_size:
    time.sleep(0.3)
    recv_size += 1024
    percent = recv_size / total_size
    if percent > 1:
        percent = 1
    process = int(50 * percent) * '#'
    print('\r[{: <50}]{}%'.format(process,int(percent*100)),end='')