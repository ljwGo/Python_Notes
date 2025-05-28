import os
import sys
print(__file__) # 获取文件的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# from core import src
#
# if __name__ == '__main__':
#     src.run()