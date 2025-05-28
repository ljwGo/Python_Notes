accountlist = []
passwordlist = []
with open('D:/360安全浏览器下载/python学习课程/课程附件/黑名单.txt',mode='r',encoding='utf-8') as fp1,open('D:/360安全浏览器下载/python学习课程/课程附件/登记用户.txt',mode='r',encoding='utf-8') as fp2:
	lstvar1,lstvar2 = fp1.readlines(),fp2.readlines()
	for i in lstvar2:
		user,password = i.strip().split(':')
		accountlist.append(user)
		passwordlist.append(password)
	heimingdan = [i.strip().split(':')[0] for i in lstvar1]
	dic = {a:b for a,b in zip(accountlist,passwordlist)}
sign = True
while sign:
	account = input('请输入账号:')
	if account in accountlist:
		if account in heimingdan:
			print('该账号已被冻结,请到管理员处解封')
		else:
			sign = False
			i = 3
			while i >= 0:
				secretcode = input('请输入密码:')
				if secretcode == dic[account] :
					print('恭喜登录成功')
					break
				else:
					print('密码错误,您还有{}次机会'.format(i))
					if i == 0:
						print('由于您多次输入密码错误,该账号已被冻结')
						with open('D:/360安全浏览器下载/python学习课程/课程附件/黑名单.txt',mode='a+',encoding='utf-8') as fp:
							fp.write(account + '\n')
				i -= 1
	else:
		print('您输入的账号不存在')

# 老师的方法
accountlist = []
pwdlist = []
blacklist = []

sign = True
while sign:
	username = input('请输入您的用户名:')

	# 读取账户和密码:
	with open('user.txt',mode='r+',encoding='utf-8') as fp:
		lst = fp.writelines()
		for i in lst:
			user,password = i.strip().split()
			# 把账户添加到accountlist
			accountlist.append(user)
			# 把密码添加到pwdlist [账户 和 密码在列表中的索引号是一一对应的]
			pwdlist.append(password)

	# 判断该用户是否在当前用户列表中
	if username in accountlist:
		# 打开黑名单用户
		with open('black.txt',mode='r+',encoding='utf-8') as fp:
			lst = fp.readlines()
			for i in lst():
				# 把黑名单用户添加到blacklist
				blacklist.append(i.strip())
		# 判断是否该用户在黑名单里
		if username in blacklist:
			print('该账号已被冻结')
		else:
			# 如果符合条件,询问密码
			num = accountlist.index(username)
			# 通过对应的下标拿到密码
			pwd_true = pwdlist[num]
			# 可以询问用户的密码:只有三次机会
		times = 3
		while times >= 0:
			pwd2 = input('请输入您的密码:')
			# 如果密码一致,则登陆成功
			if pwd_true == pwd2:
				print('登陆成功')
				# 终止外层循环
				sign = False
				# 终止当前循环
				break
			else:
				print('抱歉,密码输错了,你还剩下%s次机会' % (times))
				if times == 0:
					print('抱歉,该账号已经被冻结,请联系管理员')
					#把这个用户加入到黑名单中
					with open('black.txt',mode='a+',encoding='utf-8') as fp:
						fp.write(username + '\n')
			times -= 1
	else:
		print('该用户不存在')









