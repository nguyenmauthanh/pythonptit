num=str(input())
flag =1

for i in range(len(num)):
    if num[0]=='8':
        flag=0
        break
    if num[i]=='6' or num[i]=='8':
        flag=1
    elif num[i]!='6' and num[i]!='8':
        flag=0
        break

flag1=1
for k in range(len(num)-1):
    count=0
    for j in range(k+1,len(num)):
        if num[j]=='8':
           count+=1
        else:
            count=0
            break
    if count>2:
        flag1=0
        break

if flag == 1 and flag1==1 :
    print("YES")
else:
    print("NO")