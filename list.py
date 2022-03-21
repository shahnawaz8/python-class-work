family=[]
gf=input('grandfather name')
family.append(gf)
for x in range(2):
    child=[]
    father=[]
    name=input('father name')
    father.append(name)
    for y in range(2):
        name1=input('child name')
        child.append(name1)
    father.append(child)
    family.append(father)
print(family)