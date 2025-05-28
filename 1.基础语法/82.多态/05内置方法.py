# bin() 转化为二进制
# oct() 转化为8进制
# hex() 转化为16进制

# chr(65) 将二进制码转化为ascii编码表对应的字符
# ord('A') 获取对应的ascii编码表对应的二进制数

# 掌握 =======>
# dir(obj/cls) 获取属性
# divmod(10000,33) 返回10000除以33的商和余数
# enumerate(iterable) 返回迭代器，每个项是索引和值的元组
# isinstance() 判断一个对象是否是一个类的实例（用于类型判断）

# eval() 将eval括号中的字符串作为python命令执行
# exec() 支持更复杂的python语句

# zip() 将两个iterable依次拼接成小元组
it = zip(['aaa','bbb','ccc'],(111,222,333))
for i in it:
    print(i)
