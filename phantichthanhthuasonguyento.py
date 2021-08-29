t = int(input())
while t > 0:
    n = int(input())
    i = 2
    count = 0
    print("1 * ",end="")
    while(n > 1):
        while(n % i == 0):
            n //= i
            count += 1
        if count != 0: 
            print(i,count,sep="^",end=" ")
            if n != 1: print("* ",end="")
        count = 0
        i += 1
    print()
    t-=1