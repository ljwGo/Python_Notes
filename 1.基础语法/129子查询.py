# ### part3 子查询
'''
子查询:嵌套查询
    1 子查询是查询的语句中又嵌套了另外一条sql语句,用括号()包起来，表达一个整体
    2 一般应用在from 子句后面表达一张表，或者where子句后面表达一个条件
    3 速度从快到慢 单表查询速度最快 -> 联表查询 -> 子查询

# 子查询
1 先选出平均年龄大于25岁的部门id
select dep_id from employee group by dep_id having avg (age) > 25
2 通过部门id，找部门名字
select id,name from department where id in (201,202)
3 综合拼接
select id,name from department where id in (select dep_id from employee group by dep_id having avg (age) > 25)
'''