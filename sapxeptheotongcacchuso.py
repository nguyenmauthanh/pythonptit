def tong(n):
    sum = 0
    while n>0:
        sum += n % 10
        n //= 10
    return sum

t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    vp = []
    for i in range(n):
        vp.append([tong(a[i]),a[i]])
    vp.sort()
    for i in range(len(vp)):
        print(vp[i][1] , end=" ")
    print()
    t-=1