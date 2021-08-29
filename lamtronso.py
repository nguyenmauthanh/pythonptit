def main():
    for _ in range(int(input())):
        n = input()[::-1]
        ans = ""
        up = 0
        for i in range(len(n) - 1):
            if int(n[i]) + up >= 5:
                up = 1
            else:
                up = 0
            ans += '0'
        if up:
            ans += str(int(n[-1]) + 1)[::-1]
        else:
            ans += n[-1]
        print(ans[::-1])

if __name__ == '__main__':
    main()

