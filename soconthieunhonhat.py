n = int(input())
a = sorted([int(x) for x in input().split()])
check = True
for i in range(n-1):
    if(a[i+1] - a[i] > 1):
        print(a[i]+1)
        check = False
        break
if check == True:
    print(a[n-1] + 1)
