for x in range(5,0,-1):           
    for y in range(x,0,-1):       
        print('*',end='')      
    print()
for x in range(1,6):           
    for y in range(x+1,6):
        print('*',end='')
    print()
    
for i in range(1,6):           
    for j in range(6,1,-1):
        if(i==2 and j>1) or (i==3 and j>2) or (i==4 and j>3) or (i==5 and j>4):
            print('*',end='')
        else:
            print(end=' ')
    print()
    
    