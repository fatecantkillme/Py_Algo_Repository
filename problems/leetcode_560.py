class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        prefix_sum=0
        prefix_sums={0:1}
        for i in nums:
            prefix_sum+=i
            if prefix_sum - k in prefix_sums:
                ans+=prefix_sums[prefix_sum-k]
            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
        return ans