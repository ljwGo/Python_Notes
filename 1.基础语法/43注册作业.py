# ### 自己的写法
with open('D:/360安全浏览器下载/python学习课程/课程附件/登记用户.txt',mode='r+',encoding='utf-8') as fp:
	lst1 = fp.readlines()

# 提取账号组成一个列表
lst_account = []
for i in lst1:
	lst2 = i.strip().split(':')
	lst_account.append(lst2[0])

while True:
	account = input('请输入您的账号:')
	if ' ' in account:
		print('含有非法符号')
	elif account == '':
		print('账号不能为空')
	elif len(account) < 7 or len(account) > 12:
		print('账号字数不符合要求')
	elif account in lst_account:
		print('该账号已注册')
	else:
		while True:
			mima = input('请输入您的密码:')
			if len(mima) < 7 or len(mima) > 12:
				print('密码字数不符合要求')
			else:
				mima2 = input('请确认您的密码:')
				if mima == mima2:
					print('恭喜你注册成功')
					with open('D:/360安全浏览器下载/python学习课程/课程附件/登记用户.txt', mode='a+', encoding='utf-8') as fp:
						fp.write('\n{}:{}'.format(account, mima))
					break
				else:
					print('两次输入的密码不一致')
		break

# ### 注册(老师的方法)
'''
1 注册的名字不能为空
2 注册的名字不能重复
3 确认两次密码的时候,要一致
'''
fp = open('user.txt',mode='a+',encoding='utf-8')
sign = True
while sign:
	accountlist = []
	username = input('请输入您的用户名:')
	if username == '' or ' 'in username:
		print('用户名含有非法字符')
	else:
		fp.seek(0)
		lst = fp.readlines()
		for i in lst:
			user,password = i.strip().split(':')
			accountlist.append(user)
		# 判断输入的用户名是否存在
		if username in accountlist:
			print('用户名已经存在')
		else:
			pwd = input('请输入密码:')
			while True:
				pwd2 = input('请输入您的密码:')
				if pwd == pwd2:
					print('注册成功')
					strvar = username + ':' + pwd + '\n'
					fp.write(strvar)
					sign = False
					break
				elif pwd2.upper() == 'Q':
					print('退出密码确认环节')
					break
				else:
					print('密码错误')

