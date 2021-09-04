import math
n  = int(input())

mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])
check = int(input())
tt = 0
td = 0
for i in range(n):
    for j in range(n-1,-1,-1):
        if i < j:
            tt += mat[i][j]
        if i > j:
            td += mat[i][j]

if abs(tt - td) <= check:
    print("YES")
    print(abs(tt-td))
else:
    print("NO")
    print(abs(tt-td))