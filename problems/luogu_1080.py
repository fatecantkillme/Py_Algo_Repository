def solution():
    n=int(input())
    p=[]
    for _ in range(n):
        p.append([int(z) for z in input().split()])
    for i in range(n):
        for j in range(n):
            if max(p[j+1][1],p[j][1]*p[j][0])>max(p[j][1],p[j+1][1]*p[i][0]):
                p[i],p[j]=p[j],p[i]
                
    
