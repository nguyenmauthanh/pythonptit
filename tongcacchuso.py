t = int(input())
while t > 0:
    s =str(input())
    char_c = [0] * 26
    sum = 0
    for i in range(len(s)):
        if s[i] >= "A" and s[i] <= "Z":
            char_c[ord(s[i]) - ord("A")] += 1
        else:
            sum += ord(s[i]) - ord("0")
    res = ""
    for i in range(26):
        ch = chr(ord("A")+i)
        while char_c[i]:
            res += ch
            char_c[i] -=1
    if sum > 0:
        res += str(sum)
    print(res)
    t-=1