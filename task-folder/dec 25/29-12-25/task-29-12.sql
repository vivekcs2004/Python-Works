create database social_media_db;
use social_media_db;

create table users(
user_id int primary key auto_increment,
username varchar(200) not null unique,
email varchar(200) unique,
password varchar(200) not null,
bio text,
is_active boolean default true,
created_at datetime default current_timestamp   
);
desc users;

create table posts(
post_id int primary key auto_increment,
user_id int not null,
created_at datetime default current_timestamp,
foreign key (user_id) references users(user_id)
); 
desc posts;

create table comments(
comment_id int primary key auto_increment,
post_id int not null,
user_id int not null,
comment_text text not null,
created_at datetime default current_timestamp,
foreign key (post_id) references posts(post_id),
foreign key (user_id) references users(user_id)
); 
desc comments;

create table likes(
like_id int primary key auto_increment,
comment_id int,
post_id int not null,
user_id int not null,
reaction_type enum("like","love","haha","angry") default "like",
created_at datetime default current_timestamp,
foreign key (post_id) references posts(post_id),
foreign key (user_id) references users(user_id),
foreign key (comment_id) references comments(comment_id)
);
desc likes;



INSERT INTO users (username, email, password, bio) VALUES
('ashik', 'ashik@gmail.com', 'pass123', 'Tech enthusiast'),
('vivek', 'vivek@gmail.com', 'pass456', 'Love coding'),
('abhijith', 'abhijith@gmail.com', 'pass789', 'Photography fan'),
('arun', 'arun@gmail.com', 'pass321', 'Traveller'),
('adhil', 'adhil@gmail.com', 'pass654', 'Food lover');
select * from users;

INSERT INTO posts (user_id) VALUES
(1),
(2),
(3),
(1),
(4);
select * from posts;

INSERT INTO comments (post_id, user_id, comment_text) VALUES
(1, 2, 'Nice post!'),
(1, 3, 'Really helpful'),
(2, 1, 'Good one'),
(3, 4, 'Amazing'),
(4, 5, 'Loved this post');
select * from comments;

INSERT INTO likes (post_id, user_id, reaction_type) VALUES
(1, 2, 'like'),
(1, 3, 'love'),
(2, 1, 'haha'),
(3, 4, 'like'),
(4, 5, 'angry');
INSERT INTO likes (post_id, comment_id, user_id, reaction_type) VALUES
(1, 1, 3, 'like'),
(2, 3, 4, 'love'),
(3, 4, 1, 'haha');
select * from likes;