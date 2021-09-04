t = int(input())
list = []
while t > 0:
    s = str(input())
    count = 0
    ok = False
    for i in range(len(s)):
        if s[i].isdigit():
            count =  count*10 + int(s[i])
            ok = True
        else:
            if(ok == True): 
                list.append(count)
            ok = False
            count = 0
    if ok == True:
        list.append(count)
    t-=1
list.sort()
for i in list:
    print(i)