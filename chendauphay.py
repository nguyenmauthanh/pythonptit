
s = input()[::-1]
ans = ""
for i in range(len(s)):
    ans += s[i]
    if i % 3 == 2 and i != len(s) - 1:
        ans += ','
print(ans[::-1])
