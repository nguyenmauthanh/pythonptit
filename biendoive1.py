while True:
    n = int(input())
    count = 1
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        while n != 1:
            if n % 2 == 0:
                n = n/2
                count += 1
            elif n % 2 == 1:
                n = n*3 + 1
                count +=1
        print(count)