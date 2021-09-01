# sang nguyen to 
p = [1] * 8001; p[0] = p[1] = 0 #init
for i in range(2, 8000):
    if p[i]:
        for j in range(i**2, 8000, i): p[j] = 0
        
# drive code
n, x = [int(x) for x in input().split()]
print(x, end=' ')
for _ in range(n):
    idx = p.index(1)
    x += idx
    p[idx] = 0
    print(x, end=' ')