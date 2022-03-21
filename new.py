li=[1,2,3,4,5,6,7,8,9]
rli=[]
print('Enter No. you want to delete')
new=(int)(input())
if new in li:
    a=li.index(new)
    s=li.pop(a)
    rli.append(s)
    print('data deleted')
else:
    print('enter valid no.')

