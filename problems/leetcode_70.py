class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]#保证n输入为1时 dp[1]=2的操作不会指针溢出
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]