import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True
def sum(n):
    sum1 = 0
    while n:
        sum1 += n % 10
        n //= 10
    return sum1

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b, a%b)

def main():
    t = int(input())
    while t > 0:
        a,b = [int(x) for x in input().split()]  
        if(snt(sum(gcd(a,b)))):
            print("YES")
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    main()