create table StudentGrade(
    rollno number primary key,
    GPA number(2,1)
);

INSERT INTO StudentGrade VALUES (1, 5.8);
INSERT INTO StudentGrade VALUES (2, 6.5);
INSERT INTO StudentGrade VALUES (3, 3.4);
INSERT INTO StudentGrade VALUES (4, 7.8);
INSERT INTO StudentGrade VALUES (5, 9.5);

declare 
    rno student.rollno%type;
    gpa_val student.GPA%type;
begin
    rno := '&rollno';
    select gpa into gpa_val from student where rollno = rno;
    dbms_output.put_line('GPA of rno ' || rno || ' is ' || gpa_val);
end;
/

-- Q2) Write a PL/SQL block to display the letter grade(0-4: F; 4-5: E; 5-6: D; 6-7: C; 7-8: B; 8-9: A; 9-10: A+} of given student

declare 
    rno StudentGrade.rollno%type;
    gpa_val StudentGrade.GPA%type;
    grade varchar2(2);
begin
    rno := '&rollno';
    select gpa into gpa_val from StudentGrade where rollno = rno;
    if gpa_val > 9 then
        grade := 'A+';
    elsif gpa_val > 8 then
        grade := 'A';
    elsif gpa_val > 7 then
        grade := 'B';
    elsif gpa_val > 6 then
        grade := 'C';
    elsif gpa_val > 5 then
        grade := 'D';
    elsif gpa_val > 4 then
        grade := 'E';
    else
        grade := 'F';
    end if;
    dbms_output.put_line('Grade of rno ' || rno || ' is ' || grade);
end;
/

/*
Q3) Input the date of issue and date of return for a book. Calculate and display the fine with the appropriate message using a PL/SQL block. The fine is charged as per the table 8.1:

late period     Fine
7 days          NIL
8-15 days       Rs. 1 per day
16-30 days      Rs. 2 per day
After 30 days   Rs. 5 per day
*/

declare 
    issue_date date;
    return_date date;
    fine number;
begin
    dbms_output.put_line('Enter issue date in format dd-mm-yyyy');
    issue_date := to_date('&issue_date', 'dd-mm-yyyy');
    dbms_output.put_line('Enter return date in format dd-mm-yyyy');
    return_date := to_date('&return_date', 'dd-mm-yyyy');
    if return_date - issue_date <= 7 then  
        fine := 0;
    elsif return_date - issue_date <= 15 then
        fine := (return_date - issue_date - 7) * 1;
    elsif return_date - issue_date <= 30 then
        fine := (return_date - issue_date -15) * 2 + 8;
    else
        fine := (return_date - issue_date - 30) * 5 + 8 + 30;
    end if;
    dbms_output.put_line('Fine is ' || fine);
end;
/

-- Q4) Write a PL/SQL block to print the letter grade of all the students(RollNo: 1 - 5)

declare
    rno StudentGrade.rollno%type := 1;
    gpa_val StudentGrade.GPA%type;
    grade varchar2(2);
begin
    loop 
        select gpa into gpa_val from StudentGrade where rollno = rno;
        if gpa_val > 9 then
            grade := 'A+';
        elsif gpa_val > 8 then
            grade := 'A';
        elsif gpa_val > 7 then
            grade := 'B';
        elsif gpa_val > 6 then
            grade := 'C';
        elsif gpa_val > 5 then
            grade := 'D';
        elsif gpa_val > 4 then
            grade := 'E';
        else
            grade := 'F';
        end if;
        dbms_output.put_line('Grade of rno ' || rno || ' is ' || grade);
        rno := rno + 1;
        exit when rno > 5;
    end loop;
end;
/

-- Q5) Alter StudentTable by appending an additional column LetterGrade Varchar2(2).Then write a PL/SQL block to update the table with letter grade of each student.

alter table StudentGrade add LetterGrade varchar2(2);

declare
    rno StudentGrade.rollno%type := 1;
    gpa_val StudentGrade.GPA%type;
    grade varchar2(2);
begin
    while rno <= 5 loop
        select gpa into gpa_val from StudentGrade where rollno = rno;
        if gpa_val > 9 then
            grade := 'A+';
        elsif gpa_val > 8 then
            grade := 'A';
        elsif gpa_val > 7 then
            grade := 'B';
        elsif gpa_val > 6 then
            grade := 'C';
        elsif gpa_val > 5 then
            grade := 'D';
        elsif gpa_val > 4 then
            grade := 'E';
        else
            grade := 'F';
        end if;
        update StudentGrade set LetterGrade = grade where rollno = rno;
        rno := rno + 1;
    end loop;
end;
/

-- Q6) Write a PL/SQL block to find the student with max. GPA without using aggregate function.

declare
    gpa_val StudentGrade.GPA%type;
    max_gpa StudentGrade.GPA%type := 0;
    max_rollno StudentGrade.rollno%type;
begin 
    for i in 1..5 loop
        select gpa into gpa_val from StudentGrade where rollno = i;
        if gpa_val > max_gpa then
            max_gpa := gpa_val;
            max_rollno := i;
        end if;
    end loop;
    dbms_output.put_line('Max GPA is ' || max_gpa || ' Roll no is ' || max_rollno);
end;
/

--Q7 Implement lab exercise 4 using GOTO.

declare
    gpa_val StudentGrade.GPA%type;
    grade varchar2(2);
begin 
    for i in 1..5 loop
        select gpa into gpa_val from StudentGrade where rollno = i;
        if gpa_val > 9 then
            grade := 'A+';
            GOTO print_now;
        elsif gpa_val > 8 then 
            grade := 'A';
            GOTO print_now;
        elsif gpa_val > 7 then
            grade := 'B';
            GOTO print_now;
        elsif gpa_val > 6 then
            grade := 'C';
            GOTO print_now;
        elsif gpa_val > 5 then
            grade := 'D';
            GOTO print_now;
        elsif gpa_val > 4 then
            grade := 'E';
            GOTO print_now;
        else
            grade := 'F';
            GOTO print_now;
        end if;
        <<print_now>>
        dbms_output.put_line('Grade of Roll No ' || i || ' is ' || grade);
    end loop;
end;
/

/*
Q8) Based on the University database schema, write a PL/SQL block to display the details of the Instructor whose name is supplied by the user. Use exceptions to show appropriate error message for the following cases: 

a. Multiple instructors with the same name

b. No instructor for the given name
*/

declare 
    inst_name Instructor.Name%type;
    id Instructor.ID%type;
    dept Instructor.Dept_name%type;
begin
