t = int(input())

while t > 0:
    string = str(input())
    check = True
    if string[0] == string[len(string)-2] and string[1] == string[len(string)-1]:
        check = False
    else:
        check = True
    if check:
        print("NO")
    else:
        print("YES")
    t = t-1