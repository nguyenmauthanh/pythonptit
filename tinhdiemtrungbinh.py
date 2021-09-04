n = int(input())

a = sorted([float(x) for x in input().split()])

tong = 0
count = 0
for i in range(1,len(a)-1):
    if(a[i] != a[0] and a[i] != a[len(a)-1]):
        tong += a[i]
        count += 1

tong = tong/count
print('%.2f' % tong)

