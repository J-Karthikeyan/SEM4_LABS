# LAB3 : INTERMEDIATE SQL
 
Q1 UNION (Use union all to retain duplicates): Find courses that ran in Fall 2009 or in Spring 2010
 
```sql
select course_id from section where semester = 'Fall' and year = 2009 
UNION
select course_id from section where semester = 'Spring' and year = 2010;
```
 
Q2 INTERSECT (Use intersect all to retain duplicates): Find courses that ran in Fall 2009 and in spring 2010
 
```sql
select course_id from section where semester = 'Fall' and year = 2009 
INTERSECT 
select course_id from section where semester = 'Spring' and year = 2010;
```
 
Q3 MINUS: Find courses that ran in Fall 2009 but not in Spring 2010
 
```sql
select course_id from section where semester = 'Fall' and year = 2009 
MINUS 
select course_id from section where semester = 'Spring' and year = 2010;
```
 
Q4 Null values : Find the name of the course for which none of the students registered.
```sql
select title from course where course_id not in (select course_id from takes);
```
 
### Nested Subqueries
#### Set Membership (in / not in):
Q5 Find courses offered in Fall 2009 and in Spring 2010.
 
```sql
select course_id, title from course 
where course_id in (select course_id from section where semester = 'Fall' and year = 2009) 
and course_id in (select course_id from section where semester = 'Spring' and year = 2010);
```
 
Q6 Find the total number of students who have taken course taught by the instructor with ID 10101.
```sql
select ID from takes where course_id in (select course_id from teaches where ID = 10101);
```
 
Q7 Find courses offered in Fall 2009 but not in Spring 2010.
```sql
select course_id, title from course 
where course_id in (select course_id from section where semester = 'Fall' and year = 2009) 
and course_id not in (select course_id from section where semester = 'Spring' and year = 2010);
```
