create database task_18_12;
use task_18_12;

create table students (
    student_id int primary key,
    name varchar(50),
    age int,
    course varchar(50),
    email varchar(100)
);

insert into students (student_id, name, age, course, email) values
(1, 'amit', 20, 'computer science', 'amit@gmail.com'),
(2, 'neha', 21, 'electronics', 'neha@gmail.com'),
(3, 'rahul', 19, 'mechanical', 'rahul@gmail.com');

select * from students;
---q2--
create table users (
    user_id int primary key,
    name varchar(50),
    email varchar(100),
    password varchar(100),
    created_at date
);

insert into users (user_id, name, email, password, created_at) values
(1, 'amit', 'amit@gmail.com', 'amit@123', '2025-01-01'),
(2, 'neha', 'neha@gmail.com', 'neha@123', '2025-01-05'),
(3, 'rahul', 'rahul@gmail.com', 'rahul@123', '2025-01-10');

select name, email
from users;

---q3---

create table employees (
    emp_id int primary key,
    name varchar(50),
    department varchar(50),
    salary int,
    city varchar(50)
);


insert into employees (emp_id, name, department, salary, city) values
(1, 'amit', 'hr', 30000, 'kochi'),
(2, 'neha', 'it', 40000, 'trivandrum'),
(3, 'rahul', 'hr', 35000, 'calicut');

select *
from employees
where department = 'hr';


---q4---

create table employees1 (
    emp_id int primary key,
    name varchar(50),
    department varchar(50),
    salary int,
    city varchar(50)
);

insert into employees1 (emp_id, name, department, salary, city) values
(1, 'amit',  'hr',      30000, 'kochi'),
(2, 'neha',  'it',      45000, 'trivandrum'),
(3, 'rahul', 'finance', 35000, 'calicut'),
(4, 'arjun', 'hr',      28000, 'kollam');

select *
from employees1
where salary > 30000;

---q5---

create table products (
    product_id int primary key,
    product_name varchar(50),
    price int,
    category varchar(50),
    stock int
);


insert into products (product_id, product_name, price, category, stock) values
(1, 'pen', 20, 'stationery', 100),
(2, 'notebook', 80, 'stationery', 50),
(3, 'headphones', 1500, 'electronics', 20),
(4, 'mouse', 700, 'electronics', 30),
(5, 'bottle', 900, 'home', 40);

select *
from products
where price < 1000;


---q6---

create table students1 (
    student_id int primary key,
    name varchar(50),
    age int,
    course varchar(50),
    email varchar(100)
);


insert into students1 (student_id, name, age, course, email) values
(1, 'amit', 20, 'computer science', 'amit@gmail.com'),
(2, 'neha', 21, 'electronics', 'neha@gmail.com'),
(3, 'rahul', 20, 'mechanical', 'rahul@gmail.com'),
(4, 'meera', 19, 'civil', 'meera@gmail.com');


select *
from students
where age = 20;


---q7---

create table customers (
    customer_id int primary key,
    name varchar(50),
    email varchar(100),
    phone varchar(15),
    city varchar(50)
);

insert into customers (customer_id, name, email, phone, city) values
(1, 'rahul', 'rahul@gmail.com', '9876543210', 'kochi'),
(2, 'amit', 'amit@gmail.com', '9876543211', 'delhi'),
(3, 'neha', 'neha@gmail.com', '9876543212', 'mumbai'),
(4, 'arjun', 'arjun@gmail.com', '9876543213', 'chennai');


select *
from customers
order by name asc;

---q8--


create table orders (
    order_id int primary key,
    customer_id int,
    order_date date,
    total_amount int
);


insert into orders (order_id, customer_id, order_date, total_amount) values
(1, 1, '2025-01-01', 2500),
(2, 2, '2025-01-02', 1800),
(3, 3, '2025-01-03', 3200),
(4, 1, '2025-01-04', 1500),
(5, 2, '2025-01-05', 4000),
(6, 3, '2025-01-06', 2100);

select *
from orders
where order_id<=5;

---q9---

create table employees2 (
    emp_id int primary key,
    name varchar(50),
    department varchar(50),
    salary int,
    city varchar(50)
);

insert into employees2 (emp_id, name, department, salary, city) values
(1, 'amit', 'hr', 30000, 'delhi'),
(2, 'neha', 'it', 45000, 'kochi'),
(3, 'rahul', 'finance', 35000, 'mumbai'),
(4, 'arjun', 'hr', 28000, 'chennai');


select *
from employees2
where city != 'delhi';

---q10---

select distinct department
from employees2;







