# PL/SQL basics

## Terminal output
```sql
set serveroutput on;
```
## Display
```sql
declare 
    message varchar2(20) := 'Hello World';
begin
    dbms_output.put_line(message);
end;
/
```
## IF-ELSE 
```sql
declare 
    grade char(1);
begin 
    grade := '&g';
if grade = 'A' then
    dbms_output.put_line('> 90 marks');
elsif grade = 'B' then 
    dbms_output.put_line('> 80 marks');
else
    dbms_output.put_line('Fail');
end if;
end;
/
```
## SIMPLE LOOP
```sql
declare
    x number := 0;
begin 
    loop
        dbms_output.put_line('Inside loop: x = ' || to_char(x));
        x := x+1;
        if x > 3 then exit;
        end if;
    end loop;
dbms_output.put_line('After loop: x = ' || to_char(x));
end;
/
```
## WHILE LOOP
```sql
DECLARE
    x NUMBER := 0;
BEGIN
    WHILE x < 4
        LOOP
            DBMS_OUTPUT.PUT_LINE ('Inside loop: x = ' || TO_CHAR(x));
            X := x + 1;
        END LOOP;
END;
/
```
## FOR LOOP
```sql
DECLARE 
    x number;
BEGIN
    DBMS_OUTPUT.PUT_LINE ('Enter the number: ');
    x := &x;
    FOR i IN 1..x LOOP
        DBMS_OUTPUT.PUT_LINE (i);
    END LOOP;
END;
/
```
##
