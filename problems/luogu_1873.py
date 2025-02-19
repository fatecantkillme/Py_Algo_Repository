def solution():
    N,M=tuple(int(item) for item in input().split())
    hight=[int(i) for i in input().split()]
    left=0
    right=max(hight)
    while left<right:
        mid = left + ((right - left + 1) >> 1)
        if if_ok(hight,M,mid):
            left=mid
        else:
            right=mid-1
    print(right)
    return right
        
def if_ok(hight,M,H):
    res=0
    for item in hight:
        h=item-H if item >=H else 0
        res+=h
    if res>=M:
        return True
    else:
        return False

solution()