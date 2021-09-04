import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

t = int(input())

while t > 0:
    s =str(input())
    ok = True
    for i in range(len(s)):
        if snt(i) == True and snt(int(s[i])) == False:
            print("NO")
            ok = False
            break
        if snt(i) == False and snt(int(s[i])) == True:
            print("NO")
            ok = False
            break
    if ok == True:
        print("YES")
    t-=1





