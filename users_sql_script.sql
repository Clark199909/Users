drop database if exists users;
create database users;
use users;

drop table if exists system_user;

create table system_user
(
    `username` varchar(50) not null,
    `email` varchar(20) not null,
    `phone` varchar(20) not null,
    `password` varchar(50) not null,
    primary key (`username`)
);

