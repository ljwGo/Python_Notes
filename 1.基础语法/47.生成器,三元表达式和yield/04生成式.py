# 列表生成式
l = ['alex_dsb','egon','lxx_dsb','zhangsan_dab']
new_l = [strvar.upper() for strvar in l]
new_l2 = [strvar.replace('_dsb','') for strvar in l]
print(new_l2)

# 字典生成器
l = [(222,'www'),(333,'eee'),(444,'hhh')]
d = {k:v for k,v in l}

# 生成器表达式 默认不加括号表示生成器
g = (i for i in range(10) if i < 5)
res = next(g)
print(res)

# with open('a.txt',mode='w+',encoding='utf-8') as f:
#     f.write('哈哈哈哈\n哈哈哈')
#     f.seek(0,0)
#     print(sum((len(line) for line in f)))
