def solution():
    n,q=tuple(int(x) for x in input().split())
    a=[int(x) for x in input().split()]
    n=len(a)
    d=[0]*n
    d[0]=a[0]
    flage_if_chage_a=False
    for i in range(1,n):
        d[i]=a[i]-a[i-1]    
    prefix=[0]  
    for i in a:
        prefix.append(prefix[-1]+i)
    for _ in range(q):
        caozuo=[int(x) for x in input().split()]
        if len(caozuo) ==3:
            if not flage_if_chage_a:
                print(prefix[caozuo[1]+1]-prefix[caozuo[0]])
            else:
                a[0]=d[0]
                for i in range(1,n):
                    a[i]=a[i-1]+d[i]
                prefix = [0]
                for value in a:
                    prefix.append(prefix[-1] + value)
                print(prefix[caozuo[1]+1]-prefix[caozuo[0]])
            flage_if_chage_a=False
        else:
            flage_if_chage_a=True
            d[caozuo[0]]+=caozuo[2]
            if caozuo[1]+1<n:
                d[caozuo[1]+1]-=caozuo[2]
solution()


            