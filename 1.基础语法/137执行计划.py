# ### part1
'''
表的数据行
    数据量越大，树的高度就会变高，理论上3层索引树高度就可以达到百万计数据
    解决:可以使用分表，分表，数据库缓存，解决数据过大问题

解决键值过长
    该索引字段存储数据太大，每个叶子点默认可以存储16K，超过范围增加叶子节点
    解决：前缀索引（截取前10个长度）

数据类型
    char ， varchar

# ### part2 执行计划分析
desc/explain sql
# 执行计划：在一条sql执行之前，指定执行的方案
    desc select * from s1

select_type
simple 代表的是简单查询（不包括子查询，union）
primary sql嵌套中的主查询（最外层）
subquery sql嵌套中的子查询（非最外层）
derived 衍生查询（把子查询结果作为一张临时表）

table
再多表时，子查询的时候，关注出现问题的那张表是谁

type
把执行计划的类型，优化级别从低到高，前提都有索引，至少达到range，ref
all < index < range < ref < eq_ref < const < system

all 全表扫描(不走索引)
在大范围内查询 > < >= <= != between .. and   in   not in   like '%a%'
where条件中有计算，有函数
数据类型不匹配(隐式索引)
索引失效，数据信息过旧，发生树状结构变更的时候，可能产生索引索引对不上实际数据的情况

index 全索引扫描
扫描整个索引树，才能获取到数据，失去索引的意义
select count(*) from s1;

range 索引范围扫描(注意点:如果范围过大，不能命中索引)
select * from s1 where id < 10 type => range
select * from s1 where id < 1000000 type => all

注意如果范围过大,不能命中索引
如果范围适当，可以命中索引

or 和 in 语句可以进行优化的,
desc select * from s1 where id in (1,2,3);
union all 比 union 速度快,因为union多了一步去重操作

desc select * from s1 where id = 1
union all
select * from s1 where id = 2

ref
普通索引查询
desc select * from s1 where email = 'xboyww'

eq_ref 唯一性索引
应用在多表联查中，关联字段只能是主键或者唯一索引，表之间是1对1的关系并且数据条数相同，查询具体的某个带索引的字段
搜索的是索引字段，联表的数据必须一致

const:主键或者唯一索引(单表)

system(了解)
只有一条数据的系统表或者衍生表(子查询出来的临时表)只有一条数据主查询
create table system_index(id int , name varchar(10))
insert into system_index(1,'a')

possible_key : 可能用到的索引是谁
show index from 表名 查看表的索引

key : 实际用到的索引

key_len : 判断联合二索引覆盖的索引长度
    预留一个字节，在没有not null 约束的时候，加上一个字节，标记是空还是非空
    utf8 预留的最大字节数是4个字节，通常情况下，一个中文3个字节，一些个别生僻字4个字节存储
    varchar 每次存储数据的时候，系统底层要额外预留2个字节
            有not null 没有not null
    tinyint    1字节       2
    int        4字节       5
    char(5)  5*4字节   5*4+1
    varchar(5) 5*4+2  5*4+2+1

    在创建联合索引的时候，实际是根据参数的不同，创建了不同的索引树，命中一个即可，符合最左前缀原则
'''