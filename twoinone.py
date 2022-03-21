ans='y'
fileone=[]
filetwo=[]
filethree=[]
while ans=='y':
    print('1. Add record')
    print('2.Show One')
    print('3,divide a list')
    print('4.Show Two')
    print('5.Show Three')
    print('6.Exit')
    print('/nEnter your choise between 1...6')
    ch=(int)(input())
    if ch==1:
        name=(int)(input('Enter name'))
        fileone.append(name)
        print('record saved')
    elif ch==2:
        print('/Student Name/n')
        for x in fileone:
            print(x)
    elif ch==3:
        a=len(fileone)
        b=a//2
        filetwo=fileone[0:b]
        filethree=fileone[b:a]
        print('list divided/n')
    elif ch==4:
        print('/Student Name/n')
        for m in filetwo:
            print(m)
    elif ch==5:
        print('/Student Name/n')
        for n in filethree:
            print(n)
    else:
        exit(0)
    print('Do you want to continue Y/n')
    ans=input()