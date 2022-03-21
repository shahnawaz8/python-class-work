ans='y'
dict1={}
dict2={}
while ans=='y':
    print('press 1. for Add data in Dictionary')
    print('press 2. for Show Data')
    print('press 3. for Show all key')
    print('press 4. for Show all value')
    print('press 5. for Search value')
    print('press 6. for delete data from the Dictionary')
    ch=(int)(input('What do you want to do'))
    if ch==1:
        key=(input('Enter Key'))
        value=(input('Enter Value'))
        dict1[key]=value
        print('Data Succesfully add in Dictionary')
    elif ch==2:
        for x in dict1:
            print(x,':',dict1[x])
    elif ch==3:
        print(dict1.keys())
    elif ch==4:
        print(dict1.values())
    elif ch==5:
        found=1
        key=input('Enter Key')
        for x in dict1:
            if x==key:
                print('key',x,':','value',dict1[x])
                found=1
                break
            else:
                found=0
        if found==0:
            print(x,'is not present in the dictionary')
    elif ch==6:
        delete=(input('Enter key for you want to delete the value from Dictionary'))
        dict1.pop(delete)
        print('Deleted')
    else:
        exit(0)
    print('Do You Want To Continue Y/N')
    ans=input()
      