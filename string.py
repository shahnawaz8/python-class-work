name=input('Enter Name')
li=name.split()
lenth=len(li)
shortName=''
for x in range(lenth):
    shortName=shortName+' '+li[x][0]
shortName=shortName+''+li[lenth-1]
print((shortName.title()).strip())
