t=int(input())
while t>0:
    name=str(input())
    for i in range(len(name)):
        if(name[i].isdigit()):
            print(name[i-1]*int(name[i]),end='')
    print()
    t-=1
