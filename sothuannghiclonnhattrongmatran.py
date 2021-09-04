def k1(n):
    s = str(n)
    if len(s) == 1:
        return False
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

[n,m] = [int(x) for x in input().split()]

mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])
minm = 0
for i in range(n):
    for j in range(m):
        if(k1(mat[i][j])):
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