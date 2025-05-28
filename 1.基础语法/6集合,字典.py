# ### set 集合类型作用:做交叉并补操作
"""
无序性
"""
setvar = {"周杰伦","李宇春","张三"}
print(setvar)
print(type(setvar))

#是否可以获取集合当中的值?不可以
#print(setvar[0])

#是否可以修改集合当中的值?不可以
#setvar[0] = "我来了"

setvar = {"周杰伦","林志颖","伍佰",str(12)}
print(setvar)

# ### dict 字典类型
'''由键值对存储的数据'''

#定义一个空字典
dictvar = {}
print(dictvar)
print(type(dictvar))

#定义一个普通字典
"""
键和值用冒号隔开,键值对之间用逗号隔开
{键1:值1,键2:值2,键3:值3...}
"""
dictvar = {"我":"小明","他":"张三","她":"李四"}
print(dictvar)
print(type(dictvar))

#1获取字典中的值
print(dictvar["我"])

#2修改字典中的值
dictvar["我"] = "赖建威"
print(dictvar["我"])


# ### 集合的值 字典的键 需要的是可哈希数据(可以通过哈希算法进行运算的数据)这就是集合和字典的值无序的原因
#但集合和字典本身不能用哈希算法
#哈希算法: 可以均匀的把数据分散在内存当中进行存储的算法(对数据进行加密);
#哈希碰撞???
"""
可哈希数据不可改变的数据
哈希算法要求数据必须可哈希:
可哈希数据(不可变):
    Number(int float bool complex) str tuple
不可哈希数据(可变):
    list(值可改变) set(顺序改变) dict(顺序改变)
"""

#字典
dictvar = {1:1,5.88:"anv",False:111,7+2j:"家","12341":"wewaf",(1,2,3):"wjef"}
#dictvar = {["name","war","mane"]:"wo"}   错误写法
print(dictvar)
print(dictvar[(1,2,3)])
listvar = [{1,2,3},{1:"j"},["我","你"]]   #列表中的值不要求是否可哈希
print(listvar)

# 集合
#setvar = {1,6.2,True,4+1j,"ea",("wf",1,1),(1,[1,2,3])}
#在可哈希数据中镶嵌不可哈希数据任然不可以 例如集合的值的一个元组中有一个列表











