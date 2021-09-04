t = int(input())
while t > 0:
    n = int(input())
    if n %  2 == 0:
        tong = 0
        for i in range(2,n+1,2):
            tong += 1/i
        print(format(tong,'.6f'))
    if n % 2 == 1:
        tong = 0
        for i in range(1,n+1,2):
            tong += 1/i
        print(format(tong,'.6f'))
    t-=1