# def func():
#     x = 222
# x = 111
# func()
# print(x) # 111

# 示范二：如果在局部空间想要改变全局变量的值（不可变类型），必须先使用global声明
def func():
    global x
    x = 222
x = 111
func()
print(x)

# 示范三3：
# l = [111,222]
# def func():
#     l = [111,222]
#     l.append(333)
#     print(l,id(l))
# func()
# print(l,id(l))

# nonloacl（了解）：修改函数外层函数包含的名字对应的值（不可变类型）
