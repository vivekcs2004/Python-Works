create database emp;
use emp;

create table empl (
    emp_id int primary key,
    emp_name varchar(50),
    department varchar(30),
    salary int,
    age int,
    city varchar(30)
);
insert into empl (emp_id, emp_name, department, salary, age, city) values
(1, 'amit', 'it', 50000, 28, 'kochi'),
(2, 'neha', 'hr', 42000, 32, 'trivandrum'),
(3, 'rahul', 'finance', 60000, 35, 'chennai'),
(4, 'arjun', 'it', 38000, 26, 'kochi'),
(5, 'meera', 'hr', 45000, 29, 'bangalore'),
(6, 'suresh', 'finance', 30000, 41, 'mumbai'),
(7, 'anjali', 'it', 70000, 34, 'trivandrum'),
(8, 'vimal', 'sales', 28000, 24, 'kochi'),
(9, 'kiran', 'hr', 52000, 38, 'delhi'),
(10, 'priya', 'finance', 48000, 31, 'bangalore');

-- q1
select distinct department from empl;


-- q2
select *from empl order by salary desc;

-- q3
select * from empl order by salary desc limit 5;

-- q4
select * from empl limit 5 offset 3;

-- q5
select * from empl where department='it' and salary>40000;

-- q6
select * from empl where city in ('kochi','trivandrum');


-- q7
select * from empl where department in ('hr','finance');

-- q8
select * from empl where city not in ('chennai','bangalore');


-- q9
select * from empl where salary between 30000 and 60000;

-- q10
select max(salary) from empl;

-- q11
select min(age) from empl;

-- q12
select avg(salary) from empl;

-- q13
select count(*) from empl;

-- q14
select sum(salary) from empl;

-- q15
select * from empl where salary>(select avg(salary) from empl);

-- q16
select * from empl where salary=(select max(salary) from empl);

-- q17
-- q18

-- q19
select * from empl where age>(select avg(age) from empl);

-- q20
alter table empl add email varchar(100);
desc empl;























