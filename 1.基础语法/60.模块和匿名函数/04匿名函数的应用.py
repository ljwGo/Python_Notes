salaries = {
    'tom': 2222,
    'lxx': 11111,
    'zhangsan': 5200,
    'jack': 7777
}


# 需求1：找出薪资最高的那个人
def func(x):
    return salaries[x]


max(salaries, key=func)
# max方法会将salaries中的值进行迭代，并将迭代出的值抛给func处理，处理的返回值进行比较

max(salaries, key=lambda k: salaries[k])

min(salaries, key=lambda k:salaries[k])

# 排序
sorted(salaries, key=lambda k:salaries[k])

# map() 了解
# filter() 过滤
# reduce() 合并