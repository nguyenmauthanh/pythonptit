t = int(input())

while t > 0:
    s = str(input())
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
        
    
    s = str(tong)
   
    ok = True
    if len(s) == 1:
        print("NO")
    else:
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                ok =False
                break
        if ok == True:
            print("YES")
        else:
            print("NO")
        
    t-=1