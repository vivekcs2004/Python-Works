create database task0201;
use task0201;

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    price INT NOT NULL,
    category VARCHAR(100) NOT NULL,
    status BOOLEAN DEFAULT TRUE
);


