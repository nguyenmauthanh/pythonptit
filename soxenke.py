def k1(s):
    if len(s) % 2 == 1:
        return True
    return False
def k2(s):
    if s[0] != s[1]:
        return True
    return False
def k3(s):
    for i in range(0,len(s)-2,2):
        if s[i] != s[i+2]:
            return False
    return True
t=int(input())
while t > 0:
    s =str(input())
    if k1(s) and k2(s) and k3(s):
        print("YES")
    else:
        print("NO")
    t-=1
