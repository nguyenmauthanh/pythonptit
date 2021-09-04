s = str(input())

while len(s) > 1:
    count = 0
    ans = ""
    for i in range(int(len(s)/2)):
        count = count*10 + int(s[i])
    
    count1 = 0
    for i in range(int(len(s)/2) , len(s)):
        count1 = count1*10 + int(s[i])
    ans += str(count + count1)
    print(ans)
    s = ans