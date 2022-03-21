di={}
print('How Many Employ You Want to Enter')
E=int(input())
i=1
for x in range(E):
    print('Enter Employ Name',i)
    name=input()
    fixed_salary=int(input('Enter Fixed Salary to Employ'))
    y=fixed_salary/30
    work=int(input('Enter Working Days in a Month'))
    if work>0 and work<31:
        month=work*y
        di[name]=month
        i+=1
    else:
        print('Enter Working day B/w 1 to 30')
        continue
for x in di:
            print('Name',x,':','Salary',di[x])
