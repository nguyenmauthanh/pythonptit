import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

[n,m] = [int(x) for x in input().split()]

mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])

minm = 0
for i in range(n):
    for j in range(m):
        if(snt(mat[i][j])):
            minm = max(mat[i][j],minm)
        
ok=True
for i in range(n):
    for j in range(m):
        if mat[i][j] == minm:
            ok =False
            break
if ok == True:
    print("NOT FOUND")
else:
    print(minm)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == (minm):
                print("Vi tri [{}][{}]".format(i,j))