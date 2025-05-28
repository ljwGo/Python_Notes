# ### 多项分支
"""
if 条件表达式1:
	code1
	code2
elif 条件表达式2:
	code1
	code2
elif 条件表达式3:
	code1
	code2
...
else:
	code1
	code2

如果条件表达式1成立,执行对应1号里面的代码块,否则向下执行
如果条件表达式2成立,执行对应2号里面的代码块,否则向下执行
如果条件表达式3成立,执行对应3号里面的代码块,否则向下执行
当其中一个执行,跳过接下来的所有代码块
...
如果都不成立
最后执行else 里面的代码块

elif : 最少0个 或者 任意多个
else : 最少0个 或者 1个
"""


youqian = True
youfang = True
youyanzhi = True
youche = False
youtili = False

if youqian == True:
	print("我要嫁给你")
elif youfang == True:
	print("我要嫁给你")
elif youche == True:
	print("我要嫁给你")
elif youyanzhi == True:
	print("我要嫁给你")
elif youtili == True:
	print("我要嫁给你")
else:
	print("你是个好人")

# ### 巢状分支 (单项分支,双项分支,多项分支的相互嵌套)
if youqian == True:
	if youfang == True:
		if youche == True:
			if youyanzhi == True:
				if youtili == True:
					print("我要嫁给你")
				else:
					print("你补点六味地黄丸")
			else:
				print("去韩国整整容")
		else:
			print("走开")
	else:
		print("走开")
else:
	print("走开")
#  if  的条件  不满足  是,只有在  同一作用域  中的  else  才会被执行

#python 特有的写法
height = input("你身高多少呢?")
if "1" <= height < "1.5":
	print("小强,你在哪里")
elif "1.5" <= height < "1.7":
	print("没有安全感")
elif "1.7" <= height < "1.8":
	print("帅哥,留个电话")
elif "1.8" <= height < "2":
	print("帅哥,你建议多一个女朋友吗?")
else:
	print("别骗我哇")

# str 是可以比较的  input默认的是转化成字符串

#通用写法
height = float(input("你的身高是多少呢?"))

if height >= 1 and height < 1.5:
	print("小强,你在哪里")
elif height >= 1.5 and height < 1.7:
	print("没有安全感")
elif height >= 1.7 and height < 1.8:
	print("帅哥,留个电话")
elif height >= 1.8 and height <= 2:
	print("帅哥,你建议多一个女朋友吗?")
else:
	print("别骗我哇")