create database if not exists lego;
use lego;

/* Uncomment the section below to regenerate the tables if major changes to the schema are made */

drop table if exists orderitemset;
drop table if exists setparts;
drop table if exists sets;
drop table if exists parts;
drop table if exists orders;
drop table if exists customers;
drop table if exists employees;

CREATE TABLE IF NOT EXISTS parts (
    partID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price float,
    quantity int
);

insert into parts (name, price, quantity)
values('1x1 brick', 0.15, 256), ('2x2 brick', 0.17, 256);
/* select * from parts; */

CREATE TABLE IF NOT EXISTS sets (
    setID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

/* Create some sample sets */
insert into sets(name)
values ('TIE-Fighter'), ('X-Wing');

CREATE TABLE IF NOT EXISTS setparts (
    partID INT,
    setID INT,
    quantity int,
    FOREIGN KEY (partID)
        REFERENCES parts (partID),
    FOREIGN KEY (setID)
        REFERENCES sets (setID)
);

/* Create some sample set-part lists */
INSERT INTO setparts (partID, setID, quantity)
	VALUES (1, 1, 14), (2, 1, 6), (2, 2, 4);
    
CREATE TABLE IF NOT EXISTS customers (
    name VARCHAR(255),
    address VARCHAR(255),
    storeprefs ENUM('physical', 'online'),
    username VARCHAR(255) UNIQUE PRIMARY KEY,
    password VARCHAR(255)
);

insert into customers(name, address, storeprefs, username, password)
	values('John Doe', '123 Apple Lane', 'physical', 'jd123', '123'), ('Jane Doe Carpenter', '456 Cherry Avenue', 'physical', 'jc456', '456');

/* select * from customers where username='jd123'; */
    
CREATE TABLE IF NOT EXISTS employees (
    employeeID INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(255),
    name VARCHAR(255),
    storeprefs ENUM('store', 'online')
);

/* Insert sample employees */
insert into employees (name, storeprefs, password)
values('jacob', 'store', '44931'), ('kamal', 'online', '65535'), ('sagar', 'store', '12345');

CREATE TABLE IF NOT EXISTS orders (
    orderNum INT AUTO_INCREMENT KEY,
    username VARCHAR(255),
    type ENUM('card', 'cash'),
    cardType ENUM('amex', 'mc', 'vista', 'other'),
    cardNumber int,
    pin INT,
    billingAddress VARCHAR(255),
    placed DATETIME,
    delivered DATETIME,
    amount FLOAT,
    status ENUM('open', 'transit', 'delivered', 'refunded'),
    FOREIGN KEY (username)
        REFERENCES customers (username)
);

insert into orders (username, type, status, placed)
values ('jd123', 'card', 'transit', '2020-7-14 14:29:36'), ('jd123', 'card', 'refunded', '2020-7-22 12:00:00'), ('jc456', 'card', 'transit', '2020-7-25 2:13:00');

/* select * from orders where username = 'jd123'; */

CREATE TABLE IF NOT EXISTS orderitemset (
    orderNum INT not null,
    partID INT,
    setID INT,
    FOREIGN KEY (partID)
        REFERENCES parts (partID),
    FOREIGN KEY (setID)
        REFERENCES sets (setID)
);

insert into orderitemset(orderNum, partID) values(1, 1); /* First part */
insert into orderitemset(orderNum, setID) values(1, 1); /* First set */
