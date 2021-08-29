test = int(input())
while test > 0:
    [m, n, k] = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    m1,n1,k1 = 0,0,0
    check = True
    while m1 < m and n1 < n and k1 < k:
        if a[m1] == b[n1] and b[n1] == c[k1]:
            check = False
            print(a[m1],end=" ")
            m1 += 1
            n1 += 1
            k1 += 1
        elif a[m1] < b[n1]:
            m1 += 1
        elif b[n1] < c[k1]:
            n1 += 1
        else:
            k1 += 1
    if check == True:
        print("NO", end="")
    print()
    test -= 1