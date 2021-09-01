n = int(input())

a = []
for i in range(n):
    s = str(input())
    a.append(s)
dem = 0
count = 0
for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C':
            dem+=1
    count += (dem*(dem-1))/2
for i in range(n):
    dem = 0
    for j in range(n):
        if(a[j][i] == 'C'):
            dem +=1
    count += (dem*(dem-1))/2
print(int(count))
