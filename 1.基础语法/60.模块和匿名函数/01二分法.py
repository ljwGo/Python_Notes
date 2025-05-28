# 算法：是高效解决问题的办法
# 算法之二分法

# 需求：有一个按照从小到大顺序排列的数字列表
#       需要从该数字列表中找到我们想要的那个数字
nums = [-2,3,4,5,7,22,33,88,123]
find_num = 22
# 方案一：整体遍历效率太低
for num in nums:
    if num == find_num:
        print('find it')
        break

# sort()排序
# 方案二：二分法
def outter(find_num):
    def find(num_l):
        half_len = len(num_l)//2
        mid_val = num_l[half_len]
        if half_len == 0:
            print('找的值不存在')
            return
        if find_num > mid_val:
            l = num_l[half_len+1:]
            find(l)
        elif find_num < mid_val:
            l = num_l[:half_len]
            find(l)
        else:
            print('找到了')
    return find
