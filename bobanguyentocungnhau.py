import math

l, r = map(int, input().split())
for i in range(l, r - 1):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if math.gcd(i,j) == math.gcd(j, k) == math.gcd(k, i) == 1:
                print("({}, {}, {})".format(i,j,k))