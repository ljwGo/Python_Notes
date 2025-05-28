def func():
    print('第一次')
    yield 1
    print('second time')
    yield 2
    print('third time')
    yield 3

g = func()
print(g)
# 生成器就是迭代器
# g.__iter__()
# g.__next__()

# 会触发函数体代码执行，然后遇到yield后停下来，并将yield后的值返回值来
res1 = g.__next__()
print(res1)

res2 = g.__next__()
print(res2)

# 应用案例
def my_range(start,end,step=1):
    while start < end:
        yield start
        start += step

g = my_range(1,3)
print(next(g))

for i in my_range(2,22,2):
    print(i)