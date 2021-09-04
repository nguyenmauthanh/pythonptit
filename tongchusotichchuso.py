t = int(input())

while t>0:
    s = str(input())
    tong = 0
    tich = 1
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            tong += int(s[i])
        elif i % 2 == 1 and s[i] != '0':
            tich *= int(s[i])
        elif i % 2 == 1 and s[i] == '0':
            count += 1
    if count == len(s)//2:
        print(tong,0,sep=" ")
    else:
        print(tong,tich,sep=" ")
    t-=1