# not：就是把紧跟其后的那个条件结果取反
# ps：not与紧跟其后的那个条件是一个不可分割的整体
print(not 16>10)
print(not True)
print(not False)
print(not 10)
print(not None)

# and:逻辑与，and用来连接左右两个条件，必须两个条件同时为True,最终结果才为真
# 条件1 and 条件2
print(True and 10 > 3 and 10 and 0) # 条件结果全为真，最终结果才为True
# 偷懒原则

# or:逻辑或，or用来连接左右两个条件，但凡有一个条件为True,最终结果就为真
print(3 > 2 or 0)