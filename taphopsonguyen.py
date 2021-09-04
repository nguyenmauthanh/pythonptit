[n,m] = [int(x) for x in input().split()]

a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])

c = a.intersection(b)
c = sorted(c)
for i in c:
    print(i,end=' ')
print()
d = a.symmetric_difference(b)
d = sorted(d)
e = b.symmetric_difference(a)
e = sorted(e)
for i in d:
    if i in a:
        print(i,end=' ')
print()
for i in e:
    if i in b:
        print(i,end=' ')
