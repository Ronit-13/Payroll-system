import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='12345')
mycursor=conn.cursor()
conn.commit
mycursor.execute("create database test")
mycursor.execute("use test")
mycursor.execute("create table log_id(user_id varchar(20) ,password  varchar(100) primary key)")
mycursor.execute("create table office (em_no bigint,em_name varchar(255),em_dept varchar(255),em_salary int,em_age int)")
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')

