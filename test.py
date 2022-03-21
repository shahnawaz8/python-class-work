ans='y'
fileone=['amir,khan']
filetwo=[]
while ans=='y':
    print('1. Add record')
    print('2. Delete Record')
    print('3.Show One')
    print('4.Show Two')
    print('5.Exit')
    print('/nEnter your choise between 1...6')
    ch=(int)(input())
    if ch==1:
        name=input('Enter name')
        fileone.append(name)
        print('record saved')
    elif ch==2:
        dname=input('Input for Name')
        i=fileone.index(dname)
        nam=fileone.pop(i)
        filetwo.append(nam)
    elif ch==3:
        print('/Student Name/n')
        for x in fileone:
            print(x)
    elif ch==4:
        print('/Student Name/n')
        for m in filetwo:
            print(m)
    else:
        exit(0)
    print('Do you want to continue Y/n')
    ans=input()