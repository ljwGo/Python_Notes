# 1、函数的嵌套调用
def max(a,b):
    if a>b:
        return a
    else:
        return b

def max4(a,b,c,d):
    res1 = max(a,b)
    res2 = max(res1,c)
    res3 = max(res2,d)
    return res3

# 2、函数的嵌套定义：在函数内定义其他函数

# 圆形
# 求周长：2*pi*radius
def circle(radius, action=0):
    from math import pi
    def perimiter(radius):
        return 2*pi*radius

    # 求圆形的面积：pi*(radius**2)
    def area(radius):
        return pi*(radius**2)