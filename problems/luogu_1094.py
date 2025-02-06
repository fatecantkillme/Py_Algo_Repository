def solution():
    w = int(input())
    n = int(input())
    P = [int(input()) for _ in range(n)]
    P.sort()
    P.reverse()
    ans = 0
    
    while P:
        if len(P) >= 2:
            if (P[0] + P[-1]) > w:
                P.pop(0)
                ans += 1
                continue
        else:
            if P:
                P.pop()
                ans += 1
            break
        
        for i in range(len(P)-1, 0, -1):
            if (P[0] + P[i]) > w:
                ans += 1
                P.pop(0)
                P.pop(i)
                break
            else:
                if i == 1:
                    ans += 1
                    P.pop(0)
                    if P:
                        P.pop(0)
                    break
    
    print(ans)

solution()
        