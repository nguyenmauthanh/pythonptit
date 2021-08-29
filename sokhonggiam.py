t = int(input())
while t > 0:
    string = input()
    check = 0
    for i in range(len(string)-1):
        if(string[i] <= string[i+1]):
            check = 0
        else:
            check = 1
            break
    if check == 1:
        print("NO")
    else: 
        print("YES")
    t=t-1
