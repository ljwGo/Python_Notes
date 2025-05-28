# 1、什么是序列化
#   序列化指的是把内存的数据类型转换成一个特定格式的内容
#   该格式的内容可用于存储或者传输给其它平台使用

# 土办法：
# {'aaa':111}--->序列化str({'aaa':111})--->"{'aaa':111}"
# {'aaa':111}<---反序列化eval{"{'aaa':111}"}<---"{'aaa':111}"

# 2、为何要序列化
#   序列化得到结果=>特定的格式的内容有两种用途
#   1、可用于存储=》用于存档
#   2、传输给其他平台使用=》跨平台数据交互=》跨平台数据交互

# 强调：
#       针对用途2的特定一格式：应该是一种通用的、用够被所有语言识别的格式=》json
#       针对用途1的特定一格式：应该是一种通用的、只能被python识别=》pickle

#3、如何序列化与反序列化
# 复杂的序列化
import json
json_res = json.dumps([1, 'aaa', True, False])
print(json_res, type(json_res))
with open('text.json', mode='wt', encoding='utf-8') as f:
    f.write(json_res)
# 简单的序列化
with open('text.json', mode='wt', encoding='utf-8') as f:
    json.dump([1,'aaa','www'],f)

# 反序列化
# 复杂的反序列化
with open('text.json', mode='rt', encoding='utf-8') as f:
    res = f.read()
    res2 = json.loads(res)
    print(res2)
# 简单的序列化
with open('text.json', mode='rt', encoding='utf-8') as f:
    print(json.load(f))

# json补充
# 一定要弄清楚json格式，不要与python混淆
# setvar = json.dumps({222,'eee','ennn'})
# l = json.loads("[11,1.2,true,'www']")

# l = json.loads(b'[11,1.2,true,"www"]')
# res = json.dumps({'name':'哈哈哈'})

# 猴子补丁
# json.dumps = 其他更好的dumps功能
# 原理：模块导入只有首次导入时才会执行，后续导入直接使用第一次导入时产生的内存空间中

# 在入口文件处
# ujson效率更快，用法与json一样
# import ujson
# def monkey_json():
#     if __name__ == '__main__':
#         json.dumps = ujson.dumps
#         json.loads = ujson.loads

# 5.pickle模块
import pickle
res = pickle.dumps({1,2,3,4})
print(res, type(res))

pickle.loads(res)

# python2不支持protocol>2
# 在使用pickle序列化中文时，应该指定protocol的值为2
# pickle.dumps('你好啊',f,protocol=2)