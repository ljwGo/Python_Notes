'''
1、什么是for循环
    循环就是重复做某件事情，for循环时python提供第二种循环机制

2、为何要有for循环
    理论上for循环能做的事情，while循环都可以做
    之所以要有for循环，是因为循环在循环取值（遍历取值）比while更简洁

3、如何用for循环
语法：
for 变量名 in 可迭代对象：# 可迭代对象可以是：列表、字典、字符串、元组、集合
    代码1
    代码2
    代码3
'''

# 案例1：循环取值
# 简单版
# for x in ['egon', 'alex', 'lxx']:
#     print(x)
# for循环也称为迭代循环

# 复杂版
# l = ['egon', 'alex', 'lxx']
# i = 0
# while i < 3:
#     print(l[i])
#     i+=1

# 二：总结for循环与while循环的异同
# 1、相同之处：都是循环，for循环可以干的事，while循环也可以干
# 2、不同之处：while循环称之为条件循环，循环次数取决于条件何时变为假；for循环称之为取值循环，循环次数取决in后包含的值得个数

# 三：for循环控制循环次数：range
# range(10)是一个[0,1,2,3,4,5,6,7,8,9]
# range(1,9,2) 1开始数字，9结束数字（无法取），2步长

# 补充
# print('hello', 'world', 'egon')
# print('hello\n')
# print('world')

print('hello', end='*')
print('world', end='*')