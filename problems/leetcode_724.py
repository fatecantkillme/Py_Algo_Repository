class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all=0
        left=0
        for  i in range(len(nums)):
            all+=nums[i]
        right=all-nums[0]
        if right==0:
            return 0
        for i in  range(1,len(nums)):
            left+=nums[i-1]
            right+=-nums[i]
            if left==right:
                return i
        return -1
