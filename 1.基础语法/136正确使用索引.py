'''
import time
import pymysql
conn = pymysql.connect(host='192.168.169.129', user='root', password='123456', database='suoyin')
cursor = conn.cursor()
sql = 'insert into use_index(name) values(%s)'
t1 = time.time()
for i in range(3000000):
    cursor.execute(sql, (i,))
    conn.commit()
t2 = time.time()
print(t2 - t1)
cursor.close()
conn.close()
'''

# 备注信息 text 全文索引 , 可使用fulltext 多数情况下使用第三方软件sphinx来运行

# 3 常用的索引数据结构
'''
hash 类型的索引:数据在内存中，通过键来获取值，查询单条数据最快，一个范围的数据慢
b-tree:理想层级是三层，可支撑百万条数据
'''

# 4 创建索引
# create table t1(id int,name varchar(255),索引类型 索引名(索引字段))
# create table t1(id int,name varchar(255));create 索引类型 索引名 on 表名(字段名)
# alter table t1 add 索引类型 索引名(索引字段)

# 删除索引 drop 索引类型 索引名 on 表名

# 1 把频繁作为搜索条件的字段作为索引，查询的是一个范围的数据，不能命中索引 例如< > <= >=

# 2 选一个字段作为索引，这个列(字段)必须是区分度较高的字段

# 3 不推荐在where条件上使用索引字段运算，不能命中索引

# 4 使用函数不能命中索引(用在索引列)



