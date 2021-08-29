def tich(n):
    sum = 1
    while n:
        sum *= n % 10
        n //= 10
    return sum



t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    vp = []
    for i in range(n):
        vp.append([tich(a[i]) , a[i]])
    vp.sort()
    for i in range(len(vp)) :
        print(vp[i][1], end = " ")
    print()
    t-=1