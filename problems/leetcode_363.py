class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            self.presum = []
            return
        m, n = len(matrix), len(matrix[0])
        self.presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.presum[i + 1][j + 1] = (
                    self.presum[i + 1][j] +
                    self.presum[i][j + 1] -
                    self.presum[i][j] +
                    matrix[i][j])
        
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.presum[row2 + 1][col2 + 1] -
            self.presum[row1][col2 + 1] -
            self.presum[row2 + 1][col1] +
            self.presum[row1][col1]
        )