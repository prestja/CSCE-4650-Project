create database if not exists lego;
use lego;

/* Uncomment the section below to regenerate the tables if major changes to the schema are made */

drop table if exists orderitemset;
drop table if exists setparts;
drop table if exists sets;
drop table if exists parts;
drop table if exists customers;
drop table if exists employees;
drop table if exists orders;


CREATE TABLE IF NOT EXISTS parts (
    partID INT NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (partID)
);

CREATE TABLE IF NOT EXISTS sets (
    setID INT NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (setID)
);

CREATE TABLE IF NOT EXISTS setparts (
    partID INT,
    setID INT,
    FOREIGN KEY (partID)
        REFERENCES parts (partID),
    FOREIGN KEY (setID)
        REFERENCES sets (setID)
);

CREATE TABLE IF NOT EXISTS customers (
    name VARCHAR(255),
    address VARCHAR(255),
    storeprefs ENUM('physical', 'online'),
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS employees (
    employeeID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    storeprefs ENUM('store', 'online')
);

/* Insert sample employees */
insert into employees (name, storeprefs)
values('jacob', 'store'), ('kamal', 'online'), ('sagar', 'store');

CREATE TABLE IF NOT EXISTS orders (
    orderNum INT UNIQUE,
    type ENUM('card', 'cash'),
    cardType ENUM('amex', 'mc', 'vista', 'other'),
    pin INT,
    billingAddress VARCHAR(255),
    amount FLOAT
);

CREATE TABLE IF NOT EXISTS orderitemset (
    orderNum INT NOT NULL,
    partID INT,
    setID INT,
    FOREIGN KEY (partID)
        REFERENCES parts (partID),
    FOREIGN KEY (setID)
        REFERENCES sets (setID)
);
