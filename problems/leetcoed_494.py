class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size=len(nums)
        table=dict()

        def dfs(i,cur_sum):
            if size==i:
                if cur_sum==target:
                    return 1
                else:
                    return 0
            if (i,cur_sum) in table:
                return table[(i,cur_sum)]
            else:
                cnt=dfs(i+1,cur_sum-nums[i])+dfs(i+1,cur_sum+nums[i])
                table[(i,cur_sum)]=cnt
            return cnt
        return dfs(0,0)