t = int(input())
count = 0
arr = [int(x) for x in input().split()]
for i in range(t-1):
    if arr[i] != arr[i+1]:
        count += 1
print(count)
