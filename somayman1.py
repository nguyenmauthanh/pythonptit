string = str(input())
dem_4 = 0
dem_7 = 0
for i in range(len(string)):
    if(string[i] == '4'):
        dem_4+=1
    elif(string[i]=='7'):
        dem_7+=1
if dem_4 + dem_7 == 4 or dem_4 + dem_7 == 7:
    print("YES")
else:
    print("NO")