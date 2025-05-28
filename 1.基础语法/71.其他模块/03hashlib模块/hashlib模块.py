import hashlib,random,os.path
# 基本用法
# 1 创建一个md5的算法对象
hs = hashlib.md5()
# 2 把要加密的字符串通过updata跟新到hs这个对象当中进行运算
'''数据类型需求：二进制字节流'''
hs.update('abcd'.encode('utf-8'))
# 3 返回32位16进制的字符串
res = hs.hexdigest()
print(res,type(res),len(res))

# 加盐 （加key = wW123#）
# 目的:是用户的密码变得复杂，不容易破解
# 参数是二进制字节流
hs = hashlib.md5('wW123#'.encode())
hs.update('abcd'.encode())
res = hs.hexdigest()
print(res,type(res),len(res))

# 动态加盐
res = str(random.randrange(100000,1000000))
hs = hashlib.md5(res.encode('utf-8'))
hs.update('abcd'.encode())
res = hs.hexdigest()
print(res)

'''
md5 加密速度快，安全性一般
sha 加密速度稍慢，安全性稍好
'''
hs = hashlib.sha1()
hs.update('abcd'.encode())
res = hs.hexdigest()
print(res,len(res),type(res))

hs = hashlib.sha512()
hs.update('abcd'.encode())
res = hs.hexdigest()
print(res,len(res))

# ### hmac
import hmac
'''
hmac 也是一个加密算法，相对来说，字符串更难破解
'''
#key = b'123'
#msg = b'abcd'
#hm = hmac.new(msg,key)
#res = hm.hexdigest()
#print(res)

# 动态加盐
"""
import os
res = os.urandom(16)
print(res,len(res))
key = b'abcd'
hm = hmac.new(key,res)
res = hm.hexdigest()
print(res)
"""

# ### 文件效验
def check_md5(file):
    with open(file,mode='rb') as fp:
        hs = hashlib.md5()
        hs.update(fp.read())
    return hs.hexdigest()

res1 = check_md5('ceshi1.txt')
res2 = check_md5('ceshi2.txt')
print(res1,res2)

# 针对大文件的效验
hs = hashlib.md5()
hs.update('ig牛逼'.encode())
hs.update('是的'.encode())
res = hs.hexdigest()
print(res)

def check_md5(file):
    hs = hashlib.md5()
    with open(file,mode='rb') as fp:
        while True:
            # 最多读取5个字节
            content = fp.read(5)
            if content:
                hs.update(content)
            else:
                break
    return hs.hexdigest()

print(check_md5('ceshi3.txt'))

def check_md5(file):
    file_size = os.path.getsize(file)
    hs = hashlib.md5()
    with open(file,mode='rb') as fp:
        while file_size:
            res = fp.read(10)
            hs.update(res)
            file_size -= len(res)
    return hs.hexdigest()

check_md5('ceshi3.txt')











