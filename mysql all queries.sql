-- mysql -u userName -p.
-- create database employee;
-- use employee;
 
create table emp (emp_id int primary key,name varchar(20),desg varchar(20));
-- desc emp;
insert into emp values(0011,'abhishek','intern');
insert into emp values(0012,'ashutosh','manager');
insert into emp values(0013,'ashwin','HR');
insert into emp values(0014,'vijay','devloper');
insert into emp values(0015,'deepak','intern');
-- create index e_id on emp(emp_id);
-- alter table emp drop index e_id;
-- alter table emp drop column desg; 
alter table emp add column city varchar(20);
-- alter table emp modify column city int;

create view view1 as select emp_id from emp;
create or replace view view1 as select emp_id,name from emp; 
drop view view1;

-- select * from emp order by emp_id desc; -- bydefault its ascending order
update emp set city = 'pune' where name='abhishek';

delete from emp where name ='vijay';
-- select * from emp;

-- select min (emp_id) from emp;
-- select max (emp_id) from emp;
-- select avg (emp_id) from emp;
-- select count (emp_id) from emp;
-- select sum (emp_id) from emp;

create table emp_s (id int primary key,state varchar(20),passcode varchar(20));

insert into emp_s values (0011,'MH','dem009');
insert into emp_s values (0013,'MP','eem109');
insert into emp_s values (0015,'UP','fem209');
insert into emp_s values (0014,'TN','del029');
insert into emp_s values (0019,'MH','djm025');

select * from emp_s;
-- select emp.emp_id , emp.name,emp_s.state from emp inner join emp_s on emp.emp_id=emp_s.id ;

-- select emp.emp_id , emp.name,emp_s.state from emp left join emp_s on emp.emp_id=emp_s.id ;

-- select emp.emp_id , emp.name,emp_s.state from emp right join emp_s on emp.emp_id=emp_s.id ;

-- select emp.emp_id , emp.name,emp_s.state from emp cross join emp_s where emp.emp_id=emp_s.id ;

-- select * from emp union all select * from emp_s;
-- create table tp(number int);
-- insert into tp select * from emp;



