from collections import Counter
t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    count = Counter(a)
    for i in range(n):
        if count[a[i]] % 2 == 1:
            print(a[i])
            break
    t-=1