import sys
import os
# python3.8 run.py 1 2 3
# sys.argv获取的是解释器后的参数值
# print(sys.argv)

listvar = sys.argv
orgin_file = listvar[1]
goal_file = listvar[2]
if os.path.isfile(orgin_file) and os.path.isfile(goal_file):
    with open('{}'.format(orgin_file),mode='rb') as f,\
        open('{}'.format(goal_file),mode='wb') as f2:
        for line in f:
            f2.write(line)