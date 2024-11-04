class Solution(object):
    dp=[[0]]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo=[[0 for _ in range(n)] for _ in range(m)]
        return self.my_path(m-1,n-1,memo)
    
    def my_path(self,m,n,memo):
        if m==0 and n ==0:
            return 1
        if memo[m][n]!=0:
            return memo[m][n]
        if m-1>=0:
            memo[m][n]+=self.my_path(m-1,n,memo)
        if n-1>=0:
            memo[m][n]+=self.my_path(m,n-1,memo)
        return memo[m][n]