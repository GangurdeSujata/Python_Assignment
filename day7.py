
pip install mysql-connector

import mysql.connector as sqlcon

db = sqlcon.connect(host = "localhost", user = "APMC", passwd = "system", database = 'essentials')

cur = db.cursor()

cur.execute("update teacher set subject='TCS' where tname = 'dc'")
cur.execute("select * from teacher")

for i in cur:
	print(i)

cur.close()
db.commit()

# SQL Statements

'''

create database essentials;
drop database essentials;

show databases;
use essentials;
show tables;
create table teacher(tid int, tname varchar(30), subject varchar(50));
desc teacher;

insert into teacher values(1120, 'Swapnil', 'python');
insert into teacher values(1121, 'Pratibha', 'java');
insert into teacher values(1122, 'dc', 'operating system');
insert into teacher values(1123, 'yogesh', 'php');


select * from teacher;

update teacher set subject'TCS' where tname = 'dc';

set SQL_SAFE_UPDATES = 1;

drop table teacher;

'''
pdbc.py
Displaying pdbc.py.
