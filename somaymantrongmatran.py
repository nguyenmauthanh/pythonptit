[n,m] = [int(x) for x in input().split()]

mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])
minm = 10001
maxm = 0
for i in range(n):
    for j in range(m):
        minm = min(mat[i][j],minm)
        maxm = max(mat[i][j],maxm)
ok=True
for i in range(n):
    for j in range(m):
        if mat[i][j] == (maxm-minm):
            ok =False
            break
if ok == True:
    
    print("NOT FOUND")
else:
    print(maxm - minm)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == (maxm-minm):
                print("Vi tri [{}][{}]".format(i,j))