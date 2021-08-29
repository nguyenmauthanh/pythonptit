while True:
    arr = [int(x) for x in input().split()]
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3] and arr[0] == 0:
        break
    ans = 0
    while not (arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]):
        ans += 1
        arr = [abs(arr[i] - arr[i+1]) if i < 3 else abs(arr[3] - arr[0]) for i in range(4)]
    print(ans)