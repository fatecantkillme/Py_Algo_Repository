def binary_search(arr,start,end,key):
    res=-1
    mid=start+(end-start)>>1
    while start<=end:
        mid=start+((end-start)>>1)
        if arr[mid]==key:
            res=mid
            break
        else:
            if arr[mid]<key:
                start=mid+1
            else:
                end=mid-1
    return res

arr=[1,2,3,4,5]
print(binary_search(arr,0,4,2)==1)