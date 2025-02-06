class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.presum=[]
            return
        m,n=len(matrix),len(matrix[0])
        self.presum=[[0]* (n+1) for _ in range(m+1)]
        for i in range(m):
            for j  in range(n):
                self.presum[i+1][j+1]=self.presum[i+1][j]+self.presum[i][j+1]-self.presum[i][j]+matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1=row1+1
        c1=col1+1
        r2=row2+1
        c2=col2+1
        return self.presum[r2][c2]-self.presum[r2][c1-1]-self.presum[r1-1][c2]+self.presum[r1-1][c1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)