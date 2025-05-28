# ### 文件操作
# 打开模式
# w write 写入模式
# 文件不存在则创建文件,存在的话打开清空内容,并且将文件指针放在文件的开头

# r read 读取模式
# 文件不存在则报错!存在的话则打开文件,并且将文件指针放在文件的开头

# a append 追加模式
# 文件不存在则创建文件,存在的话则打开文件,*并且将文件指针放在文件的末尾*

# 扩展模式 (配合打开模式的辅助模式,自己单独不能使用)
#  +  plus  增强模式(可以让文件具有读写功能)
#  b  bytes bytes模式(二进制字节流)

#模式一共16(常用为12种)种
'''
w,w+,wb,wb+
r,r+,rb,rb+
a,a+,ab,ab+
'''

'''
fp = open('文件名称',mode = 模式,encoding = 编码集)
fp(文件io对象) (java中称文件句柄)
i : input 输入
o : output 输出
'''

# 1文件的写入内容
# 打开冰箱(打开文件)
fp = open('ceshi1.txt',mode='w',encoding= 'utf-8')
# 把大象放进去(写入内容)
fp.write('把大象塞进去')
# 关上冰箱(关闭文件)
fp.close()

# 2文件的读取操作
# 打开文件
fp = open('ceshi1.txt',mode='r',encoding='utf-8')
# 读取内容
res = fp.read()
# 关闭文件
fp.close()
print(res)

#b'abc' b'你好' 是错误的 b二进制字节流的编码集中没有中文对应的编码

# 3 转化成二进制字节流
# 将字符串和字节流(Bytes流)类型进行转换(参数写成转化的字符编码格式)
	#encode() 编码 将字符串转化为字节流(Bytes流)
	#decode() 解码 将Bytes流转化为字符串

strvar = '我爱你'
res = strvar.encode('utf-8')
print(res)
strnew = res.decode('utf-8')
print(strnew)

# 三个字节对应一个中文字符
res = b'\xe7\x88\xb1'
strnew = res.decode('utf-8')
print(strnew)

# 4 写入字节流 (不要指定字符编码encoding)
fp = open('ceshi2.txt',mode='wb')
str_Bytes = '我爱你,亲爱的菇凉'.encode('utf-8')
fp.write(str_Bytes)
fp.close()

# 5 读取字节流 (不要指定字符编码encoding)
fp = open('ceshi2.txt',mode='rb')
res = fp.read()
fp.close()
print()

# 复制图片的操作(图片,音乐,视频...二进制字节流模式)
# 读取旧图片
fp = open('集合的交并补.png',mode='rb')
str_bytes = fp.read()
fp.close()

# 创建新图片
fp = open('集合2.png',mode='wb')
fp.write(str_bytes)
fp.close()
