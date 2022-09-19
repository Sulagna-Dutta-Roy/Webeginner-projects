-- Active: 1657354454494@@127.0.0.1@3306@movie

show databases;

create DATABASE movie;

use movie;

create table movie(
	mov_id int primary key,
    start_time varchar(100) not null,
    ticket_available int not null,
    mov_name varchar(100) not null	
);

create table customer(
	cust_id int primary key,
    cust_name varchar(100) not null,
    cust_age int not null,
    mov_id int not null,
	foreign key(mov_id) references movie(mov_id)
);

select * from movie;

Insert into movie
values(4,'04:00',180,'TOP GUN');