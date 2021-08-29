def main():
    p = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(int(input())):
        s = input()
        a = [abs(p.find(s[i])-p.find(s[i+1])) for i in range(len(s)-1)]
        s = s[::-1]
        b = [abs(p.find(s[i])-p.find(s[i+1])) for i in range(len(s)-1)]
        ok = True
        for i in range(len(a)):
            if(a[i]!=b[i]):
                ok = False
                break
        if ok: print("YES")
        else: print("NO")

if __name__ == '__main__':
    main()