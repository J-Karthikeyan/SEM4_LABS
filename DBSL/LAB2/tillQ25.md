SELECT * from student;

SELECT * from instructor where dept_name = 'Comp. Sci.';

SELECT title from course where dept_name = 'Comp. Sci.' and credits = 3;

SELECT course.course_id , course.title from student, takes, course WHERE course.course_id = takes.course_id and student.ID = 12345 and takes.ID = student.ID;

SELECT * from instructor where salary > 40000 and salary < 90000;

SELECT ID from instructor where ID not in (SELECT ID from teaches);
