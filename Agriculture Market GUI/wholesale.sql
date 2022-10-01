-- Active: 1657354454494@@127.0.0.1@3306@agn
show databases;
use agn;
use agriculture;
create table crop(
	crop_name varchar(100) PRIMARY KEY,
    crop_type varchar(100) not null,
    crop_desc varchar(100) not null,
    exp_date date not null
);
create table supplier(
	sup_name varchar(100) not null,
    s_id int primary key,
    commission varchar(25) not null,
    phone varchar(100) not null,
    email varchar(100) not null
);

create table farmer(
	farmer_name varchar(100) not null,
    f_id int primary key,
    age int not null,
    phone varchar(100) not null
);

create table warehouse(
	w_id int primary key,
    address varchar(100) not null,
    max_capacity varchar(100) not null,
    present_storage varchar(100) not null
);

create table payment(
	p_id int primary key,
    amount varchar(100) not null,
    discount varchar(100) not null,
    tax varchar(100) not null,
    mode_of_payment varchar(100) not null,
    cust_id int not null,
    FOREIGN KEY(cust_id) REFERENCES customer(c_id)
);

create table orders(
	o_id int primary key,
    order_date date not null,
    due_date date not null,
    delivery_loc varchar(100),
    cust_id int not null,
    FOREIGN KEY(cust_id) REFERENCES CUSTOMER(c_id)
);

create table customer(
	name varchar(100) not null,
    c_id int PRIMARY KEY,
    age int not null,
    address varchar(100) not null,
    phone varchar(100) not null,
    email varchar(100) not null
);

create table stocks_in(
	s_id int not null,
    w_id int not null,
    PRIMARY KEY(s_id, w_id),
    FOREIGN KEY(s_id) REFERENCES supplier(s_id),
    FOREIGN KEY(w_id) REFERENCES warehouse(w_id)
);

create table supplies_to(
	s_id int not null,
    f_id int not null,
    PRIMARY KEY(s_id, f_id),
    FOREIGN KEY(s_id) REFERENCES supplier(s_id),
    FOREIGN KEY(f_id) REFERENCES farmer(f_id)
);


create table gets(
	crop_name varchar(100) not null,
    o_id int not null,
    quantity int not null,
    PRIMARY KEY(crop_name, o_id),
    FOREIGN KEY(crop_name) REFERENCES crop(crop_name),
    FOREIGN KEY(o_id) REFERENCES orders(o_id)
);

create table supply(
	f_id int not null,
    crop_name varchar(100) not null,
    PRIMARY KEY(f_id, crop_name),
    FOREIGN KEY(f_id) REFERENCES farmer(f_id),
    FOREIGN KEY(crop_name) REFERENCES crop(crop_name)
);

select * from supply;
