# ### part 单表查询
# sql 查询语句的完整语法
'''select .. from .. where .. group by .. having .. order by .. limit ..'''

# 一 where 条件的使用
'''功能:对表中的数据进行筛选过滤'''

'''
    语法:
        1 判断的符号
        = > < >= <= != <>不等于
        2 拼接条件的关键字
        and or not
        3 查询的区间范围值 between
        between 小值 and 大值 [小值，大值] 查询两者之间这个范围的所有数据
        4 查询具体某个值的范围 in
        in(1,-9,-10,'a') 指定范围
        5 模糊查询 like '%' 通配符
            like '%a' 匹配以a结尾的任意长度字符串
            like 'a%' 匹配以a开头的任意长度字符串
            like '%a%' 匹配含有a字母的任意长度字符串
            like '_a' 个数一共2个字符，必须以a结尾，前面这个字符随意
            like 'a__' 个数一共3个字符，必须以a开头，后面这两个字符随意

'''
# 1 但条件的查询
# 查询部门是sale的所有员工姓名
# select 字段名 from 表名 where 条件1 and 条件2 and ...

# 搜索 null 关键字 要使用is，而不是=
# select name from ch1 where post is null

# concat 拼接
# select concat('姓名',name，'地址',address) as aaa from ch1;
# concat_ws(拼接的符号，参数1，参数2，参数3)
# 可以在sql中使用四则运算

# 二 分组 group by 子句 分组，分类
'''group by 对数据进行分类。 group by 字段名 后面字段就是要搜索的字段'''
# select name from ch1 group by name;
# group_concat 按照分组形式进行字段的拼接
# select group_concat(adress),name from ch1 group by name

# 聚合函数
    # 统计总数 count
    # select count(*) from employee
    # select * from employee
    # 统计最大值
    # select concat(name),max(salary) from emplovee
    # 最小值 min 平均值 avg 总和 sum

# 三 having 查询数据之后再进行过滤，一般配合group by使用，进行分组后过滤
# select 字段名 from 表名 group by 字段名 having 条件

# 四 order by 排序 按照什么字段进行排序
# select * from 表名 order by 字段 (默认升序)
# select * from 表名 order by 字段 desc (降序)

# 五 limit 限制查询的条数(数据分页)
# limit m,n m代表从第几条开始查询，n代表查询几条 m=0 代表的是第一条
# select * from laonanhai limit 0,5 从第一条开始查，查5条

# ### 多表查询
    # 内连接:(内敛查询 inner join) : 量表或者夺标满足条件的所有数据查询出来
'''
两表查询
select 字段 from 表1 inner join 表2 on 条件
多表查询
select 字段 from 表一 inner join 表2 on 条件 inner join 表3 .。。
# where 实现的就是内联查询
'''
    # 外连接
    # 1 左连接 (左联查询 left join)
    # 2 右连接 (右联查询 right join)
    # 3 全连接 (union)把所有数据合并起来结合成一个大表