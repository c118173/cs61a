-- 2.1
select name from records where supervisor="Oliver Warbucks";

-- 2.2
select * from records where name=supervisor;

-- 2.3
select name from records where salary>50000 order by name;

-- 3.1
select a.day, a.time from meetings as a, records as b
  where b.supervisor = "Oliver Warbucks" and a.division=b.division;
  
-- 3.2
select a.name, b.name from records as a, records as b, meetings as c, meetings as d 
  where a.division=c.division and b.division=d.division and c.time=d.time and a.name<b.name;
  
-- 3.4
select a.name from records as a, records as b
  where a.supervisor=b.name and a.division<>b.division
 
-- 4.1
select sum(salary) from records group by supervisor;

-- 4.2
select day from records as a, meetings as b 
  where a.division=b.division group by day having count(*)<5;

-- 4.3
select a.division from records as a, records as b 
  where a.division=b.division and a.name<b.name 
  group by a.division having max(a.salary+b.salary)<100000;
  
-- 5.1
create table num_taught as select professor, course, count(professor) as times from courses 
  group by professor, course;
  
-- 5.2
select a.professor, b.professor, a.course from num_taught as a, num_taught as b 
  where a.times=b.times and a.course=b.course and a.professor<b.professor;
  
-- 5.3
select a.professor, b.professor from courses as a, courses as b 
  where a.course=b.course and a.semester=b.semester and a.professor<b.professor 
  group by a.course, a.professor, b.professor having count(*)>1;
