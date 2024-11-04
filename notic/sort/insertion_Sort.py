class Solution(object):
    def insrtion_sort(nums):
        for i in range(1,len(nums)-1):
            key= nums[i]
            #insert key into sorted nums[0,```,i]
            j=i-1
            while j>0 and nums[j]>key:
                nums[j+1]=nums[j+1]
                j-=1
            nums[j+1]=key
        return nums
solution = Solution()
print(Solution.insrtion_sort([4,2,3,1]))
                    

