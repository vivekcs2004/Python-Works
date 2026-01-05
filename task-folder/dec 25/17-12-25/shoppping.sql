create database shopping;
use shopping;

create table orders(
	order_id int auto_increment primary key,
    order_date datetime default current_timestamp,
    customer_name varchar(100) 
    );
    
    desc orders;
    
create table users(
	user_id int auto_increment primary key,
    username varchar(100) unique,
    password varchar(100) not null
    );
    
    desc orders;
    
create table products(
	product_id int primary key auto_increment,
    price int not null,
    stock varchar(100) default ("0")
    );
    
    desc products;
    
    
create table payments(
	amount decimal(10,2) ,
    payment_mode enum("cash","card","upi"),
    payment_date date
    );
    
    desc payments;
    