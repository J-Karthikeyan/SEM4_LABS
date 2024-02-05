# LAB4
 
Q1 Find the number of students in each course.
```sql
select course.course_id, count(takes.course_id)
from course
join takes on course.course_id = takes.course_id
group by course.course_id;
```
 
Q2 Find those departments where the average number of students are greater than 10. Find the total number of courses in each department.
```sql
select dept_name, count(ID) from student group by dept_name having count(ID) > 10;
```
 
Q3 Find the total number of courses in each department.
```sql
select department.dept_name, count(course.dept_name) 
from department join course 
on course.dept_name = department.dept_name 
group by department.dept_name;
```
 
Q4 Find the names and average salaries of all departments whose average salary is greater than 42000.
```sql
select department.dept_name , avg(instructor.salary) 
from department join instructor on instructor.dept_name = department.dept_name 
group by department.dept_name 
having avg(instructor.salary) > 42000;
```
 
Q5 Find the enrolment of each section that was offered in Spring 2009.
```sql
select sec_id, course_id, count(ID) 
from takes where year = 2009 and semester = 'Spring' 
group by sec_id,course_id;
```
 
Q6 List all the courses with prerequisite courses, then display course id in increasing order.
```sql
select course_id, title from course 
where course_id in (select course_id from prereq) order by(course_id);
```
 
Q7 Display the details of instructors sorting the salary in decreasing order.
```sql
select * from instructor order by (salary) desc;
```
 
Q8 Find the maximum total salary across the departments.
