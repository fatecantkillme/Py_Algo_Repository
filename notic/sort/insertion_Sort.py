class Solution(object):
    def insrtion_sort(self, nums):
        for i in range(1,len(nums)-1):
            for j in range(i-1,0,-1):
                if nums[i]>=nums[j]:
                    

