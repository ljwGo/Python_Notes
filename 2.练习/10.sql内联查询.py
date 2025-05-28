'''
1 查询所有的课程的名称以及对应的任课老师姓名
# 内联写法
select
    course.cname,teacher.tname
from
    course inner join teacher on course.teacher_id = teacher.tid

# where 写法
select
    course.name,teacher.tname
from course,teacher
where
    course.teacher_id = teacher.tid

2 select gender,count(*) from student group by gender

3
select
    *
from
    course inner join score on course.cid = score.course_id
    inner join student on score.student_id = student.sid
where
    course.cname = 'wuli' and score.num = '75'

4
select student.sname,avg(num) from score inner join student on score.student_id = student.sid group by student_id having avg(num) > 80

5
select
    student.sname,count(*),sum(score.num)
from
    score inner join student on score.student_id = student.sid
group by
    student_id

6
select
    count(*)
from
    teacher
where
    tname like '李%'

7
# distinct 自动去重
select distinct(字段名) from 表名

select
    student.sname
from
    teacher,course,student,score
where
    teacher.tid = course.teacher_id
    and
    course.cid = score.course_id
    and
    score.student_id = student.sid
    and
    tname = 'lipin'

8







'''