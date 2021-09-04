t = int(input())

while t > 0:
    s =str(input())
    tich = 1
    tong = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != '0':
            tich *= int(s[i])
        elif i % 2 == 1:
            tong += int(s[i])
    print(tich,tong,sep=" ")
    t-=1