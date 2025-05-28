# ### python 操作 mysql 增删改查
import pymysql
'''
    python 操作 mysql 默认开启事务,必须在增删改之后，提交数据
    才会对数据库产生变化，否则默认回滚
    提交数据 conn.commit()
    回滚数据 conn.rollback()
    
    execute 执行sql指令
    execute 执行多条sql(插入时，可以使用)
'''
conn = pymysql.connect(host='192.168.169.129', user='root', password='123456', database='pymysql_ope')
# 查询数据，默认返回的是元组，可以设置参数，返回字典 pymysql.cursors.DictCursor
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 增
sql = 'insert into operation(name,money,address,sex) values(%s,%s,%s,%s)'
# 一次插入一条数据
res = cursor.execute(sql, ('lisi', '30000', 'guangdong', '1'))
print(res)
# 一次插入多条数据
res = cursor.executemany(sql, [('zhangsan', '2222222', 'yunnan', '2'), ('wangwem', '1981917', 'guangxi', '1')])
# 获取最后一条数据的id号 (只能针对于插入单条数据的id)
print(cursor.lastrowid)
# 如果执行多条数据executemany，通过查询的方式获取
# select id from 表名 order by id desc limit 1

# 删
sql = 'delete from operation where id = %s'
cursor.execute(sql, (4,))

# 改
sql = 'update operation set money = %s where id = %s'
res = cursor.execute(sql, (6000000,3))
print(res)
if res:
    print('更新成功')
else:
    print('更新失败')

# 查
sql = 'select * from operation'
res = cursor.execute(sql)
print(res)

# 获取一条数据 fetchone
res = cursor.fetchone()
print(res)

# 获取多条数据 fetchmany 默认搜索一条，从上一次查询的数据往下数，类似迭代器
data = cursor.fetchmany(3)
print(data)

# 获取所有数据 fetchall 从上一次查询的数据往下数，类似迭代器
res = cursor.fetchall()
print(res)

for row in data:
    name = row['name']
    money = row['money']
    address = row['address']
    if row['sex']:
        sex = '男'
    else:
        sex = '女'
    print('{},{},{}人,收入{}'.format(name, sex, address, money))

# 可以自定义查询的位置
# 相对滚动
sql = 'select * from operation where id > 10'
res = cursor.execute(sql)
print(res)
# 先获取一条 11
res = cursor.fetchone()
print(res)

# 再向后滚动2条 13
cursor.scroll(2,mode='relative')
res = cursor.fetchone()
print(res)

# 绝对滚动 相对于最开始第一条数据进行运算
sql = 'select * from operation where id > 10'
res = cursor.execute(sql)
cursor.scroll(0, mode='absolute')
print(cursor.fetchone())
cursor.scroll(3, mode='absolute')
print(cursor.scroll())

# 在进行增删改的时候，必须替换数据，才真正进行修改，默认开启事务处理
conn.commit()
# 资源释放 游标对象和连接对象
cursor.close()
conn.close()

# 导出数据库 与 导入数据库
'''
先退出mysql 执行mysqldump -uroot -p123456 pymysql_ope [可指定要要导出的具体表，而不是全部] > pymysql_ope.sql
source ~/ceshi01.sql
'''