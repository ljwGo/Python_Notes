import random
print(random.random()) # 获取一个0~1之间的随机浮点数
print(random.randint(1,3)) # 了解
print(random.randrange(1,3)) # 获取[1,3)之间的一个随机整数
print(random.choice([1,'2',[22,33]])) # 获取参数中随机值
print(random.sample([1,2,3,4],2)) # 第二个参数指定每次取值的个数
print(random.uniform(1,3)) # 随机获取1，3之间的小数
print(random.shuffle([1,2,3,4])) # 随机打乱列表

# 应用：随机验证码