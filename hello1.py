def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    mp = dict()
    for x in arr:
        if x not in mp:
            mp[x] = 0
        mp[x] += 1
    ans = ansCnt = 0
    for x in mp:
        if mp[x] > ansCnt:
            ans, ansCnt = x, mp[x]
    if ansCnt > n / 2:
        print(ans)
    else:
        print("NO")


def main():
    t = int(input())
    for _ in range(t):
        solve()


main()