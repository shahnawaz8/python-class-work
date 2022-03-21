ans='y'
aset=set()
bset=set()
aset={1,2,3,4,5,6,7,8,9,10}
bset={11,12,13,14,15,16,17,18,19,20}
while ans=='y':
    print('press 1. for Add data in Set 1')
    print('press 2. for Add data in Set 2')
    print('press 3. for Show Set 1')
    print('press 4. for Show Set 2')
    print('press 5. for Union of both')
    print('press 6. for Intersection of both')
    print('press 7. for Difference of both')
    print('press 8. To check uncommon data in both')
    print('press 9. for delete data from the set 1')
    print('press 10.for delete data from the set 2')
    ch=(int)(input('What do you want to do'))
    if ch==1:
        data1=(int)(input('Enter No. to add data in set one'))
        aset.add(data1)
        print('Data Succesfully add in set 1')
    elif ch==2:
        data2=(int)(input('Enter No. to add data in set two'))
        bset.add(data2)
        print('Data Succesfully add in set 2')
    elif ch==3:
        s1=aset
        print(s1)
    elif ch==4:
        s2=bset
        print(s2)
    elif ch==5:
        u=aset.union(bset)
        print(u)
    elif ch==6:
        i=aset.intersection(bset)
        print(i)
    elif ch==7:
        d1=aset-bset
        print(d1)
        d2=bset-aset
        print(d2)
    elif ch==8:
        sy=aset^bset
        print(sy)
    elif ch==9:
        delete=(int)(input('Enter data you want to delete from set one'))
        if delete in aset:
            delete1=aset.discard(delete)
            print('Data deleted from set 1')
        else:
            print('Data not present in the set 1')
    elif ch==10:
        delete2=(int)(input('Enter data you want to delete from set two'))
        if delete2 in bset:
            delete3=bset.discard(delete2)
            print('Data deleted from set 2')
        else:
            print('Data not present in the set 2')
    
    else:
        exit(0)
    print('Do You Want To Continue Y/N')
    ans=input()
      