class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num=nums
        self.prefix=[0]
        for i in nums:
            self.prefix.append(self.prefix[-1]+i)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)