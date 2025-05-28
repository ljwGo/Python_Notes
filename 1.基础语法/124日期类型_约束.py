# ### part1.数据类型 - 时间
'''
date YYYY-MM-DD 年月日(纪念日)
time HH:MM:SS 时分秒(体育竞赛)
year YYYY 年份值(酒的年份)
datetime YYYY-MM-DD HH-MM-SS 年月日 时分秒(登录时间,下单时间)

timestamp YYYYMMDDHHMMSS 自动更新时间(不需要手动写入，修改数据时候，自动更新)
    create table t2(dt datetime,ts timestamp)
    insert into t2 values(null,null)
    # 时间戳最多到2038年最后一天

mysql 内置函数
    now 获取当前时间
    concat 拼接各个参数
    user() 获取当前登录的用户
'''

# ### part2 约束
# 约束 : 对插入的数据类型进行限制，不满足约束的条件就直接报错
'''
unsigned 无符号
not null 不为空
default 设置默认值
unique 唯一约束，数据唯一不能重复
primary key 主键，唯一不为空的值，表达这条数据的唯一性
auto_increment 自动加一，(一般针对于主键 或者 unique进行自增)
zerofill 零填充，int（6），位数不够6，拿0来填充
foreign key 外键，把多张表通过一个字段联合在一起
'''

# unique 唯一约束，数据唯一不能重复[默认创建索引,通过索引可以加快查询速度，想当于]
'''默认允许插入多个null值'''

# primary key 主键，唯一不为空的值，表达这条数据的唯一性
# 原型 PRI 在一个表中，只能有一个字段标记成主键，一般标记id
'''
create table t11(id int not null unique , name char(15) default '张三')
create table t12(id int primary key);
两者同时存在，优先显示primary key 作为主键
'''

# auto_increment 自动加一，(一般针对于主键 或者 unique进行自增)
'''create table t13(id int primary key auto_increment,name varchr(11) default 'en')'''

# 删除
'''
    1 delete from 表 where 条件(删除数据，保留id)
    
    2 turncate table 表名 （删除数据，重置id，重置表）
'''

# ### part3
# 1 联合唯一索引:unique(字段1，字段2，...) 把多个字段拼接在一起表达一个唯一的数据
# 联合唯一索引（在非空的情况下，显示为主键 PRI）
'''
create table t1_server(id int,server_name char(10) not null,ip char(15) not null ,port int not null , unique(ip,port));
insert into t5 values(1,'aa','192.0.0.1',3666);
insert into t5 values(1,'aa','192.0.0.1',3666);
insert into t5 values(1,'aa','192.0.0.1',3666);

alter table t5 add primary key(id);
'''

# foreign key 外键,把多张表通过一个字段联合在一起
'''
student1:
    id name age classname address hobby...
    1   changyuan 81 python8 世外桃源
    2   wangwen   7  python8 世外桃源
    3   zhangshan 18 python8 世外桃源
'''
# 为了避免出现过多的字段，可以采取分表的形式，来减少冗余数据，提升查询的效率；
'''外键的要求：主动关联的这张表设置外键,要求被关联的表字段必须具有唯一属性（unique 或者 primary key）
create table student1(id int primary key auto_increment,
name varchar(12) not null,
classid int unique,
foreign key(classid) references class1(id)

create table class1(id int ,classname varchar(255));
# 设置classid为主键或者唯一索引
alter table class1 add unique(id);

create table student1(id int primary key auto_increment,name varchar(15),classid int))
insert into class1 values(1,'python6')
insert into class1 values(2,'python7')
insert into student1 values(null,'changyuan',1)
insert into student1 values(null,'zhangsan',2)
insert into student1 values(null,'lisi',2)
'''
# 删除class1 如果这条数据在多张表中被使用，直接删除会报错，因为有外键关联
'''
delete from class1 where id = 1
# 把有关联的数据删除之后，才可以删除
delete from student1 where id = 2
delete from class1 where id = 1

# 联级删除 联级更新（谨慎操作）
联级删除 on delete cascade
联级更新 on update cascade
在创建连接时在后面加上这两句话

# 7 带有exists关键字的子查询
子查询可以单独作为一个字句，也可以作为一个表或者某个字段
一般用在from where select 子句后面
通过查询出来的临时表，可以跟任意的表重新拼接，组成更大的表，在
'''