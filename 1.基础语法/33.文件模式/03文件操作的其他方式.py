# 1、readline() 读取文件的一行
# 2、readlines() 读文件的每一行，再依次放到列表中 # 当读取的文件过大，有内存效率问题

# 二：写相关操作
# f.writelines():
with open('h.txt', mode='wt', encoding='utf-8') as fp:
    fp.write('1111\n2222\n3333\n')

    l=['11111\n','22222','wfawf']
    # for line in l:
    #     fp.write(line)
    fp.writelines(l)

    # 如果是纯英文字符，可以直接加前缀b得到bytes类型
    l = [
        b'11213agwga\n',
        b'ewga314\n'
    ]

# 补充：'上'.encode('utf-8')等同于bytes('上',encoding='utf-8')

# flush:主要用于写操作
with open('h.txt', mode='wt', encoding='utf-8') as fp2:
    fp2.write('哈哈哈')
