# ### sql 注入攻击
# 创建一张表
'''
create table usr_pwd(
id int unsigned primary key auto_increment,
username varchar(255) not null,
password varchar(255) not null
)
'''

# 1 注入攻击
import pymysql
user = input('user:'.strip())
pwd = input('password:'.strip())
conn = pymysql.connect(host='192.168.169.129', user='root', password='123456', database='bd2')
cursor = conn.cursor()
sql = "select * from usr_pwd where username='%s' and password='%s' " % (user, pwd)
res = corsur.execute(sql)
if res:
    print('登陆成功')
else:
    primt('登陆失败')
'''-- 是注释，加入or True就可以破解登录'''
# 列如 afewgwg' or 2=2 -- awegaweg # (-- 后面要有空格)

cursor.execute(sql)
# 2 解决办法
'''
使用预处理机制,可以避免绝大多数的sql注入问题;
execute 默认参数是一个sql语句,如果把sql语句和参数值分开执行，就开启预处理
execute(sql,(参数1，参数2，参数3...))
'''

conn = pymysql.connect(host='192.168.169.129', user='root', password='123456', database='bd2')
cursor = conn.cursor()
sql = "select * from usr_pwd where username=%s and password=%s"
res = cursor.execute(sql,(user,pwd))