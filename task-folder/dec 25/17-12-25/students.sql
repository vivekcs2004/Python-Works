create database college;
use college;
create table students(
	student_id int  primary key,
    name varchar(100),
    age int,
    email varchar(100)
    );
    
    desc students;
    
create table employees(
	emp_id int auto_increment primary key,
    salary int not null,
    email varchar(200) unique
    );
    
    desc employees;


create table courses(
	course_id int auto_increment primary key,
    course_name  varchar(100) not null,
    duration varchar(200) default "3 months"
    );
    
    desc courses;
    
create table marks(
	student_id int auto_increment primary key,
    subject varchar(100) not null,
    marks int not null
    );
    
    desc marks;
    
    
create table attendance(
	attendance_id int auto_increment primary key,
    status enum("present","absent")
    );
    
    desc attendance;
    
    
