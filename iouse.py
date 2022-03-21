ans='y'
import io
import shutil
import os
fname='amar.txt'
while ans=='y' or ans=='Y':
    print('1. Add')
    print('2. Display')
    print('3. Search')
    print('4. Modify')
    print('5. delete')
    print('6.Exit')
    print('/nEnter your choise between 1...7')
    ch=int(input())
    if ch<=6:
        if ch==1:
            with open(fname,'a+') as file:
                name=input('Enter name')+'\n'
                file.write(name)
        elif ch==2:
            with open(fname,'a+') as file:
                slist=file.readline()
                for x in slist:
                    print(x)
        elif ch==3:
            slist=[]
            with open(fname) as file:
                slist=file.readlines()
                sname=input('Enter name for search')
                if sname in slist:
                    print('name found',sname)
                else:
                    print('name not found')
        elif ch==4:
            slist=[]
            with open(fname) as file:
                slist=file.readlines()
            oname=input('Name')+'\n'
            nname=input('newname')+'\n'
            if oname in slist:
                i=slist.index(oname)
                slist[i]=nname
                print('Updated')
            else:
                print('not found')
            with open(fname,'w') as file:
                for x in slist:
                    file.write(x)
        elif ch==5:
            slist=[]
            with open(fname) as file:
                slist=file.readlines()
            nname=input('newname')+'\n'
            if oname in slist:
                slist.remove(oname)
                print('deleted')
            else:
                print('not found')
            with open(fname,'w') as file:
                for x in slist:
                    file.write(x)
            
        else:
            exit(0)
        print('Do you want to continue Y/n')
        ans=input()