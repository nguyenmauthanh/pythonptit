
def tinh(s):
    count = 0
    sum = 0
    while len(s) > 1:
        count += 1
        sum = 0
        for i in range(len(s)):
            sum += (ord(s[i]) - ord('0'))
        s = str(sum)
    return count


s = str(input())
if len(s) == 1:
    print(len(s))
else:
    print(tinh(s))

    