ans='y'
student=[]
while ans=='y':
    print('1. Add record')
    print('2. Search Record')
    print('3.Show All')
    print('4.Update Record')
    print('5. Delete Record')
    print('6.Exit')
    print('/nEnter your choise between 1...6')
    ch=(int)(input())
if ch==1:
    name=input('Enter name')
    student.append(name)
    print('record saved')
elif ch==2:
    sname=input('enter name you want to search')
    if sname in student:
            print('Name found')
    else:
            print('Not found')
elif ch==3:
        print('/Student Name/n')
        for x in student:
            print(x)
elif ch==4:
        sname=input('name to update')
        nname=input('name to update')
        if sname in student:
            i=student.index(sname)
            student[i]=nname
            print('Name updated')
        else:
            print('Name not found')
        
elif ch==5:
        dname=input('Name for delete')
        if dname in student:
            student.remove(dname)
            print('Name deleted')
        else:
            print('Name not found')
else:
        exit(0)
        print('Do you want to continue Y/n')
        ans=input()