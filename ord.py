ch=ord('a')
for i in range(1,10):
    for j in range(1,5):
        print(chr(ch),end='')
        ch+=1
    print()
    if ch==122:
        print('yz')
        break
    ch-=1