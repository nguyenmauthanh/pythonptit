test=int(input())
while test>0:
    a=int(input())
    b=False
    while a>0:
        t=a%10
        if t==4 or t==7:
            b=True
        else:
            b=False
            break
        a=a//10
    print("YES" if b==True else "NO")
    test-=1

