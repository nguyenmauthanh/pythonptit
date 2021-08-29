t=int(input())
while t>0:
    n=int(input())
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    a.sort()
    count=0
    max_count=0
    res=0
    for i in range (n):
        count=a.count(a[i])
        if max_count<count:
            max_count=count
            res=a[i]
    print(res)
    t-=1
        