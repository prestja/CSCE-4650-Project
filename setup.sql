create database if not exists lego;
use lego;

/* Drop tables as we are making massive changes to the scheme */
drop table if exists setparts;
drop table if exists sets;
drop table if exists parts;
drop table if exists customers;
drop table if exists payment;

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

create table if not exists customers (
	name varchar(255),
    address varchar (255),
    storeprefs enum('physical', 'online'),
    username varchar(255),
    password varchar(255)
);

create table if not exists orders (
	orderNum int,
    type enum ('card', 'cash'),
    cardType enum('amex', 'mc', 'vista', 'other'),
    pin int,
    billingAddress varchar(255),
    amount float
);