while True:
    nhap=[str(x) for x in input().split()]
    k=int(nhap[0])
    if k==0:
        break
    b=nhap[1]
    ans=""
    P = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_","."]
   
    for i in range(len(b)):
        for j in range(len(P)):
            if b[i]==P[j]:
                c=int((j+int(k))%28)
                ans+=P[c]
    print(ans[::-1])
    
            
    