# SQL

---
## SQL commands 
1. DDL
2. DML
3. DCL
4. TCL

## Basic Data Types 
1. CHARACTER [(length)] or CHAR [(length)],
2. VARCHAR (length)
3. BOOLEAN
4. SMALLINT
5. INTEGER or INT
6. DECIMAL [(p[,s])] or DEC [(p[,s])]
7. NUMERIC [(p[,s])]
8. REAL
9. FLOAT(p)
10. DOUBLE PRECISION
12. DATE
13. TIME
14. TIMESTAMP
15. CLOB [(length)] or CHARACTER LARGE OBJECT [(length)] or CHAR LARGE OBJECT [(length)]
16. BLOB [(length)] or BINARY LARGE OBJECT [(length)]

## Creating a table 
```sql
create table student(
    reg_no numeric(5),
    stu_name varchar(15),
    stu_age numeric(5),
    stu_dob date,
    subject1_marks numeric(4,2), 
    ...
    ...  
);
```

### Q1
```sql
create table employee(
    emp_no numeric(4),
    emp_name varchar(15),
    emp_address varchar(15)
);
```

### Q2
```sql
insert into employee values (1111, 'name1', 'manipal');
insert into employee values (1112, 'name2', 'manglore');
insert into employee values (1113, 'name3', 'banglore');
insert into employee values (1114, 'name4', 'manglore');
insert into employee values (1115, 'name5', 'manipal');
```
### Q3
```sql
select emp_name from employee;
```
### Q4
```sql
select name from employee where name = 'manipal';
```
### Q5
```sql
alter table employee add (salary numeric(7,2));
```
### Q6
```sql
update table employee set salary = 123456.12 where emp_no = 1111;
update table employee set salary = 223456.12 where emp_no = 1112;
update table employee set salary = 323456.12 where emp_no = 1113;
update table employee set salary = 423456.12 where emp_no = 1114;
update table employee set salary = 523456.12 where emp_no = 1115;

```

### Q7
```sql
desc employee;
```

### Q8
```sql
delete from employee where emp_address = 'manglore';
```

### Q9
```sql
rename table employee to employee;
```
### Q10
```sql
drop table employee1;
```