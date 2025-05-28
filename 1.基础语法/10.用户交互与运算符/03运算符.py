# 1、算术运算符
# print(10 + 3.1)
# print(10 + 3)
print(10/3) # 结果带小数
print(10//3) # 只保留整数部分
print(10 % 3) # 取模、取余数
print(10 ** 3) # 取模、取余数

# 2、比较运算符：>、>=、<、<=、==、!=

# 3、赋值运算符
# 3.1 =:变量的赋值
# 3.2 增量赋值:
age = 18
#age = age+1
age += 1
print(age)
# 3.3 链式赋值
x = 10
y = x
z = y
print(x,y,z)

# 交叉赋值
m = 10
n = 20
tem = m
m = n
n = tem
# m,n = m,n
print(m, n)

# 解压赋值
salaries = [111,222,333,444,555]
mon0 = salaries[0]
mon1 = salaries[1]
mon2 = salaries[2]
mon3 = salaries[3]
mon4 = salaries[4]
# mon0,mon1,mon2,mon3,mon4 = salaries
# 对应的变量名多一个或者少一个都不行
# x,y,z,*_ = salaries # *会将没有对应关系的值存成列表然后
# 取后三个值
# *_,x,y,z = salaries
# 无法取中间的值

# 解压字典默认解压出来的是字典的key