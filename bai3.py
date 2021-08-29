string = input()
sum = int()
for i in range(0, len(string) - 2):
    if(i >= 0 and i <= 9):
        sum += i
if sum == int(string[len(string) - 1]):
    print("YES")
else:
    print("NO")
