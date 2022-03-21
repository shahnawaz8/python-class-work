Operator
+ * - /
(//)
**(Power)
%(modular)
relational
+= (1+=1)=1
-=
**=
/=
%=
>
<
>=
<=
!=
== conditional equlity
Logical oprator
and
or
not
Membership
in
not in (name="parul")
ex 'u' in name o/p true
 'U' in name o/p  false
Identity operator
is
is not 
ex name='parul'
name1='Parul'
name is name1 o/p False
16/07/2019
Rang
1. start stop step
for loop:-
    for obj in rang():
            logic 
    else #optional
            logic
Ex:-
    1. for x in range(1,10):
            print(x)
            
    2.        for x in range(1,10):
            print(x,end=' ')
            
    3. for x in range(1,10):
            print(x,end='')
        else:
                print() for line terminate
    4. for x in range(2,21,2for gap):
                print(x)
            o/p= 2 4 6 8 10 12 14 16 18 20 >>>
            
Nested loop
    1. for x in range(1,7):
         for y in range(1,x+1):
                    print(y,end='')
                print()
    
    2. for x in range(5,0,-1):           5 4 3 2 1
         for y in range(x,0,-1):         4 3 2 1
                    print(y,end='')      3 2 1
                print()                  2 1
                                         1
    3. for x in range(1,7):
         for y in range(1,x+1):
                    print(*,end='')
                print()
    4. i=1
       j=1
        for x in range(5)
            print(i)
            j=j*10+1
            i=j*j
    5. i=1
       j=1
       s=6
        for x in range(5)
            for y in range(s):
                        print(end=' ')
            print(i)
            j=j*10+1
            i=j*j
            s-=j
    Que:-      1
              121
             12321
            1234321
           123454321
            1234321
             12321
              121
               1
            
    while loop:-- syntax
         while condition:
                logic
            else
                logic
            Ex:--
                i=1
                while i<=10:
                        print(i)
                        i+=1
            
                2.    i=1
                       while i<=10:
                        j=1
                        while j<=10:
                                print(i*j,end=' ')
                                  j+=1
                                print()
                                i+=1
                3. i=12345
                      while i>=1
                     k=i//10
                        x=i%10
                        j=j*10+x
                        i=k
                            print(j)
            Que:-- 0 1 1 2 3 5 8
   
        
    i=0
    j=1
    k=0
        for x in range(7)
            print(k)
            k=i+j
            j=i
            i=s
            
31/07/2019:
    ord('a')
    return the number
    chr('65')
    return the alpha
.
                                  08/08/2019  mysql:
Keyword:
    1. Like
    2.Between
    3.references
    4.in
    5.exist
    6.check
Data type in mysql:
    char    size(20) fixed lenth
    varchar
    int
    float
    long
    lob         large object
    blog        binary large object
    datetime    for date & time
Sql language:
    DDL-Data Difinition language
    DML-Data manipulation language
    TCL-Transition control language
command for sql:
    CREATE DATABASE name;
    USE database_name;
    SHOW TABLES;
    CREATE TABLE name
    (
    feiled one INT PRIMARY KEY,
    feiled two DATA TYPE SIZE
    )
    DESC table_name;
    DROP TABLE table_name;
    INSERT INTO table_name VALUES(,'');
    desc or describe name;
    drop table name
    select * from Table_name;
    select feild_name,feild_data from table_name;
    select * from table_name WHERE salary>20000;
    select * from table_name WHERE salary between 12000   AND 21500;
    select * from table_name WHERE salary in depno(10,20);
    select * from table_name WHERE ename LIKE 'R%';
    select * from table_name WHERE ename LIKE '_a%';
    for joit two table--
    select e.ename,s.dname from table_name1 e,table_name2 s(first carchater)
        where s.deptno.=e.deptno;
    select * from table_name order by name(feild_name) asc/dsc
    select sum(salary) from table_name
    select deptno,sum(salary) from table_name
        group by deptno;
        
    select deptno,sum(salary) from table_name
        group by deptno having sum(salary)>35000;
     

    
    
    
    
    