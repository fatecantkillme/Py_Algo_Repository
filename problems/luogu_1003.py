def solution():
    n=int(input())
    info=[[int(x) for x in input().split()] for _ in range(n)]
    x,y=tuple(int(m) for m in input().split())
    for i in range(n-1,-1,-1):
        if x <= info[i][0]+info[i][2] and x>=info[i][0] and y<=info[i][1]+info[i][3] and y>=info[i][1]:
            print(i+1)
            return
    print(-1)
    return

solution()