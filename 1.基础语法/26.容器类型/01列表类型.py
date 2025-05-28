# 1、作用
# 按照位置存储多个值

# 2、定义
# l=[1,1.2,'a'] # l=list([1,1.2,'a'])

# 3、类型转换:但凡能够被for循环便利的类型都可以当作参数传给list()转成列表
# res = list('hello')
# print(res) ['h', 'e', 'l', 'l', 'o']

# res = list({'k1':111,'k2':222,'k3':333})
# print(res)

# 4、内置方法
# 优先掌握的操作：
# 1、索引存取值（正向存取+反向存取）：既可以取也可以改
# l = [111,'222','hello']
# l[0] = 2 # 索引存在则修改对应的值
# print(l)

# 2、切片（顾头不顾尾，步长）
# l = [111,'egon','hello','a','b','c']
# print(l[0:3])
# print(l[::-1])
# new_l = l[:] # 切片等同于拷贝行为，而且相当于浅copy

# 3、长度
# res = len(l)

# # 4、成员运算符
# # in 和 not in

# # 5、追加
# l.append(333)
# print(l)

# # 6、插入值
# l.insert(1,'age')
# print(l)

# # 7、合并值
# # extend实现列表的合并

# # 8、删除
# # 方式一：通用的删除方法，只是单纯的删除，没有返回值
# l = [111,222,333]
# del l[1]
# # x = del l[1] # 抛出异常，不支持赋值语法

# # 方式二：l.pop()根据索引删除
# l.pop() # 不指定索引默认删除最后一个
# print(l)

# res = l.pop(1) # 按照索引删除,返回值res是删除的值
# print(l,res)

# # 方式三 l.remove() 根据元素删除,返回None，相当于没有返回值
# res = l.remove('111')
# print(l,res)

# 需要掌握的操作
l = [1,'aaa','bbb','ccc','aaa']

# 1、l.count()
res = l.count('aaa')
print(res)

# 2、l.index()
print(l.index('aaa'))

# 3、l.clear()
l.clear() # 清空

# 4、l.reverse():不是排序，而是将列表颠倒过来
l = [1,'egon','alex','lxx']
l.reverse()

# 5、l.sort():列表内元素必须是同种类型才可以排序[字符串可以比大小，按照ASCI码表的先后顺序区别字符的大小]
# 字符串比较大小按照对应位置的字符依次pk
l = [11,-3,9,2]
l.sort(reverse=True) # 默认从小到大排，称之为升序
l.sort()
print(l)

# 了解：列表也可以比较大小，原理同字符串一样，但对应位置的元素必须是同种类型
l1 = [1,'abc','zaa']
l2 = [1,'abc','zac']
print(l1 < l2)

# 补充：
# 队列：first in first out （fifo） 先进先出

# 堆栈：last in first out （lifo） 后进先出