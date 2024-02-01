### Q1
```sql
create table employee(
    EmpNo numeric(4) primary key,
    EmpName varchar(15) not null,
    gender char(1) not null check (gender in ('M','F')),
    salary numeric(9,2) not null,
    address varchar(15) not null
);
```

### Q2
```sql
create table department(
    deptno numeric(3) primary key,
    deptname varchar(10) not null unique
);
```