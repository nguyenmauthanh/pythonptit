def tim(arr,n):
    ok=dict() 
    for i in range(n):
        if arr[i] in ok.keys():
            ok[arr[i]]+=1
        else:
            ok[arr[i]]=1
    max_count=0
    res=-1
    for i in ok:
        if(max_count<ok[i]):
            res=i
            max_count=ok[i]
    if max_count>n/2:
        return res
    else:
        return 0
t=int(input())
while t>0:
    n=int(input())
    a = [int(x) for x in input().split()]
    res=tim(a,n)
    if res!=0:
        print(res)
    else:
        print("NO")
    t-=1


    
