# 1、成员运算符
print('egon' in 'hello egon') # 判断一个字符串是否存在于一个大字符串中
print('e' in 'hello egon') # 判断一个字符串是否存在于一个大字符串中

# 判断key是否存在于字典中
print(111 in {'k1':111,'k2':222})
print('k1' in {'k1':111,'k2':222})

print('egon' not in 'hello egon') # 推荐使用
print('egon' not in 'hello egon') # 逻辑同上，但语义不明确，不推荐

# id身份运算符
