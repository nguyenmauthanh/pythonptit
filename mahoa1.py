t = int(input())

while t>0:
    string = str(input())
    k = 0
    ans = ""
    count = 1
    for i in range(0,len(string)):
        if i+1 == len(string):
            ans += str(count) + string[i]
        elif string[i] == string[i+1]:
            count += 1
        else:
            ans += str(count) + string[i]
            count = 1
    print(ans)
    t-=1
        

