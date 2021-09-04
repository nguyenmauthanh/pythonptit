import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def k1(s):
    count = 0
    for i in range(len(s)):
        if snt(int(s[i])):
            count +=1
    if count > len(s)-count:
        return True
    else:
        return False
n = int(input())
while n > 0:
    s = str(input())
    if snt(len(s)) and k1(s):
        print("YES")
    else:
        print("NO")
    n-=1