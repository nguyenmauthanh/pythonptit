n = int(input())

c = []
l = []
a = [int(x) for x in input().split()]
while len(a) < n:
    a += [int(x) for x in input().split()]
for i in range(n):
    if a[i] % 2 == 0:
        c.append(a[i])
    else:
        l.append(a[i])
c.sort()
l.sort(reverse=True)
k1 = k2 = 0
for i in range(n):
    if(a[i] % 2 == 1):
        print(l[k1],end=" ")
        k1+=1
    else:
        print(c[k2],end=" ")
        k2+=1
