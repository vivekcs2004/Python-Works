create database task22_12;
use task22_12;

create table students (student_id int primary key, student_name varchar(50), department_id int);

create table departments (department_id int primary key, department_name varchar(30));


insert into students (student_id,student_name,department_id) values (101,'amit',1),(102,'neha',1),(103,'rahul',2),(104,'meera',3),(105,'arjun',null),(106,'kiran',5),(107,'priya',2),(108,'vimal',null);

insert into departments (department_id,department_name) values (1,'computer science'),(2,'electronics'),(3,'mechanical'),(4,'civil'),(5,'mathematics');

-- q1
select d.department_name,s.student_name from departments d left join students s on d.department_id=s.department_id;

-- q2
select s.* from students s join departments d on s.department_id=d.department_id where d.department_name='computer science';

-- q3
select d.department_name,count(s.student_id) from departments d left join students s on d.department_id=s.department_id group by d.department_name;

-- q4
select s.student_name,d.department_name from students s join departments d on s.department_id=d.department_id order by d.department_name;

-- q5
select s.student_name,d.department_name from students s join departments d on s.department_id=d.department_id;

-- q6
select s.student_name,d.department_name from students s left join departments d on s.department_id=d.department_id;

-- q7
select d.department_name,count(s.student_id) from departments d left join students s on d.department_id=s.department_id group by d.department_name;

-- q8
select d.department_name,s.student_name from departments d left join students s on d.department_id=s.department_id;

-- q9
select d.department_name,s.student_name from departments d left join students s on d.department_id=s.department_id;

-- q10
select s.student_name,d.department_name from students s join departments d on s.department_id=d.department_id;

-- q12
select s.student_id,s.student_name,s.department_id,d.department_name from students s join departments d on s.department_id=d.department_id;

-- q14
select d.department_name,s.student_name from departments d join students s on d.department_id=s.department_id order by s.student_name;












