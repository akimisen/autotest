use test;
drop table if exists user;
drop table if exists department;
drop table if exists project;
drop table if exists case_info;
drop table if exists rest_case;
drop table if exists ui_case;

CREATE TABLE user( user_id int not null primary key auto_increment, user_name varchar(20) not null,pwd_hash char(128) not null,group_id int not null);
CREATE TABLE department( department_id int not null primary key, department_name varchar(20) unique not null);
CREATE TABLE case_info( case_id int not null primary key auto_increment, user_id int, group_id int, project_id int,case_model varchar(10),case_description varchar(100));
CREATE TABLE rest_case( case_id int not null primary key auto_increment, url varchar(100) not null, method enum('GET','POST','PUT','DELETE') default 'GET' not null, params json, token char(128) default null,token_expire datetime default null,data json,headers json);
CREATE TABLE project(project_id int primary key auto_increment, project_name varchar(100) not null);
CREATE TABLE task(task_id int primary key auto_increment, task_name varchar(100) not null, user_id int, case_id int,auth Boolean default True, task_time Datetime default null);


insert into department (department_id, department_name) values(1,'group1');
insert into department (department_id, department_name) values(2,'group2');
insert into department (department_id, department_name) values(3,'group3');

insert into project(project_id,project_name) values (1,'project1');
insert into project(project_id,project_name) values (1,'project2');
insert into project(project_id,project_name) values (1,'project3');

-- ssh -p 27209 tracy@104.128.92.28 
-- mysql root/tracy>>>Test@123/Test_123