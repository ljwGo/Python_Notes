import struct
'''
pack:把任意长度的数字转化为具有4个字节固定长度的字节流
unpack:把4个字节值恢复成原本的数字，返回的是元组
'''

# i => int 要转换的当前数据是一个整型
res = struct.pack('i',999999)
print(res)
print(len(res))

# i => 把res转化为整形，返回的是元组
tup = struct.unpack('i',res)
print(tup)