create database task22;
use task22;


create table college (student_id int, student_name varchar(50), department varchar(30), course varchar(30), year int, marks int, gender varchar(10));


insert into college (student_id, student_name, department, course, year, marks, gender) values
(1,'amit','cs','bsc cs',1,78,'male'),
(2,'neha','cs','bsc cs',1,85,'female'),
(3,'rahul','it','bca',2,69,'male'),
(4,'meera','it','bca',2,72,'female'),
(5,'arjun','ece','btech',3,91,'male'),
(6,'anjali','ece','btech',3,88,'female'),
(7,'vimal','cs','bsc cs',2,55,'male'),
(8,'kiran','cs','bsc cs',3,62,'female'),
(9,'priya','it','bca',1,74,'female'),
(10,'suresh','mech','btech',4,66,'male'),
(11,'deepa','mech','btech',4,59,'female'),
(12,'nithin','cs','bsc cs',1,81,'male'),
(13,'reshma','ece','btech',2,77,'female'),
(14,'abin','it','bca',3,68,'male'),
(15,'sneha','cs','bsc cs',2,92,'female');

-- q1
select department,count(*) from college group by department;

-- q2
select department,avg(marks) from college group by department;

-- q3
select course,max(marks) from college group by course;

-- q4
select department,min(marks) from college group by department;

-- q5
select year,count(*) from college group by year;

-- q6
select department,sum(marks) from college group by department;


-- q7
select gender, count(*) from college group by gender;

-- q8
select year,avg(marks) from college group by year;

-- q9
select course,count(*) from college group by course;

-- q10
select department, count(*) as total_students from college group by department;

-- q11
select department,count(*) as more_than_five from college group by department having more_than_five>5;

-- q12
select course from college group by course having avg(marks) > 70;

-- q13
select year from college group by year having count(*) > 10;

-- q14
select department from college group by department having max(marks) > 90;

-- q15
select course from college where gender='female' group by course having count(*) > 3;

-- q16
select department from college group by department having avg(marks) < 60;

-- ensure avg marks < 60 for a department (q16)
update college set marks=95 where student_id=15;

set sql_safe_updates = 0;


update college set course='bsc cs' where student_id in (2,8,9,15);
update college set marks = 50 where student_id in (10,11);
update college set marks = 90 where student_id in (3,7,13);
update college set course = 'bcom' where student_id = 14;


-- q15
select course from college where gender='female' group by course having count(*) > 3;

-- q16
select department from college group by department having avg(marks) < 60;

-- q17
select year from college group by year having sum(marks) > 500;

-- q18
select course from college group by course having count(*) < 5;















