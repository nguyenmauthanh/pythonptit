for _ in [0] * int(input()):
    n = int(input())
    l, res = 2, 0
    # print(l)
    while l * (l - 1) < 2 * n:
        if ( n - l * (l - 1) // 2 ) % l == 0: res += 1
        l += 1
    print(res)