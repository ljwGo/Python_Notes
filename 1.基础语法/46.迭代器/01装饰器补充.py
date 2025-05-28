# import time
# # 统计函数执行时间的装饰器
# def outter(func):
#     def decorate(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         print(end - start)
#     return decorate
#
# @outter
# def index(x,y):
#     print(x,y)
# print(index.__name__)
#
# # index = outter(index)
#
# # 将decorate做得跟原函数一模一样
# from functools import wraps
#
# def outter(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         # 添加的代码
#         res = func(*args,**kwargs)
#         return res
#     # wrapper.__name__ = func.__name__
#     # wrapper.__doc__ = func.__doc__
#     return wrapper