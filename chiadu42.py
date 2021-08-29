
a=[]
for i in range(10):
    a.append(int(input()))
count=10
for i in range(10):
    a[i]=a[i]%42
a.sort()
for i in range(9):
    if a[i]==a[i+1]:
        count-=1
print(count)

        
