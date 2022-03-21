def add(x):
    k=0
    while x>=1:
        i=x%10
        j=x//10
        k=i
        x=j
    print('total',k)
    
    
    
def total(*no):
    sum=0
    for x in no:
        sum+=x
    print('Total',sum)
total(1,2,3,4,5)
add(12345)

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
    
print(fact(5))

