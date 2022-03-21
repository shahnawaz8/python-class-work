ans='y'
fileone=[1,1,1]
filetwo=[]
filethree=[]
while ans=='y':
    print('1. Add record in fileone')
    print('2. Add record in filetwo')
    print('3. Add record in filethree')
    print('4. Delete Record')
    print('5.Show One')
    print('6.Show Two')
    print('7.Show Three')
    print('8.Exit')
    print('/nEnter your choise between 1...6')
    ch=(int)(input())
    if ch==1:
        name=(int)(input('Enter name'))
        fileone.append(name)
        print('record saved')
    elif ch==2:
        name1=(int)(input('Enter name'))
        filetwo.append(name1)
        print('record saved')
    elif ch==3:
        name2=(int)(input('Enter name'))
        filethree.append(name2)
        print('record saved')
    elif ch==4:
        dname=(int)(input('Input for Name'))
        i=fileone.index(dname)
        j=filetwo.index(dname)
        k=filethree.index(dname)
        nam=fileone.pop(i)
        nam1=filetwo.pop(j)
        nam2=filethree.pop(k)
    elif ch==5:
        print('/Student Name/n')
        for x in fileone:
            print(x)
    elif ch==6:
        print('/Student Name/n')
        for m in filetwo:
            print(m)
    elif ch==7:
        print('/Student Name/n')
        for m in filetwo:
            print(m)
    else:
        exit(0)
    print('Do you want to continue Y/n')
    ans=input()