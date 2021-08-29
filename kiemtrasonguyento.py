import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

[n, m] = [int(x) for x in input().split()]
a = []
for i in range(n):
    a1 = [int(x) for x in input().split()]
    a.append(a1)
for i in range(n):
    for j in range(m):
        if snt(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
        print(a[i][j], end=' ')
    print()