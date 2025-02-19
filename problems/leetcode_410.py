class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=max(nums)
        right=sum(nums)
        while left<right:
            max_num=left+((right-left)>>1)
            if not self.if_feasible(nums,k,max_num):
                left=max_num+1
            else:
                right=max_num
        return left

    
    def if_feasible(self,nums,k,max_num):
        current_sum=0
        dived_num=1
        for num in nums:
            current_sum+=num
            if current_sum>max_num:
                dived_num+=1
                if dived_num>k:
                    return False
                current_sum=num
        return True