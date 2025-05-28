# 1、作用

# 2、定义：{}内用逗号分隔开多个key:value,其中value可以使用任意类型，但是key必须是不可变类型，且唯一
# d = {'k1':111,(1,2,3):222,'k2':22}
# d2 = {} # 默认定义出来的是空字典
# d3 = dict(x=1,y=2,z=3)

# 3、数据类型转换
info=[
    ['name','egon'],
    ('age',18),
    ['gander','male']
]

# d= {}
# for k,v in info:
#     d[k] = v
# print(d)

# d = {k:v for k,v in info} # 推导式
# print(d)

# d = dict(info)

# 造字典的方式(快速初始化一个字典)
# keys = ['name','age','gander']
# d = dict.fromkeys(keys,None)
# print(d)

# 4、内置方法
# 优先掌握的操作：
# 1、按key存取值：可存可取
d = {'k1':111}
# 针对赋值操作，key存在，则修改
d['k1'] = 222
# key不存在，则创建新值
d['k2'] = 333

# 2、长度len

# 3、成员运算in和not in
# 依据key

# 4、删除
# 4.1del d['k1']

# 4.2d.pop('k2') # 根据key删除元素，返回删除key对应的那个value值

# 4.3d.popitem() # 随即删除，返回key对应value值得元组

# 5、键keys(),值values(),键值对items()
dict3 = dict(x=1,y=2,z=3)
# 在python2中获取的是一个列表，在python3中获取到的是一只下蛋的老母鸡
dict3.keys()
dict3.values()
dict3.items()

# 需要掌握的内置方法
# clear()清空字典
dict3.clear()
# update()更新字典
dic = {'k2':222,'k3':333}
dict3.update(dic)
# get()通过key获取值，key不存在时不报错
# setdefault() 设置键值对默认值，如果有key就用添加的值，没有则使用默认值
# setdefault返回字典中key对应的值