# 定义有名函数
# func = 函数的内存地址
def func(x,y):
    return x+y

# 2、定义匿名函数
# lambda x,b: x+y

# 3、调用匿名函数
# 方式一
(lambda x,y:x+y)(1,2)

# 方式二
func1=lambda x,y:x+y
func1(2,2)

# 匿名函数用于临时调用一次场景：更多的是将匿名函数与其他函数配合使用