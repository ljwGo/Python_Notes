# 异常错误:在代码语法正常的前提下,程序报错就是异常
'''
try:
	code1
except:
	code2
把可能存在问题的代码放到try这个代码块之后,
如果出现异常直接执行except这个代码块里面内容
如果没有异常,就不走except
'''
lst = [1,23]
try:
	print(lst[3])
except IndexError :
	print(1)
except KeyError :
	print(2)
except:
	print(3)

# 异常处理的扩展写法
# try ... finally 如果保措施也要执行,就是用finally
try:
	print(wangwen)
finally:
	print(1)
	print(2)
print(3)

# try ... except ... else





