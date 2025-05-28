# 1、什么是哈希hash
#   hash是一类算法，该算法接受传入的内容，经过运算得到一串hash值
#   hash值得特点：
#               1、只要传入的内容一样，得到得hash值必然一样===》要用明文传输密码文件完整性
#               2、无法将hash值反解成内容===》把密码做成hash值，不应该在网络传输明文密码
#               3、只要使用的hash算法不变，无论效验得内容有多大，得到的hash值长度是固定的

# 2、hash得用途：密文加密和文件完整性效验

# 3、如何用
import hashlib
m = hashlib.md5()
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
m.hexdigest()

m1 = hashlib.md5('he'.encode())
m1.update('llo'.encode())
m1.update('world'.encode())
m1.hexdigest()