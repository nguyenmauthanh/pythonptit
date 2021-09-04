import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

t = int(input())
while t>0:
    s = str(input())
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    if(snt(tong)):
        print("YES")
    else:
        print("NO")
    t-=1