# ### python 操作mysql
import pymysql

'''
# 1 基本语法
# 创建链接
conn = pymysql.connect(host='192.168.169.129', user='root', password='123456', database= 'ch1', charset= 'uts8', port=3306)
# 创建游标对象，通过该对象可以进行增删改查操作
cursor = conn.cursor()
# 执行sql语句
sql = 'select * from employee'
# 返回的结果是查询的总条数
res = cursor.execute(sql)
print(res)
# 获取数据
res = cursor.fetchone()
print(res)
# 释放游标对象
cursor.close()
# 关闭数据库连接
conn.close()
'''

# 2 创建/删除 数据库
conn = pymysql.connect(host='192.168.169.129', user='root', password= '123456', database= 'db1', charset='utf8', port= 3306)
cursor = conn.cursor()
sql = """
create table pt1(
id int auto_increment primary key,
first_name char(10) not null,
last_name char(10) not null,
age tinyint unsigned,
sex tinyint,
money float
)
"""
res = cursor.execute(sql)
print(res)

# 查看表结构
'''
sql = 'desc pt1'
res = cursor.execute(sql)
print(res) # 返回字段数量
print(cursor.fetchone())
'''

# 删除表,配合异常处理抑制错误，防止程序终止
'''
sql = ' drop table pt1 '
try:
    cursor = executer(sql)
except:
    pass
'''

cursor.close()
conn.close()

# ### 3 事务处理 只有执行commit命令提交，才能将数据保存到数据库
'''
begin 开始事务
commit 确认操作
rollback 回滚操作
'''
conn = pymysql.connect(host='', user='', password= '', database= '', charset='', port='')
cursor = conn.cursor()
sql1 = 'begin'
sql2 = 'select * from t1 limit 1'
cursor.execute(sql1)
cursor.execute(sql2)
cursor.close()
conn.close()
