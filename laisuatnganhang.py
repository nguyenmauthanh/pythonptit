t = int(input())

while t>0:
    
    a = [float(x) for x in input().split()]
    
    sum1 = a[0]
    count = 0
    while sum1 < a[2]:
        sum1 = sum1 + sum1*a[1]/100
        
        count+=1
    print(count)
    
    t-=1